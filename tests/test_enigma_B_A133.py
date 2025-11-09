# Import enigmapython modules
from enigmapython.EnigmaB_A133RotorI import EnigmaB_A133RotorI
from enigmapython.EnigmaB_A133Etw import EnigmaB_A133Etw
from enigmapython.EnigmaB_A133 import EnigmaB_A133
from enigmapython.ReflectorUKW_EnigmaB_A133 import ReflectorUKW_EnigmaB_A133
from assertion import assert_eq, assert_true, assert_false
from base_test import BaseTest

class EnigmaB_A133TestCase(BaseTest):

    def test_enigma_B_A133_ring_and_position_0(self):
        rotor1 = EnigmaB_A133RotorI(ring=0,position=0)
        rotor2 = EnigmaB_A133RotorI(ring=0,position=0)
        rotor3 = EnigmaB_A133RotorI(ring=0,position=0)
        reflector = ReflectorUKW_EnigmaB_A133()
        etw = EnigmaB_A133Etw()
        enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)
        return assert_eq(enigma.input_string("denis"),"mmvok", "Enigma encryption failed")

    def test_enigma_B_A133_ring_and_position_0_1(self):
        rotor1 = EnigmaB_A133RotorI(ring=0,position=0)
        rotor2 = EnigmaB_A133RotorI(ring=0,position=0)
        rotor3 = EnigmaB_A133RotorI(ring=0,position=0)
        reflector = ReflectorUKW_EnigmaB_A133()
        etw = EnigmaB_A133Etw()
        enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)
        return assert_eq(enigma.input_string("denis"),"mmvoke", "Enigma encryption failed")

def run():
    return EnigmaB_A133TestCase().run()

if __name__ == "__main__":
    run()