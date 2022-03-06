from .client import Client
from .server import Server

class Slient(Client, Server):
    def __init__(
        self,
        bot,
        host="localhost",
        sending_port = 8654,
        receiving_port = 8653,
        secret_key = None,
    ):
        Client.__init__(
            self,
            port = receiving_port,
            host = host,
            secret_key = secret_key)
            
        Server.__init__(
            self,
            bot = bot,
            port = sending_port,
            host = host,
            secret_key = secret_key
        )
