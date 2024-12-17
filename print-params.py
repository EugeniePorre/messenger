import sys

print(sys.argv)

commit_message = ''
# On veut mettre "mon message de commit" dans commit_message

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s','--server')
parser.add_argument('-u','--url')

args =  parser.parse_args()

print('Le chemin du fichier est :',args.server)
commit_message = args.server