"""interface.py"""
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
