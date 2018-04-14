from os import system
import random

def restart_docker(id):
    r = system("sudo docker restart " + str(id))
    if not r:
        return 1
    else:
        return 0

def generate_seed():
    full_wallet_seed = hex(random.SystemRandom().getrandbits(256))
    wallet_seed = full_wallet_seed[2:].upper()
    return wallet_seed