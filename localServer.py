import json

from model import User
from model import Channel
from model import Message
from server import Server

class LocalServer(Server) :
    def __init__(self, file:str):
        self.file = file
        self.server = self
        self._users : list[User] = []
    
    def load(self):
        server = json.load(open(self.file))
        self._users = [User.dico_to_user(user) for user in server['users']]
        self._channels = [Channel.dico_to_channel(channel) for channel in server['channels']]
        self._messages = [Message.dico_to_message(message) for message in server['messages']]
    
    def get_users(self):
        return self._users
        
    def server_to_dico(self)->dict:
        users = [User.user_to_dico(user) for user in self.users]
        channels = [Channel.channel_to_dico(channel) for channel in self.channels]
        messages = [Message.message_to_dico(message) for message in self.messages]
        return {'users': users,'channels':channels,'messages':messages}
    
    def dico_to_server(cls,server:dict)->'LocalServer':
        users = [User.dico_to_user(user) for user in server['users']]
        channels = [Channel.dico_to_channel(channel) for channel in server['channels']]
        messages = [Message.dico_to_message(message) for message in server['messages']]
        return cls(users,channels,messages)

