"""ref:https://en.wikipedia.org/wiki/Kryptos"""

from dataclasses import dataclass


@dataclass
class K4:
    """
    NOTE:
        k4 = K4()
        k4.main()
        encoding = 'utf-8'
        encoding = 'ascii'
        ciphertext = 'QQPRNGKSS'.encode(encoding=encoding)
        print(ciphertext)
    """
    k4 = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'

    hint_0 = ['NYPVTT', 'BERLIN']  # 2010 year

    hint_1 = ['MZFPK', 'CLOCK']  # 2014 year

    hint_2 = ['QQPRNGKSS', 'NORTHEAST']  # 2020 year

    hint_3 = ['FLRV', 'EAST']  # 2020 year

    hint_list = [hint_0, hint_1, hint_2, hint_3]

    hex_list: list = None
    dec_list: list = None
    bin_list: list = None

    def replace_from_hints(self,
                           original_k4,  # type:str
                           ):
        replaced_k4 = original_k4
        for hint in self.hint_list:
            word = hint[0]
            if word in self.k4:
                # replaced_k4 = replaced_k4.replace(word, f'"{hint[1]}"', 1)
                replaced_k4 = replaced_k4.replace(word, hint[1], 1)
        return replaced_k4

    def calc_binary(self,
                    string  # type: str
                    ):
        """ref: https://watchcontents.com/python-convert-bin-str/"""
        listStr = [c for c in string]

        print()
        print("To hex")
        hex_list = []
        for item in listStr:
            hex_list.append(hex(ord(item)))
            print(hex(ord(item)), end=" ")
        self.hex_list = hex_list
        print()

        print("To dec")
        dec_list = []
        for item in listStr:
            dec_list.append(int(ord(item)))
            print(int(ord(item)), end=" ")
        self.dec_list = dec_list
        print()

        print("To bin")
        bin_list = []
        for item in listStr:
            bin_list.append(bin(ord(item)))
            print(bin(ord(item)), end=" ")
        self.bin_list = bin_list

        return hex_list, dec_list, bin_list

    def calc_diff(self,
                  a_list,  # type:list
                  b_list  # type:list
                  ):
        assert len(a_list) == len(b_list)
        diff_list = []
        for i in range(len(a_list)):
            diff_list.append(a_list[i] - b_list[i])
        return diff_list

    def main(self):
        print(self.k4)

        # for hint in hint_list:
        #     print(hint)

        replaced_k4 = self.replace_from_hints(original_k4=self.k4)
        print(replaced_k4)

        hex_list_k4, dec_list_k4, bin_list_k4 = self.calc_binary(
            string=self.k4)
        hex_list_rep_k4, dec_list_from_rep_k4, bin_list_rep_k4 = self.calc_binary(
            string=replaced_k4)

        print()
        print('dec_list_k4:')
        print(dec_list_k4)
        print()
        print('dec_list_from_rep_k4')
        print(dec_list_from_rep_k4)

        # diff_hex_list = self.calc_diff(a_list=hex_list_k4, b_list=hex_list_rep_k4)
        # print()
        # print(diff_hex_list)

        diff_dec_list = self.calc_diff(
            a_list=dec_list_k4, b_list=dec_list_from_rep_k4)
        print()
        print(diff_dec_list)

        diff_bin_list = self.calc_diff(
            a_list=bin_list_k4, b_list=bin_list_rep_k4)
        print()
        print(diff_bin_list)
