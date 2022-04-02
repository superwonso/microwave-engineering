#2020037063 차동현
# input : Load impedance ZL (complex), characteristic impedance Z0 (real)
# output : Reflection coefficient Γ (complex) 
import cmath
pi=cmath.pi
ZL = complex(input('ZL(ohm)='))
Z0 = float(input('Z0(ohm)='))
reflection_coefficient = cmath.sqrt(ZL/Z0)
print('Γ=',reflection_coefficient)