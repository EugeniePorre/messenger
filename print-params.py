import sys

print(sys.argv)

commit_message = ''
# On veut mettre "mon message de commit" dans commit_message

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m')

args =  parser.parse_args()

print('ArgumentParser a parsé le paramètre suivant:',args.m)
commit_message = args.m