import vk_api
from datetime import datetime
import os

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
    response = vk.wall.get(count=5)
    for item in response['items']:
        text = item['text']
        unixtime = item['date']
        datetime_object = datetime.fromtimestamp(unixtime)
        print(f"{text}\ndate: {datetime_object.strftime('%Y-%m-%d')}, time: {datetime_object.strftime('%H:%M:%S')}\n")


if __name__ == '__main__':
    main()