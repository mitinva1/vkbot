# -*- coding: utf-8 -*-
import datetime
import requests

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def main():
    session = requests.Session()

    # Авторизация пользователя:
    login, password = '+79304017447', 'runs47089'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)



    # Авторизация группы (для групп рекомендуется использовать VkBotLongPoll):
    # при передаче token вызывать vk_session.auth не нужно

    vk_session = vk_api.VkApi(token='cb1b116bf5f824747cf3d8356da7c1605f511c92193dde4939a31330f74e1dddee3f1353fb4098ee73fe9')
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        """if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text == 'Мосвремя':
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            vk.messages.send(
                user_id=event.user_id,
                #attachment=','.join(attachments),
                random_id=get_random_id(),
                message='fdsgdsgsdfs'
            )"""
        z = ['привет', 'Привет', 'здаров', 'Здаров', 'Здаров', 'Здравс', 'здравс', 'добрый', 'Добрый']
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text[:6] in z:
                vk.messages.send(
                user_id=event.user_id,
                #attachment=','.join(attachments),
                random_id=get_random_id(),
                message='Здравствуйте, бот еще не настроен, свяжитесь, пожалуйста, с нами напрямую https://vk.com/yaitolkoya2013'
            )
                continue
            print('id{}: "{}"'.format(event.user_id, event.type), end=' ')

            response = session.get(
                'http://api.duckduckgo.com/',
                params={
                    'q': event.text,
                    'format': 'json'
                }
            ).json()

            text = response.get('AbstractText')
            image_url = response.get('Image')

            if not text:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='No results'
                )
                print('no results')
                continue

            attachments = []

            if image_url:
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]

                attachments.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )

            vk.messages.send(
                user_id=event.user_id,
                attachment=','.join(attachments),
                random_id=get_random_id(),
                message=text
            )
            print('ok')


if __name__ == '__main__':
    main()
