import requests

from model import User
from model import Channel
from model import Message
from server import Server

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
    
    def create_user(self):
        pass