# Input : The Reflection coefficient Γ in magnitude(linear), The Reflection coefficient Γ in phase(degree), The Line characteristic admittance Y0(real)
# Output : The Input admittance
import math
Γ_magnitude = complex(input("Γ in magnitude = "))
Γ_phase = complex(input("Γ in phase = "))
Y0_real = float(input("Y0 real = "))
Yin_n = Γ_magnitude * math.cos(Γ_phase * math.pi / 180) + 1j * Γ_magnitude * math.sin(Γ_phase * math.pi / 180)
Yin_n = Y0_real + Yin_n
print("Yin_n = {0:.2f} + {1:.2f}j".format(Yin_n.real, Yin_n.imag))