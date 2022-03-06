from .client import Client
from .server import Server

class Slient(Client, Server):
    """
    Merges the methods of class:`.Client` & class:`.Server` to allow intercommunication
    between two discord bots. 
    """
    def __init__(
        self,
        bot,
        host="localhost",
        sending_port = 8654,
        receiving_port = 8653,
        secret_key = None,
        sending_multicast = 20000,
        receiving_multicast = 20001,
    ):
        self.client = Client(
            port = receiving_port,
            multicast_port = receiving_multicast,
            host = host,
            secret_key = secret_key)

        self.server = Server(
            bot = bot,
            port = sending_port,
            multicast_port = sending_multicast,
            host = host,
            secret_key = secret_key
        )
        for com in (self.server, self.client):
            for method in dir(com):
                if method.startswith('__') is False:
                    try:
                        setattr(self, method, getattr(com, method))
                    except:
                        ...
