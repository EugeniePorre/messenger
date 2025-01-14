from model import User
from model import Channel
from model import Message

class Server :
    def __init__(self, users:list[User], channels:list[Channel], messages:list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages
        self.server = self
    def get_users(self)->list[User]:
        pass
    def server_to_dico(self)->dict:
        print('ERROR')
        return 'ERROR'
    @classmethod
    def dico_to_server(cls,server:dict)->'Server':
        print('ERROR')
        return 'ERROR'
