""" machine.py """

class Interface:
    """
    Ceci est un modèle en Python représentant une interface
    """
    def __init__(self,
        name,
        flags = None,
        ipv4_address=None,
        netmask=None,
        mac_address=None
    ):
        self.name = name

        """
        Si au moment de l'instanciation de la classe Interface 
        rien n'est passé explictement comme valeur au paramètre flags 
        alors flags prendra sa valeur par défault qui est None 

        Or ci-dessous on dit que si flags vaut None alors 
        l'attribut flags de l'instance d'Interface vaudra 
        une liste vide []
        Si on a passé explictement une valeur au paramètre flags 
        au moment de l'appel du constructeur autrement dit 
        au moment de l'instanciation alors 
        l'attribut flags de l'instance d'Interface aura comme valeur 
        la valeur passée
        """
        self.flags = [] if flags is None else flags

        self.ipv4_address = ipv4_address
        self.netmask = netmask
        self.mac_address = mac_address

    def update(self, key, val,action="append"):
        """
        méthode afin de mettre à jour une information de l'interface 
        cela peut être la liste des flags , l'adresse IP ou le masque de sous-réseau
        """
        if key == "flags":
            if action == "append":
                self.flags.append(val)
            else:
                self.flags.remove(val)
        if key == "ipv4_address":
            self.ipv4_address = val 
        if key == "netmask":
            self.netmask = val

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
                flags=["UP", "LOOPBACK", "RUNNING", "MULTICAST"],
                ipv4_address="127.0.0.1",
                netmask="255.255.255.255"
            ),
            Interface(
                name="en0",
                flags=["UP","BROADCAST","SMART","RUNNING","SIMPLEX","MULTICAST"],
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
                        i.update(key="flags", val=f,action=action)
                if ipv4_address is not None:
                    i.update(key="ipv4_address", val=ipv4_address)
                if netmask is not None:
                    i.update(key="netmask",val=netmask)
                

    def add_interface(self, interface):
        """
        méthode d'ajout d'une interface à la machine
        """
        self.interfaces.append(interface)