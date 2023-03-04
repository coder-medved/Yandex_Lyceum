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
    group_id = 123456789

    # ID альбома
    album_id = 987654321

    # Получение ссылки на сервер для загрузки фотографий
    upload_url = vk_session.method('photos.getUploadServer', {'album_id': album_id, 'group_id': group_id})['upload_url']

    # Загрузка фотографий
    photos = []
    img_dir = 'static/img'  # путь к папке с фотографиями
    for file_name in os.listdir(img_dir):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            with open(os.path.join(img_dir, file_name), 'rb') as file:
                photo = upload.photo(upload_url, photos=file)[0]
            photos.append(photo)

    # Сохранение загруженных фотографий в альбоме
    vk_session.method('photos.save', {'album_id': album_id, 'group_id': group_id, 'photos': str(photos)})


if __name__ == '__main__':
    main()