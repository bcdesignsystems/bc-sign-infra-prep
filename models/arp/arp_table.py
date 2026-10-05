"""arp_table.py"""
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
