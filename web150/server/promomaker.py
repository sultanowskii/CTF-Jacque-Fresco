from random import choice

SYMBOLS = [chr(i) for i in range(ord("A"), ord("Z") + 1)] + [str(i) for i in range(0, 10)]

def make_promo():
    promo = ["."] * 6
    for i in range(6):
        promo[i] = choice(SYMBOLS)
    return "".join(promo)