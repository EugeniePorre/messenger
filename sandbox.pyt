# import requests
# response = requests.get('https://eleves.mines-paris.eu')
# print(response.status_code, response.text[:300])

from model import User

import requests

response = requests.get('https://groupe5-python-mines.fr/users')
Users = response.json()
print([User.dico_to_user(user) for user in Users])
