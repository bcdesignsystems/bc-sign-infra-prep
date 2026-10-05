"""switch.py"""
from ..machine import Machine
from ..interface import Interface
class Switch(Machine):
    """Modèle représentant le Switch"""
    def __init__(self,
        hostname,
        fasthernet_interfaces_count: int,
        gigabit_ethernet_interfaces_count: int,
        nvram:str,
        if_type:str = "switchport"
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
            self.interfaces.append(Interface(name=f"FastEthernet0/{i + 1}",flags=["DOWN"], if_type=if_type))

