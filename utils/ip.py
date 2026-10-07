"""ip.py"""

def get_hosts_from_cidr(cidr):
    """
    En fonction du CIRD on peut savoir 
    le nombre d'hôtes disponibles sur le réseau
    """
    return 2**(32-int(cidr)) - 2

def get_dec_from_bin(binary:str):
    """
    fonction qui permet de trouve la notation décimale 
    d'une octet en binaire
    """
    #puissance|  7  | 6  | 5  | 4  | 3 | 2 | 1 | 0 |
    #valeurs  |  1  | 1  | 1  | 1  | 0 | 0 | 0 | 0 |
    #decimales| 128 | 64 | 32 | 16 | 0 | 0 | 0 | 0 |
    result = 0
    for k,i in enumerate(binary):
        result += int(i) * 2**(7-k)
    return result
