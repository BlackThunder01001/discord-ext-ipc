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
        sending_multicast = 20000,
        receiving_multicast = 20001,
    ):
        Client.__init__(
            self,
            port = receiving_port,
            multicast_port = receiving_multicast,
            host = host,
            secret_key = secret_key)

        Server.__init__(
            self,
            bot = bot,
            port = sending_port,
            multicast_port = sending_multicast,
            host = host,
            secret_key = secret_key
        )
