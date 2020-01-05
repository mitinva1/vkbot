#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api


def main():
    #""" удаляет все записи со стены вк"""

    login, password = '+79304017447', 'getattr7089'
    vk_session = vk_api.VkApi(login, password)

    vk_session.auth()

    vk = vk_session.get_api()

    posts = vk.wall.get(count=100)['items'] 
    while(posts):                                        
        for post in posts:                 
            print(post['id'])                     
            vk.wall.delete(post_id=post['id'])
        posts = vk.wall.get(count=100)['items']


if __name__ == '__main__':
    main()
