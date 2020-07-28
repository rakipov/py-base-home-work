import requests
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

TOKEN = config['vk_api']['access_token']


# Решение задачи по поиску общих друзей в VK

class User:

    def __init__(self, user_id, token=str):
        self.user_id = user_id
        self.token = token
        self.api_version = config['vk_api']['api_version']
        self.mutual_method_url = config['vk_api']['mutual_method_url']

    def __and__(self, other_user):
        params = {'access_token': self.token,
                  'v': self.api_version,
                  'source_uid': self.user_id,
                  'target_uid': other_user.user_id
                  }

        mutual_user_list = []

        response = requests.get(self.mutual_method_url, params=params)
        profile_list = response.json()

        for user in profile_list['response']:
            mutual_user_list.append(User(user))
        return mutual_user_list

    def print_user_link(self):
        print(f'https://vk.com/id{self.user_id}')


user1 = User(17198266, TOKEN)
user2 = User(85762198, TOKEN)

for user in user1 & user2:
    user.print_user_link()
