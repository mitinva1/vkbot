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

def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='mitinva1',
                                 password='ruuns27089',
                                 db='answerdb',
                                 charset='utf8mb4',
                                 cursorclass=mymysql.cursors.DictCursor)
    return connection

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
#mkskey cb1b116bf5f824747cf3d8356da7c1605f511c92193dde4939a31330f74e1dddee3f1353fb4098ee73fe9
#370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8
#loftkey cbfd5ce214721b092276ed6c946321436f94ced4c96ceb27edd5bc3d7f13c82eb4ac0ff44f1bb277d9afe
    vk_session = vk_api.VkApi(token='370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8')
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)

    quest_code = {'0': 'свяжитесь, пожалуйста, с нами напрямую https://vk.com/im?sel=190302556',
                  '1': '',
                  '2': """Изгатавливаем офисные и доьашние перегородки из 
                          Алюминия пвх и стали и закаленного стекла, возможно 
                          изготовление перегородок со встроенными жалюзями. 
                          Подберем оптимальный вариант по желанию заказчика и возможностям помещения.
                          Подробнее по тел. 8 952 102 1221 - Борис""" , 
                  '3': """Воротные и роллетные системы и автоматика.
                          Откатные, секционные и распашные ворота, рольставни.
                          Автоматическое и ручное упраление.
                          Возможность подключения к системе "Умный дом"
                          В работе используем Ворота компании Alutech и 
                          Стальные ворота собственного производства, с различными вариантами отделки.
                          Подробнее по тел. 8 952 102 1221 - Борис
                          https://vk.com/album-45845358_269178605 - фотоальбом""",
                  '4': """Остекление террас и беседок является замечательным вариантом
                          защиты людей от неблагоприятных погодных условий, а также проведения
                          приятного вечера на природе, обеспечивающей ощущение свободы, в тепле 
                          и комфорте.
                          Варианты остекления: Теплый или холодный.
                          Материалы: ПВХ, Алюминий, Сталь, Безрамное Остекление.""",
                  '00': 'Привет'} 
    image_list = {'0': '',
                  '1': 'photo-45845358_457239156',
                  '2': 'photo-45845358_457239068,photo-45845358_457239069,photo-45845358_457239070', 
                  '3': 'video-45845358_456239019,album-45845358_269231297',
                  '4': 'wall-45845358_920',
                  '00': ''} 
    
    paragraph1 = ("""\nвыберете пункт:\n0 - связаться с нами
                  1 - общая информация
                  2 - loft перегородки
                  3 - автоматика и автоматические и воротные системы
                  4 - остекление (ПВХ и Алюминий)\n\n\n""")
    for event in longpoll.listen():
        z = ['привет', 'Привет', 'здаров', 'Здаров', 'Здаров', 'Здравс', 'здравс', 'добрый', 'Добрый']
        z2 = ['0','1','2','3','4']
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text in z2 or event.text in z:
                print('id{}: "{}"'.format(event.user_id, event.text, end=' '))

                attachments = []
                if event.text[:6] in z:
                    event.text = '00'#переводит в словарь для приветствия
                vk.messages.send(
                user_id=event.user_id,
                attachment=image_list[str(event.text)],
                random_id=get_random_id(),
                message= paragraph1 + quest_code[str(event.text)],
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
                vk.messages.send(
                user_id=boris,
                #attachment=','.join(attachments),
                random_id=get_random_id(),
                message='Кто-то, что-то написал'
                )
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
