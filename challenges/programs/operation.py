import socket
import math
import re
import time

class CustomSocketConnection:
    """Représentation d'une connexion socket"""
    def __init__(self,host, port):
        self.address = (host or '',port)
        response = ""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect(self.address)

            data = s.recv(1024)

            digits = re.findall(pattern=r"\d+", string=data.decode("utf-8"))
            print(digits)
            operation_result = round(math.sqrt(float(digits[1])) * float(digits[2]), 2)

            result_bytes = str(f"{operation_result}\n").encode()

            s.sendall(result_bytes)

            response = s.recv(100).decode()



        print(response)







boris_socket = CustomSocketConnection("challenge01.root-me.org",52002)
