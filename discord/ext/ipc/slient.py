from .client import Client
from .server import Server

class Slient(Client, Server):
    def __init__(*args, **kwargs):
        Client.__init__(self, *args, **kwargs)
        Server.__init__(self, *args, **kwargs)
