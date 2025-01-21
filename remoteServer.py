import requests

from model import User
from model import Channel
from model import Message
from server import Server
from client import Client

class RemoteServer(Server) :
    def __init__(self, url:str):
        self.url = url
        self.server = self

    def load(self):
        pass

    def get_users(self)->list[User]:
        response = requests.get('https://groupe5-python-mines.fr/users')
        Users = response.json()
        return [User.dico_to_user(user) for user in Users]
    
    # def get_channels(self)->list[Channel]:
    #     response = requests.get('https://groupe5-python-mines.fr/channels')
    #     Channels = response.json()
    #     for channel in Channels :
    #         #
    #     return [Channel.dico_to_channel(channel) for channel in Channels]
    
    def create_user(self,new_user:dict):
        requests.post('https://groupe5-python-mines.fr/users/create',json = new_user)
        

        