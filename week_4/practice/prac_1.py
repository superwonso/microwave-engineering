# Input : reflection coefficient Γ in magnitue (linear) and phase (degree)
# Output : reflection coefficient Γ in real and imaginar format
import math
Γ_mag = float(input("Γ magnitue = "))
Γ_phase = float(input("Γ phase = "))
Γ_real_mag = Γ_mag * math.cos(Γ_phase * math.pi / 180)
Γ_imag_mag = Γ_mag * math.sin(Γ_phase * math.pi / 180)
Γ_real_phase = math.atan2(Γ_imag_mag, Γ_real_mag) * 180 / math.pi
Γ_imag_phase = math.atan2(Γ_imag_mag, Γ_real_mag) * 180 / math.pi
print("Γ in magnitue = {0:.2f} + {1:.2f}j".format(Γ_real_mag, Γ_imag_mag))
print("Γ in phase = {0:.2f} + {1:.2f}j".format(Γ_real_phase, Γ_imag_phase))
