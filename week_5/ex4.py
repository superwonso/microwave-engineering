# Two-port output-side matching
# Input : System reference impedance Z0(ohm, real), Load impedance Zs(ohm, real/imaginary form), Two-port scattering parameters S11, S21, S12, S22 in polar form
# Output : Γo(output reflection coefficient (in polar form) of the two-port network), Zo(output impedance (Ω) (in real and imaginary form) of the two-port network) , ZL_opt(optimum value of the load impedance ZL for maximizing the power delivered to the load ZL)
import math
import cmath
Z0 = complex(input("Enter the system reference impedance: "))
Zs = complex(input("Enter the load impedance in real and imaginary form: "))
S11 = complex(input("Enter the S11 in polar form: "))
S21 = complex(input("Enter the S21 in polar form: "))
S12 = complex(input("Enter the S12 in polar form: "))
S22 = complex(input("Enter the S22 in polar form: "))
Γo = (S11*S22 - S12*S21)/(S11*S22 + S12*S21)
Zo = Z0*(S11 + S22 - S12*cmath.conjugate(S21))/(S11*S22 + S12*S21)
ZL_opt = Z0*(S11 + S22 - S12*cmath.conjugate(S21))/(S11*S22 + S12*S21)*(S11*S22 + S12*S21)
print("The output reflection coefficient is: ", Γo)
print("The output impedance is: ", Zo)
print("The optimum value of the load impedance is: ", ZL_opt)