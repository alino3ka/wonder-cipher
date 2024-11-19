"""Различные методы шифрования и дешифрования, а также run_cipher"""

import string

alfavit = string.ascii_uppercase
alfavit_small = string.ascii_lowercase


def run_cipher(password, one_char_cipher, key):
    """Преобразует пароль побуквенно с помощью one_char_cipher"""
    output_password = []
    for i, ch in enumerate(password):
        in_alfavit = alfavit.find(ch)
        in_alfavit_small = alfavit_small.find(ch)
        if in_alfavit != -1:
            another_ch = one_char_cipher(i, in_alfavit, key)
            output_password.append(alfavit[another_ch])
        elif in_alfavit_small != -1:
            another_ch = one_char_cipher(i, in_alfavit_small, key)
            output_password.append(alfavit_small[another_ch])
        else:
            output_password.append(ch)
    return ''.join(output_password)


def ceaser(i, ch, key):
    """Шифрования методом Цезаря, key это целое число, которое обозначает сдвиг"""
    return (ch + key) % 26


def atbash(i, ch, key):
    """Шифрование и дешифрование методом Атбаша, не использует key"""
    return (25 - ch) % 26


def vinger(i, ch, key):
    """Шифрование методом Вижинера"""
    if alfavit.find(key[i % len(key)]) != -1:
        return (ch + alfavit.find(key[i % len(key)])) % 26
    else:
        return (ch + alfavit_small.find(key[i % len(key)])) % 26


def anti_ceaser(i, ch, key):
    """Дешифрование методом Цезаря, key это целое число, которое обозначает сдвиг"""
    return (ch - key) % 26


def anti_vinger(i, ch, key):
    """Дешифрование методом Вижинера"""
    if alfavit.find(key[i % len(key)]) != -1:
        return (ch - alfavit.find(key[i % len(key)])) % 26
    else:
        return (ch - alfavit_small.find(key[i % len(key)])) % 26
