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

fichier = open('server.json')
server = json.load(fichier)

def id_to_name(id):
    L = []
    for u in server['users']:
        if u['id'] == id:
            L.append(u['name'])
    if len(L) == 1:
        return L[0]
    else :
        print("ERREUR : Plusieurs utilisateurs correspondent à l'identifiant",id,"demandé")
        return L

def name_to_id(name):
    L = []
    for u in server['users']:
        if u['name'] == name :
            L.append(u['id'])
    if len(L) == 1 :
        return L[0]
    else :
        print("ERREUR : Plusieurs id correspondent au nom",name,'demandé')
        return L

def leave():
    print('Bye!')
    return None

def see_users():
    for u in server['users']:
        print(u['id'],".",u['name'])

def see_channels():
    for c in server['channels']:
        print(c['id'],".",c['name'])
        print('    Users:')
        for id in c['member_ids']:
            print('    -',id_to_name(id))
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
            print("Message sent by",id_to_name(m['sender_id']),"at",m['reception_date'],":")
            print(m['content'])
            print('************************************')
    elif choix == 'No':
        messenger()
    else :
        print('Unknown option:', choix)

def add_users():
    print("Who would you like to add ?")
    new_users = input('Enter names separated by commas: ')
    L = new_users.split(',')
    add_users_from_list(L)

def add_users_from_list(new_users):
    cleaned_users = [nu.strip() for nu in new_users]
    first_unused_id = max(u['id'] for u in server['users']) + 1
    for i, new_name in enumerate(cleaned_users):
        new_user = {'id': first_unused_id + i, 'name': new_name}
        server['users'].append(new_user)
    save()
    print('User(s) added !')
    see_users()

def add_channel():
    print("Which channel would you like to add ?")
    name = input('Enter channel name: ').strip()
    users = [u.strip() for u in input("Enter channel users's names -separated by commas:").split(',')]
    n = len(users)
    L = []
    for u in users :
        if u not in [v['name'] for v in server['users']] :
            L.append(u)
    add_users_from_list(L)
    Lusers = [name_to_id(name) for name in users]
    channel_id = max([channel['id'] for channel in server['channels']]) + 1
    new_channel = {'id': channel_id, 'name': name, 'member_ids': Lusers}
    server['channels'].append(new_channel)
    save()
    see_channels()


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




def save():
    with open('server.json','w') as file :
        json.dump(server,file)

def messenger():
    print('=== Messenger ===')
    print('x. Leave\nA. See users\nB. See channels\nC. Add users\nD. Add channel\nE. Delete users')
    choice = input('Select an option: ')
    if choice == 'x':
        leave()
    elif choice == 'A':
        see_users()
    elif choice == 'B':
        see_channels()
    elif choice == 'C':
        add_users()
    elif choice == 'D':
        add_channel()
    elif choice == 'E':
        delete_users()
    else:
        print('Unknown option:', choice)

messenger()
