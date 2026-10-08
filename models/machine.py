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
        mac_address=None,
        if_type="switchport"
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

    def update(self, key, val, action="append"):
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


class Vlan:
    """
    Modèle de Virtual Local Area Network 
    """
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Switch(Machine):
    """Modèle représentant le Switch"""
    def __init__(self,
        hostname,
        fasthernet_interfaces_count: int,
        gigabit_ethernet_interfaces_count: int,
        nvram: str,
        if_type: str = "switchport"
    ):

        """
        Quand une classe hérite d'une autre en l'occurrence la classe Switch hérite de Machine 
        On doit mettre l'instruction d'appel au constructeur de la classe parent ( ici: Machine ) en PREMIER
        """
        super().__init__(hostname=hostname)

        self.nvram = nvram
        self.hostname = hostname
        self.fasthernet_interfaces_count = fasthernet_interfaces_count
        self.gigabit_ethernet_interfaces_count = gigabit_ethernet_interfaces_count

        for i in range(self.fasthernet_interfaces_count):
            self.interfaces.append(Interface(name=f"FastEthernet0/{i + 1}", flags=["DOWN"], if_type=if_type))


class Router(Machine):
    """
    Modèle représentant le routeur
    """
    def __init__(
        self,
        hostname,
        gigabit_ethernet_interfaces_count: int,
        nvram: str
    ):
        super().__init__(hostname=hostname)

        self.nvram = nvram
        self.gigabit_ethernet_interfaces_count = gigabit_ethernet_interfaces_count

        """
        mise en place automatique des interfaces physiques (ex: GigabitEthernet0/0/0, 0/0/1...)
        """
        for i in range(self.gigabit_ethernet_interfaces_count):
            self.interfaces.append(Interface(name=f"GigabitEthernet0/0/{i}", flags=["DOWN"]))

    def route_packet(self, destination_ip):
        """
        Simule le routage d'un paquet vers une IP de destination
        """
         # On parcourt toutes les interfaces du routeur, une par une
        for interface in self.interfaces:

             # On vérifie si cette interface a une adresse IP configurée (différente de None)
            if interface.ipv4_address is not None:

                 # Si oui, on affiche un message disant par quelle interface le paquet "sort"
                print(f"Packet to {destination_ip} routed via {interface.name}")

                 # On arrête la méthode ici et on renvoie l'interface trouvée
                return interface


        # Si on arrive ici, c'est qu'aucune interface n'avait d'IP configurée
        print("No route available")
        return None
