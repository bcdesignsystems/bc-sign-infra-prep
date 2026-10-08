from ..machine import Machine
from ..interface import Interface

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
        for interface in self.interfaces:
            if interface.ipv4_address is not None:
                print(f"Paquet vers {destination_ip} routé via {interface.name}")
                return interface

        print("Aucune route disponible")
        return None


