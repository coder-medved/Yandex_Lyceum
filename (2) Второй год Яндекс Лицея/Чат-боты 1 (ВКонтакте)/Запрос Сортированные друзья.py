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
    response = vk_session.method('friends.get', {'order': 'name', 'fields': 'bdate'})

    # Обработка каждого друга и вывод информации в нужном формате
    for friend in response['items']:
        last_name = friend['last_name']
        first_name = friend['first_name']
        bdate = friend.get('bdate', 'не указана')
        bdate = datetime.strptime(bdate, '%d.%m.%Y').strftime('%Y-%m-%d') if bdate != 'не указана' else bdate
        print(f'{last_name} {first_name}; дата рождения: {bdate}')


if __name__ == '__main__':
    main()