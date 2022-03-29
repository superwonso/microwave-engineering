# Input : Zin in real and imaginary format
# Output : admittance Yin in real and imaginary format
import math
Zin_real = float(input("Zin real = "))
Zin_imag = float(input("Zin imag = "))
Yin_real = 1 / (Zin_real + 1j * Zin_imag)
Yin_imag = -1j / (Zin_real + 1j * Zin_imag)
print("Yin real = {0:.2f} + {1:.2f}j".format(Yin_real.real, Yin_real.imag))
print("Yin imag = {0:.2f} + {1:.2f}j".format(Yin_imag.real, Yin_imag.imag))
