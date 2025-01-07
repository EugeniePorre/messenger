class User :
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    def __repr__(self)->str:
        return f'User(id={self.id},name={self.name})'
    def user_to_dico(self)->dict:
        return {'id':self.id,'name':self.name}
    @classmethod
    def dico_to_user(cls,user:dict)->'User':
        return cls(user['id'],user['name'])

class Channel :
    def __init__(self, id:int, name:str, member_ids:list):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self)->str:
        return f'Channel(id={self.id},name={self.name},member_ids={self.member_ids})'
    def channel_to_dico(self)->dict:
        return {'id':self.id,'name':self.name,'member_ids':self.member_ids}
    @classmethod
    def dico_to_channel(cls,channel:dict)->'Channel':
        return cls(channel['id'],channel['name'],channel['member_ids'])

class Message :
    def __init__(self, id:int, reception_date, sender_id:int, channel:int, content:str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    def __repr__(self)->str:
        return f'User(id={self.id},reception_date={self.reception_date},sender_id={self.sender_id},channel={self.channel},content={self.content})'
    def message_to_dico(self)->dict:
        return {'id':self.id,'reception_date':self.reception_date,'sender_id':self.sender_id,'channel':self.channel,'content':self.content}
    @classmethod
    def dico_to_message(cls,message:dict)->'Message':
        return cls(message['id'],message['reception_date'],message['sender_id'],message['channel'],message['content'])
