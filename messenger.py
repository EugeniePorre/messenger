from datetime import datetime
import json

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
        return json.load(json.file)

class User :
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name


class Channel :
    def __init__(self, id:int, name:str, member_ids:list):
        self.id = id
        self.name = name
        self.member_ids = member_ids

class Message :
    def __init__(self, id:int, reception_date, sender_id:int, channel:int, content:str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content

class Server :
    def __init__(self, users:list[User], channels:list[Channel], messages:list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages

def dico_to_user(user)->User:
    return User(user['id'],user['name'])

def dico_to_channel(channel)->Channel:
    return Channel(channel['id'],channel['name'],channel['member_ids'])

def dico_to_message(message)->Message:
    return Message(message['id'],message['reception_date'],message['sender_id'],message['channel'],message['content'])

def id_to_name(id,server):
    L = []
    for u in server['users']:
        if u['id'] == id:
            L.append(u['name'])
    if len(L) == 1:
        return L[0]
    else :
        print("ERREUR : Plusieurs utilisateurs correspondent à l'identifiant",id,"demandé")
        return L

def name_to_id(name,server):
    L = []
    for u in server['users']:
        if u['name'] == name :
            L.append(u['id'])
    if len(L) == 1 :
        return L[0]
    else :
        print("ERREUR : Plusieurs id correspondent au nom",name,'demandé')
        return L

def leave(server):
    print('Bye!')
    return None

def see_users(server):
    for u in server['users']:
        print(u['id'],".",u['name'])

def see_channels(server):
    for c in server['channels']:
        print(c['id'],".",c['name'])
        print('    Users:')
        for id in c['member_ids']:
            print('    -',id_to_name(id,server))
    print("Would you like to see some channel messages ?\nYes/No")
    choix = input('Select an option: ')
    if choix == 'Yes':
        group = input('Enter channel id: ')
        CHANNELS = [c['id'] for c in server['channels']]
        if int(group) not in CHANNELS :
            print('Unknown option:', group)
        M = [m for m in server['messages'] if m['channel'] == int(group)]
        for m in M:
            print('************************************')
            print("Message id :",m['id'])
            print("Message sent by",id_to_name(m['sender_id'],server),"at",m['reception_date'],":")
            print(m['content'])
            print('************************************')
    elif choix == 'No':
        messenger(file_name)
    else :
        print('Unknown option:', choix)

def add_users(server):
    print("Who would you like to add ?")
    new_users = input('Enter names separated by commas: ')
    L = new_users.split(',')
    add_users_from_list(L,server)

def add_users_from_list(new_users,server):
    cleaned_users = [nu.strip() for nu in new_users]
    first_unused_id = max(u['id'] for u in server['users']) + 1
    for i, new_name in enumerate(cleaned_users):
        new_user = {'id': first_unused_id + i, 'name': new_name}
        server['users'].append(new_user)
    save(server)
    print('User(s) added !')
    see_users(server)

def add_channel(server):
    print("Which channel would you like to add ?")
    name = input('Enter channel name: ').strip()
    users = [u.strip() for u in input("Enter channel users's names -separated by commas:").split(',')]
    n = len(users)
    L = []
    for u in users :
        if u not in [v['name'] for v in server['users']] :
            L.append(u)
    add_users_from_list(L,server)
    Lusers = [name_to_id(name,server) for name in users]
    channel_id = max([channel['id'] for channel in server['channels']]) + 1
    new_channel = {'id': channel_id, 'name': name, 'member_ids': Lusers}
    server['channels'].append(new_channel)
    save(server)
    see_channels(server)

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

def save(server):
    with open('server.json','w') as file :
        json.dump(server,file)

def messenger(file_name):
    server = open_server(file_name)
    print('=== Messenger ===')
    print('x. Leave\nA. See users\nB. See channels\nC. Add users\nD. Add channel')
    choice = input('Select an option: ')
    if choice == 'x':
        leave(server)
    elif choice == 'A':
        see_users(server)
    elif choice == 'B':
        see_channels(server)
    elif choice == 'C':
        add_users(server)
    elif choice == 'D':
        add_channel(server)
    else:
        print('Unknown option:', choice)

messenger(file_name)
