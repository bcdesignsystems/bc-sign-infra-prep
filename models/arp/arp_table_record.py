"""arp_table_record.py"""
class ArpTableRecord:
    """
    Ceci est un modèle en Python représentant l'enregistrement d'une association entre
    une address IP et une address MAC ( Media Access Control )
    """
    def __init__(self, ipv4_address, mac_address):
        self.ipv4_address = ipv4_address
        self.mac_address = mac_address
