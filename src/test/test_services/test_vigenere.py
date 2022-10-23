import pytest

from src.applications.services.vigenere.vigenere import Vigenere


class TestCase:

    def test_vigenere_valid(self):
        expected = 'VIGENERE'
        assert isinstance(expected, str)
        vigenere_kryptos = Vigenere(key='qiita', is_kryptos=False)
        vigenere_kryptos.ciphertext = 'LQOXNUZM'
        vigenere_kryptos.decrypt(ciphertext=vigenere_kryptos.ciphertext)
        actual = vigenere_kryptos.plaintext
        assert isinstance(actual, str)
        assert expected == actual

    def test_k1_valid(self):
        expected = 'BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION'
        assert isinstance(expected, str)
        vigenere_kryptos = Vigenere(is_k1=True)
        vigenere_kryptos.decrypt(ciphertext=vigenere_kryptos.ciphertext)
        actual = vigenere_kryptos.plaintext
        assert isinstance(actual, str)
        assert expected == actual

    def test_k2_valid(self):
        expected = (
            'ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE'
            'THEYUSEDTHEEARTHSMAGNETICFIELDX'
            'THEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONX'
            'DOESLANGLEYKNOWABOUTTHIS'
            'THEYSHOULDITSBURIEDOUTTHERESOMEWHEREX'
            'WHOKNOWSTHEEXACTLOCATION'
            'ONLYWWTHISWASHISLASTMESSAGEX'
            'THIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTH'
            'SEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTXLAYERTWO')
        assert isinstance(expected, str)
        vigenere_kryptos = Vigenere(is_k2=True)
        vigenere_kryptos.decrypt(ciphertext=vigenere_kryptos.ciphertext)
        actual = vigenere_kryptos.plaintext
        assert isinstance(actual, str)
        assert expected == actual

    def test_invalid(self):
        expected = True
        actual = False
        assert isinstance(expected, bool)
        assert isinstance(actual, bool)
        with pytest.raises(AssertionError):
            assert expected == actual
