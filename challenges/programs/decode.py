import socket
from encodings import base64_codec
import re

class MySocket:
    """Représentation d'un socket"""
    # Constructeur
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        else:
            self.sock = sock

    def connect(self, host, port):
        """connecte à la socket serveuse"""
        self.sock.connect((host, port))
        data = self.sock.recv(195).decode("utf-8")
        print(data)
        encoded_str = (re.findall(pattern=r"[a-zA-Z0-9=]+", string=data))[-5]
        binary, _ = base64_codec.base64_decode(encoded_str.encode())
        print("binary", binary)
        self.sock.sendall((binary.decode() + "\n").encode())
        response = self.sock.recv(195)
        print(response.decode())
        self.sock.close()



samia_client_socket = MySocket()
samia_client_socket.connect("challenge01.root-me.org",52023)
