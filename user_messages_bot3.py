#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import requests
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pymysql.cursors
from vk_api.utils import get_random_id

import functions


def main():
    session = requests.Session()
    # Авторизация пользователя:
    login, password = '+79304017447', 'getattr7089'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
    # Авторизация группы (для групп рекомендуется использовать VkBotLongPoll):
    # при передаче token вызывать vk_session.auth не нужно
#mkskey cb1b116bf5f824747cf3d8356da7c1605f511c92193dde4939a31330f74e1dddee3f1353fb4098ee73fe9
#370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8
#loftkey cbfd5ce214721b092276ed6c946321436f94ced4c96ceb27edd5bc3d7f13c82eb4ac0ff44f1bb277d9afe
    vk_session = vk_api.VkApi(token='370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8')
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)


    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            try:
                answer = functions.answer_db(str(event.text.lower()))
            except:
                answer = '7089'
            try:
                attachments = functions.answer_db('img-'+event.text)
            except:
                attachments = ''
            print(attachments)
            if answer != '7089':
                print('id{}: "{}"'.format(event.user_id, event.text, end=' '))

                vk.messages.send(
                user_id = event.user_id,
                attachment = attachments,
                random_id=get_random_id(),
                message= answer + '\n'+functions.answer_db('ms000'),
                )
                #для оповещения
                dd = 233357783
                boris = 190302556
                # vk.messages.send(
                # user_id=dd,
                # #attachment=','.join(attachments),
                # random_id=get_random_id(),
                # message='Кто-то, что-то написал'
                # )
                # vk.messages.send(
                # user_id=boris,
                # #attachment=','.join(attachments),
                # random_id=get_random_id(),
                # message='Кто-то, что-то написал'
                # )
                #

                
                
            else:    
                print('id{}: "{}"'.format(event.user_id, event.text), end=' ')

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
                        message='Извините, запрос не распознан'
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
                print(','.join(attachments))


if __name__ == '__main__':
    main()
