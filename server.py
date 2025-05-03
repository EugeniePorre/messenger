from model import User
from model import Channel
from model import Message

class Server :
    # Pas besoin de déclarer __init__ et __repr__. Vous n'avez besoin
    # de déclarer que les fonctions qui sont appelées explicitement
    # sur des Server

    def get_users(self)-> list[User]:
        # Nous n'avons pas vu les exceptions en cours,
        # mais elles permettent de remonter des erreurs d'exécutions.
        # Ici ce code n'est pas censé être atteint, car la fonction
        # sera toujours appelée sur une sous-classe qui la redéfinira.
        # Si on oublie de la redéfinir, l'erreur sera assez explicite
        # (Not implemented)
        raise NotImplementedError()

    def create_user(self, user_name: str) -> None:
        raise NotImplementedError()

    def get_channels(self) -> list[Channel]:
        raise NotImplementedError()

    def server_to_dico(self)->dict:
        pass

    @classmethod
    def dico_to_server(cls,server:dict)->'Server':
        pass