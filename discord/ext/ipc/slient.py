from .client import Client
from .server import Server

class Slient(Client, Server):
    def __init__(self, port=8765, *args, **kwargs):
        Client.__init__(self, port=port, *args, **kwargs)
        Server.__init__(self, port=port+1, *args, **kwargs)
