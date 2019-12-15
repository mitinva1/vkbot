import vk_api
import time
import requests
import importlib

session = requests.Session()
login, password = '+79304017447', 'runs47089'

vk_session = vk_api.VkApi(login, token='370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8')
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
    return

#vk = vk_api.VkApi('+79304017447', 'runs47089')
#vk = vk_api.VkApi('+79304017447', 'runs47089', token = '370c0e1fa63820c1666f6b70943ff2e6ac24028651cf04b047c9813f604c60e962406153d4c7faaf17ea8')
#vk.auth()
#vk = vk_session.get_api()
#def write_msg(user_id, s):
 #   vk.method('messages.send', {'user_id':user_id,'message':s})
#print('import is end')
z=1


#vk = vk_session.get_api()
#print(vk.wall.post(message='My ch- bot'))
