from datetime import datetime

server = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi'
        }
    ]
}

CHANNELS = [c['id'] for c in server['channels']]
print(CHANNELS)

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

def messenger():
    print('=== Messenger ===')
    print('x. Leave\nA. See users\nB. See channels\nC. Add users')
    choice = input('Select an option: ')
    if choice == 'x':
        leave()
    elif choice == 'A':
        see_users()
    elif choice == 'B':
        see_channels()
    elif choice == 'C':
        print("Who would you like to add ?")
    else:
        print('Unknown option:', choice)

messenger()
