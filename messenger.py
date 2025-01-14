from argparse import ArgumentParser

from server import Server
from client import Client
from localServer import LocalServer
from remoteServer import RemoteServer

argument_parser = ArgumentParser()
argument_parser.add_argument('-f','--file')
argument_parser.add_argument('-u','--url')
arguments = argument_parser.parse_args()
server : Server
if arguments.file is not None :
    server = LocalServer(arguments.file)
elif arguments.url is not None :
    server = RemoteServer(arguments.url)
else :
    print('error : -f or -u should be set, try again')
    exit(-1)

file_name = 'server.json'

# class Remoteserver :
#     def __init__(self,url:str):
#         self.url = url
#     def getserver(self):

server.load()
client = Client(server)
client.messenger()