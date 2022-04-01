# Input : The Reflection coefficient Γ in magnitude(linear), The Reflection coefficient Γ in phase(degree), The Line characteristic admittance Y0(real)
# Output : The Input admittance
import math
import cmath
Γ_mag = float(input("Γ_mag: "))
Γ_phase = float(input("Γ_phase: "))
Y0_real = float(input("Y0_real: "))
Input_admittance = (1/(1+((Γ_mag*math.cos(Γ_phase*math.pi/180))+(Y0_real*Γ_mag*math.sin(Γ_phase*math.pi/180)))))
print("Input admittance: ",Input_admittance)
