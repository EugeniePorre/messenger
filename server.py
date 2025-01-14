from model import User
from model import Channel
from model import Message

class Server :
    def __init__(self, users:list[User], channels:list[Channel], messages:list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages
    def server_to_dico(self)->dict:
        users = [User.user_to_dico(user) for user in self.users]
        channels = [Channel.channel_to_dico(channel) for channel in self.channels]
        messages = [Message.message_to_dico(message) for message in self.messages]
        return {'users': users,'channels':channels,'messages':messages}
    @classmethod
    def dico_to_server(cls,server:dict)->'Server':
        users = [User.dico_to_user(user) for user in server['users']]
        channels = [Channel.dico_to_channel(channel) for channel in server['channels']]
        messages = [Message.dico_to_message(message) for message in server['messages']]
        return cls(users,channels,messages)
