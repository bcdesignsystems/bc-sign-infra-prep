""" machine.py """
from .interface import Interface
from .arp.arp_table import ArpTable



class Machine:
    """
    Ceci est un modèle en Python représentant une machine
    """
    
    def __init__(self, hostname):
        self.hostname = hostname
        self.interfaces = [
            Interface(
                name="lo0",
                flags=["UP", "LOOPBACK", "RUNNING", "MULTICAST"],
                ipv4_address="127.0.0.1",
                netmask="255.255.255.255"
            ),
            Interface(
                name="en0",
                flags=["UP", "BROADCAST", "SMART", "RUNNING", "SIMPLEX", "MULTICAST"],
                ipv4_address="192.168.1.80",
                netmask="255.255.255.0"
            )
        ]
        self.arp_table = ArpTable()

    def update_interface(self, name, flags=None, ipv4_address=None, netmask=None, action="append"):
        """
        méthode qui permet de mettre à jour une interface de la machine 
        On passe les informations que l'on souhaite donner à l'interface 
        """
        for i in self.interfaces:
            """
            On itère sur la liste self.interfaces 
            Pour chaque élément de la liste (i) on va vérifier si son attribut name
            correspond à la valeur name passée à la méthode 
            """
            if i.name == name:
                """
                Quand on sait qu'il y a une correspondance alors on sait que c'est cette
                interface que l'on voulait modifier
                """
                if flags is not None:
                    for f in flags:
                        i.update(key="flags", val=f, action=action)
                if ipv4_address is not None:
                    i.update(key="ipv4_address", val=ipv4_address)
                if netmask is not None:
                    i.update(key="netmask", val=netmask)

    def add_interface(self, interface):
        """
        méthode d'ajout d'une interface à la machine
        """
        self.interfaces.append(interface)


