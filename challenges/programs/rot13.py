"""rot13.py"""
import re
import codecs
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
    


s1 = MySocket()
s1.connect("challenge01.root-me.org",52021)
s1.my_receive(195)
s1.get_specific_data(pattern=r"[a-zA-Z0-9]{10,}")
s1.decode_specific_data()
s1.my_send()
s1.my_receive(195)