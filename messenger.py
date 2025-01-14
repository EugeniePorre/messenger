from datetime import datetime
import json
# ajout ligne parser
import argparse
parser=argparse.ArgumentParser(description="mise en entrée de paramètres json")
parser.add_argument("--server", "-s", help="donne le chemin d'accès vers le fichier json")
pars=parser.parse_args()
nom_fichier_json=parser.server

import json

file_name = 'server.json'

class Remoteserver :
    def __init__(self,url:str):
        self.url = url
    def getserver(self):

#Client.messenger()

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

# def open_server(file_name):
#     with open(file_name) as json.file :
#         return Server.dico_to_server(json.load(json.file))

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