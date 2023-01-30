import hashlib


def hash_card_number(card_number):
    return hashlib.sha256(card_number.encode()).hexdigest()


def hash_cvv(cvv):
    return hashlib.sha256(cvv.encode()).hexdigest()


def hash_code(code):
    return hashlib.sha256(code.encode()).hexdigest()
