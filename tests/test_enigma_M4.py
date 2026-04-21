# Import enigmapython modules
from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4 import EnigmaM4
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from assertion import assert_eq
from base_test import BaseTest

class EnigmaM4TestCase(BaseTest):

    def test_enigma_M4_long_string_and_double_stepping(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM4RotorI(ring=0, position=15)
        rotor2 = EnigmaM4RotorII(ring=0, position=3)
        rotor3 = EnigmaM4RotorIII(ring=0, position=0)
        rotor4 = EnigmaM4RotorBeta(ring=0, position=0)
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
        
        expected_output = "dzgovbuypkojwbowseemtzfwygkodtbzdqrczcifdidxcqzookviiomllegmsojxhnfhbofdzctzqpowvomqnwqquozufmsdxmjx"
        result = enigma.input_string("a"*100)
        
        return assert_eq(result, expected_output, "Enigma M4 long string double stepping failed")

def run():
    return EnigmaM4TestCase().run()

if __name__ == "__main__":
    run()
