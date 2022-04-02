# 2020037063 차동현
import cmath
pi=cmath.pi
R=float(input('R(ohm/m)='))
L=float(input('L(H/m)='))
G=float(input('G(S/m)='))
C=float(input('C(F/m)='))
while True:
    f=float(input('f(Hz,f<0 --> break)='))
    if f<0:
        break
    Z=complex(R,2*pi*f*L)
    Y=complex(G,2*pi*f*C)
    Z0=cmath.sqrt(Z/Y)
    gamma=cmath.sqrt(Z0)
    print('Z0=',Z0)
    print('gamma=',gamma)