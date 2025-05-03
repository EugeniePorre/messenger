import json

from model import User
from model import Channel
from server import Server

class Client :
    def __init__(self, server:Server):
        self.server = server

    # Il vaut mieux déléguer cette fonction aux Server,
    # car l'implémentation sera différente dans LocalServer
    # et RemoteServer.
    # Dans LocalServer il vous faudra parcourir _users,
    # et dans RemoteServer un `requests.get` suffira
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
 
    # Idem
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
        
    def leave(self) -> None:
        print('Bye!')
        return None
    
    def see_users(self) -> None:
        # Il vaut mieux éviter les noms de variables d'une seule
        # lettre, même si le sens est évident pour vous.
        for u in self.server.get_users():
            print(u.id,".",u.name)

    def see_channels(self) -> None:
        for c in self.server.get_channels():
            print(c.id,".",c.name)
            print('    Users:')
            for id in c.member_ids:
                print('    -', self.id_to_name(id))
        print("Would you like to see some channel messages ?\nYes/No")
        choix = input('Select an option: ')
        if choix == 'Yes':
            group = input('Enter channel id: ')
            # Par convention, les noms en majuscules identifient
            # des constantes (dont la valeur est fixée à l'écriture du code)
            channels = [c.id for c in self.server.get_channels()]
            if int(group) not in channels:
                print('Unknown option:', group)
            # Vous pouvez déléguer cette logique aux `Server`,
            # en implémentant une fonction `Server.get_channel_messages`.
            # Pour le RemoteServer, un `requests.get` suffira.
            M = [m for m in self.server.messages if m.channel == int(group)]
            if len(M) == 0 :
                print("This channel don't have messages")
            else :
                for m in M:
                    print('************************************')
                    print("Message id :",m.id)
                    print("Message sent by",self.id_to_name(m.sender_id),"at",m.reception_date,":")
                    print(m.content)
                    print('************************************')
        elif choix == 'No':
            self.messenger()
        else :
            print('Unknown option:', choix)

    def add_users(self) -> None:
        print("Who would you like to add ?")
        new_users = input('Enter names separated by commas: ')
        L = new_users.split(',')
        self.add_users_from_list(L)

    def add_users_from_list(self,new_users: 'list[str]') -> None:
        cleaned_users = [nu.strip() for nu in new_users]
        # La logique de gestion de l'`id` est du ressort du serveur
        for user_name in cleaned_users:
            self.server.create_user(user_name)
        # `self.save` n'a pas de sens pour RemoteServer. Il ne devrait donc
        # être appelé que depuis LocalServer.
        self.save()
        print('User(s) added !')
        self.see_users()

    def add_channel(self) -> None:
        print("Which channel would you like to add ?")
        name = input('Enter channel name: ').strip()
        users = [u.strip() for u in input("Enter channel users's names -separated by commas:").split(',')]
        L = []
        for u in users :
            if u not in [v.name for v in self.server.get_users()]:
                L.append(u)
        self.add_users_from_list(L)
        Lusers = [self.name_to_id(name) for name in users]
        # Il vaut mieux passer par des fonctions `add_channel` dans les classes
        # `LocalServer` et `RemoteServer`.
        # Ca facilitera la maintenance du code : ici `channels` n'existe
        # plus dans `LocalServer`, et n'a jamais existé dans `RemoteServer`
        channel_id = max([channel.id for channel in self.server.channels]) + 1
        new_channel = Channel.dico_to_channel({'id': channel_id, 'name': name, 'member_ids': Lusers})
        self.server.channels.append(new_channel)
        self.save()
        self.see_channels()

    # Cette fonction devrait être dans LocalServer, car elle n'a
    # pas de sens pour RemoteServer
    def save(self) -> None:
        with open('server.json','w',encoding = 'utf8') as file :
            json.dump(Server.server_to_dico(self.server),file)

    def messenger(self):
        #server = open_server(file_name)
        print(self.server.get_users())
        print('=== Messenger ===')
        # Vous pouvez aussi faire un print par ligne.
        # Le résultat sera le même, mais vous gagnerez en lisibilité.
        print('x. Leave\nA. See users\nB. See channels\nC. Add users\nD. Add channel')
        choice = input('Select an option: ')
        if choice == 'x':
            # La façon canonique d'appeler une méthode d'instance
            # est `self.leave`. Cet appel va automatiquement
            # envoyer `self` en 1er paramètre de la fonction appelée.
            self.leave()
        elif choice == 'A':
            self.see_users()
        elif choice == 'B':
            self.see_channels()
        elif choice == 'C':
            self.add_users()
        elif choice == 'D':
            self.add_channel()
        else:
            print('Unknown option:', choice)