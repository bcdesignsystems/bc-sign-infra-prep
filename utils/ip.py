# nous voulons 14 addresses ipv4 dispos = 16 adresses dispo
# 16 adresses dispo = 14 + 1 adresse broadcast + 1 adresse rzo

def get_hosts_from_cidr(cidr):
    """
    en fonction du cird on peut savoir
    le nombre d'hôtes dispos sur le réseau
    """
    return 2**(32-int(cidr)) - 2

def get_dec_from_bin(binary:str):
    #1 1 1 1 0 0 0 0
    """
    fonction qui permet de trouver la notation déciale d'un octet en binaire
    """
    result = 0
    for k,i in enumerate(binary):
        result += int(i) * 2**(7-k)
    return result