from models.appliances.switch import Switch


"""
Scénario:
- Création d'un switch
"""
sw1 = Switch(
    hostname="samia-switch",
    fasthernet_interfaces_count=24,
    gigabit_ethernet_interfaces_count=2,
    nvram=None
)
