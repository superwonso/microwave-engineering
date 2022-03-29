# Input : Y0(real), Yin(complex) 
# Output : The normalized input admittance Yin_n, The reflection coefficient Γ in magnitude(linear), The reflection coefficient Γ in phase(degree)
import math
Y0_real = float(input("Y0 real = "))
Yin_complex = complex(input("Yin complex = "))
Yin_n = Y0_real + Yin_complex
Γ_magnitude = math.sqrt(Yin_n.real * Yin_n.real + Yin_n.imag * Yin_n.imag)
Γ_phase = math.atan2(Yin_n.imag, Yin_n.real) * 180 / math.pi
print("Yin_n = {0:.2f} + {1:.2f}j".format(Yin_n.real, Yin_n.imag))
print("Γ in magnitude = {0:.2f}".format(Γ_magnitude))
print("Γ in phase = {0:.2f}".format(Γ_phase))