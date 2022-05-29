from math import *
f, C, R, L=map(float, input('Inductor Model 2: f(Hz),C(F),R(ohm),L(H)=').split())
j=complex(0,1)
w=2*pi*f
z=1/(j*w*C+1/(R+j*w*L))
print(z)