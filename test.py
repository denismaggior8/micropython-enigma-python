import sys
import os 
print(sys.path)
sys.path.insert(0, '/Users/denismaggiorotto/.micropython/lib')
print(sys.path)
import mip
mip.install("logging")
mip.install("copy")
import logging
import copy
from enigmapython.EnigmaB_A133RotorI import EnigmaB_A133RotorI
from enigmapython.EnigmaB_A133Etw import EnigmaB_A133Etw
from enigmapython.EnigmaB_A133 import EnigmaB_A133
from enigmapython.ReflectorUKW_EnigmaB_A133 import ReflectorUKW_EnigmaB_A133

rotor1 = EnigmaB_A133RotorI(ring=0,position=0)
rotor2 = EnigmaB_A133RotorI(ring=0,position=0)
rotor3 = EnigmaB_A133RotorI(ring=0,position=0)
reflector = ReflectorUKW_EnigmaB_A133()
etw = EnigmaB_A133Etw()


# Setup Enigma B machine
enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)

print(enigma.input_string("denis"))

