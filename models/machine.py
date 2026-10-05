""" machine.py """

class Interface:
    """
    Ceci est un modèle en Python représentant une interface
    """
    def __init__(self,name,state="down",ipv4_address=None, netmask=None):
        self.name = name
        self.state = state
        self.ipv4_address = ipv4_address
        self.netmask = netmask



class ArpTableRecord:
    """
    Ceci est un modèle en Python représentant l'enregistrement d'une association entre
    une address IP et une address MAC ( Media Access Control )
    """
    def __init__(self, ipv4_address, mac_address):
        self.ipv4_address = ipv4_address
        self.mac_address = mac_address


class ArpTable:
    """
    Ceci est un modèle en Python représentant une table ARP
    """
    def __init__(self):
        self.records = []

    def add_record(self, record):
        """
        Méthode permettant d'ajouter des enregistrements
        """
        self.records.append(record)



class Machine:
    """
    Ceci est un modèle en Python représentant une machine
    """
    def __init__(self,hostname):
        self.hostname = hostname
        self.interfaces = [
            Interface(
                name="lo0",
                state="up",
                ipv4_address="127.0.0.1",
                netmask="255.255.255.255"
            )
        ]
        self.arp_table = ArpTable()

    def add_interface(self, interface):
        """
        méthode d'ajout d'une interface à la machine
        """
        self.interfaces.append(interface)