import socket
import math
MSGLEN = 195
class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


boris_socket = MySocket()
boris_socket.connect("challenge01.root-me.org",52002)
formated_str=boris_socket.myreceive().decode("utf-8")
number_one_square_root = math.sqrt(int(formated_str.split(" ")[-5]))
number_two = int(formated_str.split(" ")[-1])
result = number_one_square_root * number_two
final_result = round(float(result),2)
boris_socket.mysend(bin(int(float(result))))
