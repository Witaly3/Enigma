import unittest
from enigma import *


class MyTestCase(unittest.TestCase):
    def test_rotor(self):
        self.assertEqual(rotor('A', 0), 'A')
        self.assertEqual(rotor('G', 1), 'D')
        self.assertEqual(rotor('S', 2), 'Z')
        self.assertEqual(rotor('I', 3), 'R')
        self.assertEqual(rotor('G', 0, reverse=True), 'G')
        self.assertEqual(rotor('K', 1, reverse=True), 'B')
        self.assertEqual(rotor('J', 2, reverse=True), 'B')
        self.assertEqual(rotor('Y', 3, reverse=True), 'O')

    def test_reflector(self):
        self.assertEqual(reflector('C', 0), 'C')
        self.assertEqual(reflector('W', 1), 'V')

    def test_changing(self):
        self.assertEqual(changing('A', 5), 'F')
        self.assertEqual(changing('S', 10), 'C')
        self.assertEqual(changing('W', 20), 'Q')
        self.assertEqual(changing('A', 0), 'A')

    def test_switching(self):
        self.assertEqual(switching('A', ['AC']), 'C')
        self.assertEqual(switching('N', ['GD', 'OS', 'NK']), 'K')

    def test_enigma(self):
        self.assertEqual(enigma('A', 1, 1, 0, 2, 0, 3, 0, ''), 'B')
        self.assertEqual(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'), 'Q')
        self.assertEqual(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'), 'D')
        self.assertEqual(enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0, ''), 'BDZGOWC')
        self.assertEqual(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'), 'Sorry, it is not possible to make the switching')
        self.assertEqual(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'), 'Sorry, it is not possible to make the switching')
        self.assertEqual(enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0), 'BDZGOWC')
        self.assertEqual(enigma('BDZGOWC', 1, 1, 0, 2, 0, 3, 0), 'AAAAAAA')
        self.assertEqual(enigma('AAAAAAA', 1, 2, 3, 2, 3, 2, 3), 'BGDMBTZ')
        self.assertEqual(enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA',
                                1, 2, 3, 2, 3, 2, 3), 'BGDMBTZUONCIZMORCPNVLGOVLMURTNZNDROPETXLPLYCMIBICXITUCM')
        self.assertEqual(enigma('AAAAAAA', 1, 2, 3, 2, 3, 2, 3), 'BGDMBTZ')
        self.assertEqual(enigma('xyz', 1, 3, 1, 1, 2, 2, 3), 'OLC')


if __name__ == '__main__':
    unittest.main()
