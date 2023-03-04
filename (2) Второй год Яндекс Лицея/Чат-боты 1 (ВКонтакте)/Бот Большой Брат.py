import vk_api
from datetime import datetime
import os
from vk_api import upload


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def main():
    login, password = os.environ['login'], os.environ['password']
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    def handle_new_message(event):
        user_id = event.obj['message']['from_id']
        user_info = vk.users.get(user_ids=user_id, fields='city')[0]
        first_name = user_info['first_name']
        city = user_info.get('city', {}).get('title')
        message_text = f"Привет, {first_name}!"
        if city:
            message_text += f" Как поживает {city}?"
        vk.messages.send(user_id=user_id, message=message_text)

    longpoll = vk_api.longpoll.VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == vk_api.longpoll.EventType.MESSAGE_NEW:
            handle_new_message(event)


if __name__ == '__main__':
    main()