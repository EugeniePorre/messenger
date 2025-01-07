from datetime import datetime
import json
# ajout ligne parser 

import argparse
parser=argparse.ArgumentParser(description="mise en entrée de paramètres json")
parser.add_argument("--server", "-s", help="donne le chemin d'accès vers le fichier json")
pars=parser.parse_args()
nom_fichier_json=parser.server

import json
#ajout commentaire pour test christelle

#### PB : le JSON se supprime tout seul par moments ????

# server = {
#     'users': [
#         {'id': 1, 'name': 'Alice'},
#         {'id': 2, 'name': 'Bob'}
#     ],
#     'channels': [
#         {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
#     ],
#     'messages': [
#         {
#             'id': 1,
#             'reception_date': datetime.now(),
#             'sender_id': 1,
#             'channel': 1,
#             'content': 'Hi'
#         }
#     ]
# }

file_name = 'server.json'

def open_server(file_name):
    with open(file_name) as json.file :
        return Server.dico_to_server(json.load(json.file))

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

class Client :
    def __init__(self, server:Server, choice:str):
        self.server = server
    
    def id_to_name(self,id):
        L = []
        for u in self.server.users:
            if u.id == id:
                L.append(u.name)
        if len(L) == 1:
            return L[0]
        else :
            print("ERREUR : Plusieurs utilisateurs correspondent à l'identifiant",id,"demandé")
            return L
        
    def name_to_id(self,name):
        L = []
        for u in self.server.users:
            if u.name == name :
                L.append(u.id)
        if len(L) == 1 :
            return L[0]
        else :
            print("ERREUR : Plusieurs id correspondent au nom",name,'demandé')
            return L
        
    def leave(self):
        print('Bye!')
        return None
    
    def see_users(self):
        for u in self.server.users:
            print(u.id,".",u.name)

    def see_channels(self):
        for c in self.server.channels:
            print(c.id,".",c.name)
            print('    Users:')
            for id in c.member_ids:
                print('    -',Client.id_to_name(self,id))
        print("Would you like to see some channel messages ?\nYes/No")
        choix = input('Select an option: ')
        if choix == 'Yes':
            group = input('Enter channel id: ')
            CHANNELS = [c.id for c in self.server.channels]
            if int(group) not in CHANNELS :
                print('Unknown option:', group)
            M = [m for m in self.server.messages if m.channel == int(group)]
            if len(M) == 0 :
                print("This channel don't have messages")
            else :
                for m in M:
                    print('************************************')
                    print("Message id :",m.id)
                    print("Message sent by",Client.id_to_name(self.server,m.sender_id),"at",m.reception_date,":")
                    print(m.content)
                    print('************************************')
        elif choix == 'No':
            Client.messenger(file_name)
        else :
            print('Unknown option:', choix)

    def add_users(self):
        print("Who would you like to add ?")
        new_users = input('Enter names separated by commas: ')
        L = new_users.split(',')
        Client.add_users_from_list(self,L)

    def add_users_from_list(self,new_users):
        cleaned_users = [nu.strip() for nu in new_users]
        first_unused_id = max(u.id for u in self.server.users) + 1
        for i, new_name in enumerate(cleaned_users):
            new_user = User.dico_to_user({'id': first_unused_id + i, 'name': new_name})
            self.server.users.append(new_user)
        Client.save(self)
        print('User(s) added !')
        Client.see_users(self)

    def add_channel(self):
        print("Which channel would you like to add ?")
        name = input('Enter channel name: ').strip()
        users = [u.strip() for u in input("Enter channel users's names -separated by commas:").split(',')]
        n = len(users)
        L = []
        for u in users :
            if u not in [v.name for v in self.server.users] :
                L.append(u)
        Client.add_users_from_list(self,L)
        Lusers = [Client.name_to_id(self,name) for name in users]
        channel_id = max([channel.id for channel in self.server.channels]) + 1
        new_channel = Channel.dico_to_channel({'id': channel_id, 'name': name, 'member_ids': Lusers})
        self.server.channels.append(new_channel)
        Client.save(self)
        Client.see_channels(self)

    def save(self):
        with open('server.json','w') as file :
            json.dump(Server.server_to_dico(self.server),file)

    def messenger(self):
        #server = open_server(file_name)
        print(self.server.users)
        print('=== Messenger ===')
        print('x. Leave\nA. See users\nB. See channels\nC. Add users\nD. Add channel')
        choice = input('Select an option: ')
        if choice == 'x':
            Client.leave(self)
        elif choice == 'A':
            Client.see_users(self)
        elif choice == 'B':
            Client.see_channels(self)
        elif choice == 'C':
            Client.add_users(self)
        elif choice == 'D':
            Client.add_channel(self)
        else:
            print('Unknown option:', choice)

#Client.messenger()


### 
# Il faut aussi supprimer les messages du user
# Il faut aussi supprimer le user des groupes
###
# def delete_users():
#     N = [n.strip() for n in input('Enter users you wish to remove from the server -separated by commas:').split(',')]
#     for n in N:
#         if n not in [u['name'] for u in server['users']]:
#             print("ERREUR : ",n,"is not an user")
#         else :
