"""Модуль с алгоритмами шифрования: Атбаш, Цезарь и Вегенер"""

from abc import ABC, abstractmethod

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
N = len(ALPHABET)


def _validate_type(value, type_, name):
    if not isinstance(value, type_):
        raise TypeError(f"{name} must be {type_.__name__}, got {type(value).__name__}")


class Cipher(ABC):
    """Абстрактный класс для представления шифров посимвольной замены"""

    def cipher(self, password):
        """Зашифровать переданный текст"""
        return self._run(self._one_char_cipher, password)

    def decipher(self, password):
        """
        Дешифровать переданный текст. Чтобы получить правильный ответ,
        дешифровать надо тем же алгоритмом и с теми же параметрами.
        """
        return self._run(self._one_char_decipher, password)

    @staticmethod
    def _run(fn, password):
        """Обработать `password` с помощью `fn`"""
        _validate_type(password, str, "password")
        output_password = []
        for i, ch in enumerate(password):
            num_ch = ALPHABET.find(ch)
            if num_ch != -1:
                output_password.append(ALPHABET[fn(num_ch, i)])
            else:
                output_password.append(ch)
        return "".join(output_password)

    @abstractmethod
    def _one_char_cipher(self, ch, i):
        """
        Зашифровать один символ, который задается своей позицией в алфавите и его
        порядковым номером (с нуля). Результат также должен быть позицией в алфавите
        """
        ...

    @abstractmethod
    def _one_char_decipher(self, ch, i):
        """
        Дешифровать один символ, который задается своей позицией в алфавите и его
        порядковым номером (с нуля). Результат также должен быть позицией в алфавите
        """
        ...


class Atbash(Cipher):
    """Шифр Атбаш"""
    def _one_char_cipher(self, ch, _i):
        return (N - 1 - ch) % N

    def _one_char_decipher(self, ch, _i):
        return self._one_char_cipher(ch, _i)


class Caesar(Cipher):
    """Шифр Цезаря, в качестве ключа используется целое число"""

    def __init__(self, key):
        _validate_type(key, int, "key")
        super().__init__()
        self.key = key

    def _one_char_cipher(self, ch, _i):
        return (ch + self.key) % N

    def _one_char_decipher(self, ch, _i):
        return (ch - self.key) % N


class Vigenere(Cipher):
    """Шифр Вегенера, в качестве ключа используется непустая фраза, все символы которой должны быть из алфавита"""

    def __init__(self, key):
        _validate_type(key, str, "key")
        if key == "":
            raise ValueError("key must not be empty")
        if any(ch not in ALPHABET for ch in key):
            raise ValueError("key must be be composed only from alphabet characters")

        super().__init__()
        self.key = [ALPHABET.find(ch) for ch in key]
        self.n = len(key)

    def _one_char_cipher(self, ch, i):
        return (ch + self.key[i % self.n]) % N

    def _one_char_decipher(self, ch, i):
        return (ch - self.key[i % self.n]) % N


