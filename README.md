# The [enigmapython](https://github.com/denismaggior8/enigma-python) wrapper package for MicroPython environment

I'm thrilled to announce that [enigmapython](https://github.com/denismaggior8/enigma-python), my powerful Enigma machine emulator, is now available on [MicroPython](https://micropython.org)! 🚀

🔹 Why is this exciting?

[enigmapython](https://github.com/denismaggior8/enigma-python) isn’t just a package... it’s a historically accurate and educational tool that allows students, researchers, and history enthusiasts to explore WWII cryptography hands-on. 

Now, with MicroPython support, you can run it on embedded devices like ESP32, Raspberry Pi Pico, and other microcontrollers!

🔹 How This Helps Education & Research

✅ Cryptography Lessons – Learn how encryption shaped history by experimenting with real Enigma machine settings on resource-constrained devices.

✅ Historical Research – Recreate encoded wartime messages and decrypt them just like WWII codebreakers.

✅ STEM & Embedded Systems – Run an Enigma emulator on a microcontroller, making learning cryptography more interactive than ever!

## Installation

Using mip (on network enabled devices):

```python
import mip
mip.install("github:denismaggior8/micropython-enigma-python", version="1.2.3")
```

## Releases

This repo mirrors the **enigmapython** releases on PyPi, meaning that by installing **micropython-enigma-python** version 1.2.3 (as in the example above) you get the **enigmapython** 1.2.3 PyPi equivalent.

## Examples

This a very simple MicroPython code that shows how to use the library

```python
# Import mip package manager
import mip

# Install enigmapython library
mip.install("github:denismaggior8/micropython-enigma-python", version="master")

# Import enigmapython modules
from enigmapython.EnigmaB_A133RotorI import EnigmaB_A133RotorI
from enigmapython.EnigmaB_A133Etw import EnigmaB_A133Etw
from enigmapython.EnigmaB_A133 import EnigmaB_A133
from enigmapython.ReflectorUKW_EnigmaB_A133 import ReflectorUKW_EnigmaB_A133

# Setup Enigma machine components
rotor1 = EnigmaB_A133RotorI(ring=0,position=0)
rotor2 = EnigmaB_A133RotorI(ring=0,position=0)
rotor3 = EnigmaB_A133RotorI(ring=0,position=0)
reflector = ReflectorUKW_EnigmaB_A133()
etw = EnigmaB_A133Etw()

# Setup Enigma B machine
enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)

# Let's encrypt a string
print(enigma.input_string("denis"))
```

To get more examples you can inspect this repo's [examples](./examples) folder or the original **enigmapython** examples [here](https://github.com/denismaggior8/enigma-python/tree/master/examples).