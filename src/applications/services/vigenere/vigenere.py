from dataclasses import dataclass
from sympy.crypto.crypto import AZ
from sympy.crypto.crypto import encipher_vigenere
from sympy.crypto.crypto import decipher_vigenere
from sympy.crypto.crypto import padded_key


@dataclass
class Vigenere:
    key: str = None
    plaintext: str = None
    ciphertext: str = None
    is_kryptos: bool = True
    is_k1: bool = False
    is_k2: bool = False
    is_k3: bool = False
    is_k4: bool = False

    set_padded_key: str = 'KRYPTOS'

    def __post_init__(self):
        assert isinstance(self.is_kryptos, bool)
        if self.is_kryptos:
            assert self.is_k1 != any([self.is_k2, self.is_k3, self.is_k4])
            assert self.is_k2 != any([self.is_k1, self.is_k3, self.is_k4])
            assert self.is_k3 != any([self.is_k1, self.is_k2, self.is_k4])
            assert self.is_k4 != any([self.is_k1, self.is_k2, self.is_k3])

            self.alp = padded_key(self.set_padded_key.upper(), AZ())
            self.__set_key_for_kryptos()
            self.__set_cipher_text_for_kryptos()

        assert self.key is not None
        pass

    def __set_key_for_kryptos(self):
        if self.is_k1:
            self.key: str = 'PALIMPSEST'
        elif self.is_k2:
            self.key: str = 'ABSCISSA'
        elif self.is_k3:
            self.key: str = 'None'
        elif self.is_k4:
            self.key: str = 'None'
        else:
            raise ValueError
        pass

    def __set_cipher_text_for_kryptos(self):
        if self.is_k1:
            self.ciphertext: str = 'EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD'
        elif self.is_k2:
            self.ciphertext: str = ('VFPJUDEEHZWETZYVGWHKKQETGFQJNCE'
                                    'GGWHKK?DQMCPFQZDQMMIAGPFXHQRLG'
                                    'TIMVMZJANQLVKQEDAGDVFRPJUNGEUNA'
                                    'QZGZLECGYUXUEENJTBJLBQCRTBJDFHRR'
                                    'YIZETKZEMVDUFKSJHKFWHKUWQLSZFTI'
                                    'HHDDDUVH?DWKBFUFPWNTDFIYCUQZERE'
                                    'EVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDX'
                                    'FLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKF'
                                    'FHQNTGPUAECNUVPDJMQCLQUMUNEDFQ'
                                    'ELZZVRRGKFFVOEEXBDMVPNFQXEZLGRE'
                                    'DNQFMPNZGLFLPMRJQYALMGNUVPDXVKP'
                                    'DQUMEBEDMHDAFMJGZNUPLGESWJLLAETG')
        elif self.is_k3:
            self.ciphertext: str = 'None'
        elif self.is_k4:
            self.ciphertext: str = ('OBKR'
                                    'UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO'
                                    'TWTQSJQSSEKZZWATJKLUDIAWINFBNYP'
                                    'VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR')
        else:
            raise ValueError

    def encrypt(self,
                plaintext):
        if self.is_kryptos:
            self.ciphertext = encipher_vigenere(plaintext, self.key, self.alp)
        elif not self.is_kryptos:
            self.ciphertext = encipher_vigenere(plaintext, self.key)
        return self.ciphertext

    def decrypt(self,
                ciphertext):
        key: str = self.key.upper()
        if self.is_kryptos:
            self.plaintext = decipher_vigenere(ciphertext, key, self.alp)
        elif not self.is_kryptos:
            self.plaintext = decipher_vigenere(ciphertext, key)
        return self.plaintext


def check_k4(text: str):
    text_lower = text.lower()
    if 'berlin' in text_lower:
        return True
    if 'clock' in text_lower:
        return True
    if 'northeast' in text_lower:
        return True
    if 'east' in text_lower:
        return True
    return False
