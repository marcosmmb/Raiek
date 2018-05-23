from os import system
import random

def generate_seed():
    full_wallet_seed = hex(random.SystemRandom().getrandbits(256))
    wallet_seed = full_wallet_seed[2:].upper()
    return wallet_seed
