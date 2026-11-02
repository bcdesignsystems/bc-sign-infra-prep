# models

Modèles Python représentant les équipements réseau.

- `machine.py` : classe de base `Machine` (hostname, interfaces, table ARP)
- `interface.py` : `Interface` (nom, flags, IPv4, masque, MAC)
- `appliances/router.py` : `Router`, hérite de `Machine`
- `appliances/switch.py` : `Switch`, hérite de `Machine`
- `arp/` : `ArpTable` et `ArpTableRecord`
- `security/vlan.py` : `Vlan` (nom, id)