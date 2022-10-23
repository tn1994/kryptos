import re
import uuid
import time
from multiprocessing import Pool, cpu_count

import pandas as pd
import streamlit as st

from ..services.vigenere.vigenere import Vigenere
from ..services.vigenere.vigenere import check_k4


class KryptosView:
    title = 'Kryptos Service'

    __key_1: str = str(uuid.uuid1())

    def main(self):
        st.title(self.title)

        kryptos_number = st.selectbox(
            label='Select Kryptos', options=[
                1, 2, 3, 4])

        match kryptos_number:
            case 1:
                vigenere_kryptos = Vigenere(is_k1=True)
            case 2:
                vigenere_kryptos = Vigenere(is_k2=True)
            case 3:
                vigenere_kryptos = Vigenere(is_k3=True)
            case 4:
                vigenere_kryptos = Vigenere(is_k4=True)
            case _:
                vigenere_kryptos = Vigenere(is_kryptos=False)

        cipher_text: str = st.text_area(
            label='Cipher Text',
            value=vigenere_kryptos.ciphertext)
        key_text: str = st.text_input(
            label='Key Text', value=vigenere_kryptos.key)

        if cipher_text is not None and key_text is not None and st.button(
                key=self.__key_1, label='Decrypt'):
            vigenere_kryptos.key = key_text
            vigenere_kryptos.decrypt(ciphertext=cipher_text)
            st.write('Decrypt text')
            st.write(vigenere_kryptos.plaintext)

            if vigenere_kryptos.is_k4:
                st.metric(
                    label='CHeck', value=check_k4(
                        text=vigenere_kryptos.plaintext))

                plaintext_lower: str = vigenere_kryptos.plaintext.lower()
                st.metric(
                    label='berlin',
                    value=True if 'berlin' in plaintext_lower else False)
                st.metric(
                    label='clock',
                    value=True if 'clock' in plaintext_lower else False)
                st.metric(
                    label='northeast',
                    value=True if 'northeast' in plaintext_lower else False)
                st.metric(
                    label='east',
                    value=True if 'east' in plaintext_lower else False)

        if st.button(label='Search'):
            self.search()
        if st.button(label='Search Using Pool'):
            self.search_using_pool()
        if st.button(label='Check'):
            self.checK()

    def search(self):
        word_txt_url: str = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
        df = pd.read_table(filepath_or_buffer=word_txt_url)

        decrypt_list = []
        if df is not None:
            st.table(df[:10])
            st.write(df.count())
            st.write(df['2'].values[:100])

            start_time = time.time()
            cnt = 0
            for padded_key in df['2'].values[:50]:
                result = re.search(r'[^A-Za-z]+', str(padded_key))
                if result is None:
                    vigenere_kryptos = Vigenere(
                        is_k4=True, set_padded_key=str(padded_key).upper())
                    cnt += 1

                    """
                    for key_text in df['2'].values:
                        result = re.search(r'[^A-Za-z]+', str(key_text))
                        if result is None:
                            vigenere_kryptos.key = str(key_text)
                            vigenere_kryptos.decrypt(ciphertext=vigenere_kryptos.ciphertext)
                            is_decrypt = check_k4(text=vigenere_kryptos.plaintext)
                            if is_decrypt:
                                decrypt_list.append(key_text)
                                """
            st.write(f'time: {time.time() - start_time}')
            st.write(f'{cnt=}')
            st.write(decrypt_list)

    def search_using_pool(self):
        # ref: https://github.com/dwyl/english-words
        word_txt_url: str = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
        df = pd.read_table(filepath_or_buffer=word_txt_url)

        search_words = []
        decrypt_list = []
        if df is not None:
            cnt = 0
            for padded_key in df['2'].values[:80]:
                result = re.search(r'[^A-Za-z]+', str(padded_key))
                if result is None:
                    vigenere_kryptos = Vigenere(
                        is_k4=True, set_padded_key=str(padded_key).upper())
                    search_words.append(
                        (str(padded_key).upper(), df['2'].values))
                    cnt += 1
            st.write(f'{cnt=}')

        print(f'{cpu_count() - 1=}')
        start_time = time.time()
        p = Pool(processes=cpu_count() - 1)
        result = p.map(self._search, search_words)
        st.dataframe(result)
        st.write(f'time: {time.time() - start_time}')

    def _search(self, inputs):
        padded_key, values = inputs
        decrypt_list = []
        vigenere_kryptos = Vigenere(
            is_k4=True, set_padded_key=str(padded_key).upper())
        for key_text in values:
            result = re.search(r'[^A-Za-z]+', str(key_text))
            if result is None:
                vigenere_kryptos.key = str(key_text)
                vigenere_kryptos.decrypt(
                    ciphertext=vigenere_kryptos.ciphertext)
                is_decrypt = check_k4(text=vigenere_kryptos.plaintext)
                if is_decrypt:
                    decrypt_list.append(key_text)
        return {str(padded_key).upper(): decrypt_list}

    def checK(self):
        vigenere_kryptos = Vigenere(is_k4=True)

        result = []
        start_time = time.time()
        for key_text in log:
            value: int = 0
            vigenere_kryptos.key = key_text
            vigenere_kryptos.decrypt(ciphertext=vigenere_kryptos.ciphertext)
            plaintext_lower: str = vigenere_kryptos.plaintext.lower()

            value += 1 if 'berlin' in plaintext_lower else 0
            value += 2 if 'clock' in plaintext_lower else 0
            value += 4 if 'northeast' in plaintext_lower else 0
            value += 8 if 'east' in plaintext_lower else 0
            result.append(value)
        st.write(f'time: {time.time() - start_time}')
        max_value = max(result)
        max_index = result.index(max_value)
        st.write(f'{max_index=}, {max_value=}')
        st.table(result)


log = [
    "alonely",
    "amphidiscophoran",
    "aphetism",
    "aphetize",
    "boyish",
    "boyishness",
    "boyishnesses",
    "boyism",
    "bonelessly",
    "Chyou",
    "colonels",
    "colonel's",
    "colonelships",
    "coronels",
    "dumbfounder",
    "hetmanship",
    "hybridisable",
    "hyperparathyroidism",
    "yeeuch",
    "isatid",
    "isocyanid",
    "isoniazid",
    "Japheth",
    "Jonel",
    "lairstone",
    "lazzarone",
    "leadstone",
    "lieutenant-colonelcy",
    "limestone",
    "lithopone",
    "loadstone",
    "lodestone",
    "lonelihood",
    "loneliness",
    "longicone",
    "Monel",
    "nannyberry",
    "nonelastic",
    "nonelected",
    "nonelector",
    "nonelusive",
    "Norry",
    "nurry",
    "Pyxidis",
    "pronely",
    "pseudoprophetic",
    "pseudoprophetical",
    "quasi-disgustedly",
    "quasi-distant",
    "Rhynchonellacea",
    "Rhynchonellidae",
    "rhipidistian",
    "Ronel",
    "Saidi",
    "Skidi",
    "small-boyish",
    "Stachytarpheta",
    "starry-nebulous",
    "supraquantivalence",
    "textbookish",
    "tonelessly",
    "Topheth",
    "Tuonela",
    "unlonely",
    "unoxidisable",
    "Urdummheit",
    "Viridis",
    "Whiteboyism",
    "zymograms",
    "zirams"
]
