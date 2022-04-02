# input: Load impedance ZL (complex), characteristic impedance Z0 (real), transmission line length L (m), propagation constant γ (complex)
# output: Input reflection coefficient Γin (complex) 
import cmath
pi=cmath.pi
ZL = complex(input('ZL(ohm)='))
Z0 = float(input('Z0(ohm)='))
L = float(input('L(m)='))
gamma = complex(float(input('γ(ohm/m)=')))
Zin = ZL*(1+gamma*L)/(1-gamma*L)
print('Zin=',Zin)