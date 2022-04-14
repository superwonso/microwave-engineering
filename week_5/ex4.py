# Two-port output-side matching
import math
import cmath
Z0 = complex(input("Enter the system reference impedance: "))
Zs = complex(input("Enter the load impedance in real and imaginary form: "))
S11 = complex(input("Enter the S11 in polar form: "))
S21 = complex(input("Enter the S21 in polar form: "))
S12 = complex(input("Enter the S12 in polar form: "))
S22 = complex(input("Enter the S22 in polar form: "))
r_0 = (S11*S22 - S12*S21)/(S11*S22 + S12*S21)
Z_o = Z0*r_0
ZL_opt = Zs*Z_o
print("The output reflection coefficient is: ", r_0)
print("The output impedance is: ", Z_o)
print("The optimum value of the load impedance is: ", ZL_opt)