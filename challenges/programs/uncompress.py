"""uncompress.py"""
import re
import codecs
from encodings import base64_codec, zlib_codec
from socket import AF_INET, SOCK_STREAM, socket
class MySocket:
    """Représentation d'un Socket"""
    def __init__(self, s = None):
        if s is None:
            self.s = socket(AF_INET,SOCK_STREAM)
        else:
            self.s = s
        self.server_data = ""
        self.specific_data = ""
        self.decoded_data = ""
    
    def connect(self, host, port):
        """se connecte à la socket serveuse"""
        self.s.connect((host, port))
    
    def my_receive(self, bufer_size=100):
        """reçoit la réponse du serveur"""
        data = self.s.recv(bufer_size)
        self.server_data=data.decode()
        print(self.server_data)


    def get_specific_data(self, pattern):
        """récupère une information spécifique dans data"""
        self.specific_data = re.findall(pattern=pattern, string=self.server_data)[0]
        print(self.specific_data)
    
    def decode_specific_data(self,encoding="rot13"):
        """décoder l'information cachée"""
        if encoding == "rot13":
            self.decoded_data = codecs.decode(self.specific_data, "rot_13")
            self.specific_data = self.decoded_data
        if encoding == "base64":
            binary, _= base64_codec.base64_decode(self.specific_data.encode())
            self.decoded_data = binary
            self.specific_data = self.decoded_data
        if encoding == "zlib":
            binary, _ = zlib_codec.zlib_decode(self.specific_data)
            self.decoded_data = binary
            self.specific_data = self.decoded_data
    

    def solve_loop(self, pattern=r"'([a-zA-Z0-9+/=]+)'"):
        """chaque tour : nouvelle chaîne -> base64 -> zlib -> réponse, jusqu'au flag"""
        while True:
            self.my_receive(1024)
            if not self.server_data or "flag" in self.server_data.lower():
                break
            matches = re.findall(pattern=pattern, string=self.server_data)
            if not matches:
                continue
            self.specific_data = matches[-1]
            self.decode_specific_data("base64")
            self.decode_specific_data("zlib")
            self.my_send()

    def my_send(self):
        """envoie vers le serveur"""
        result = ""
        if isinstance(self.decoded_data, str):
            result = (f"{self.decoded_data}\n").encode()
            print("result {0}", result)
            self.s.sendall(result)
        else:
            result = (self.decoded_data.decode("utf-8") + "\n").encode()
            print("result {0}", result)
            self.s.sendall(result)
        return "\033[32;1mdata sent✅\033[m"
    

s2 = MySocket()
s2.connect("challenge01.root-me.org", 52022)
s2.solve_loop()
