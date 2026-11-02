# Topologie réseau (Packet Tracer + Python)

Configurations Cisco d'une topologie d'entreprise (inter-VLAN, DHCP, FTP avec ACL,
Wi-Fi, redondance HSRP/STP, DMZ avec pare-feu ASA 5505) et modèles Python
des équipements réseau.

## Équipements

| Équipement | Type | Rôle |
|---|---|---|
| CORE | Switch L3 3650 | Passerelle HSRP active, root bridge STP |
| CORE-2 | Switch L3 3650 | Passerelle de secours, root secondaire |
| Switch0 / Switch1 | Switch L2 2960 | Accès Marketing / RH + FTP |
| Router0 | Routeur | Liaison vers le pare-feu |
| ASA0 | Pare-feu ASA 5505 | Protège la DMZ |
| Server3 | Serveur web | En DMZ |

## Plan d'adressage

| VLAN | Usage | Réseau | HSRP | CORE | CORE-2 |
|---|---|---|---|---|---|
| 20 | Marketing | 192.168.20.0/28 | .5 | .6 | .7 |
| 21 | RH | 192.168.21.0/28 | .5 | .6 | .7 |
| 30 | Serveurs | 192.168.30.0/28 | .5 | .6 | .7 |
| 40 | Routeur | 192.168.40.0/28 | .5 | .6 | .7 |
| 50 | Wi-Fi | 192.168.50.0/28 | .5 | .6 | .7 |

DMZ : 192.168.41.0/28 (outside) et 192.168.42.0/28 (dmz).

## Arborescence

- `topologies/1/switches/` : configs des switchs (core, access)
- `topologies/1/router/` : configs du routeur
- `topologies/1/firewall/` : config de l'ASA
- `topologies/1/hosts/` : configs des serveurs
- `models/` : classes Python (Machine, Router, Switch, Interface, Vlan, ARP)
- `utils/` : fonctions utilitaires (calcul d'adresses)

## Utilisation

Copier le contenu d'un fichier `.config` dans la console CLI de l'équipement
correspondant dans Packet Tracer.

## Conventions

Commits au format Conventional Commits (feat, fix, docs, refacto...).