import json

from model import User
from model import Channel
from server import Server

class Client :
    def __init__(self, server:Server):
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
        for u in self.server.get_users():
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
            Client.messenger(self)
        else :
            print('Unknown option:', choix)

    def add_users(self):
        print("Who would you like to add ?")
        new_users = input('Enter names separated by commas: ')
        L = new_users.split(',')
        Client.add_users_from_list(self,L)

    def add_users_from_list(self,new_users):
        cleaned_users = [nu.strip() for nu in new_users]
        first_unused_id = max(u.id for u in self.server.get_users()) + 1
        for i, new_name in enumerate(cleaned_users):
            new_user = {'id': first_unused_id + i, 'name': new_name}
            self.server.create_user(new_user)
        Client.save(self)
        print('User(s) added !')
        Client.see_users(self)

    def add_channel(self):
        print("Which channel would you like to add ?")
        name = input('Enter channel name: ').strip()
        users = [u.strip() for u in input("Enter channel users's names -separated by commas:").split(',')]
        L = []
        for u in users :
            if u not in [v.name for v in self.server.users]:
                L.append(u)
        Client.add_users_from_list(self,L)
        Lusers = [Client.name_to_id(self,name) for name in users]
        channel_id = max([channel.id for channel in self.server.channels]) + 1
        new_channel = Channel.dico_to_channel({'id': channel_id, 'name': name, 'member_ids': Lusers})
        self.server.channels.append(new_channel)
        Client.save(self)
        Client.see_channels(self)

    def save(self):
        with open('server.json','w',encoding = 'utf8') as file :
            json.dump(Server.server_to_dico(self.server),file)

    def messenger(self):
        #server = open_server(file_name)
        print(self.server.get_users())
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