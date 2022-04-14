from math import *
from cmath import *

j=complex(0,1)

while True:
 zL,z0 = map(complex,input('Load and input impedances: ZL,Z0(ohm)=').split())
 z2 = (z0+zL)/2
 f0,fb=map(float,input('freqency: f0,fb(Hz)=').split())
 z1=sqrt(z0*z2)
 LQ=3e8/4*f0
 print('Quarter-wave transformer: Z1(ohm), LQ(m)=',z1,LQ)
 while True:
     fb=float(input('Fractional bandwidth: fb='))
     n=int(input('Numer of points for freq. response: N='))
     if n==0:
        break
     df=f0*fb/n
     print('f(Hz) mag(S11)(dB) phase(S11)(deg)')
     for k in range(n+1):
         f=f0*(1-fb/2)+k*df ; wL=3e8/f ; beta=2*pi/wL
         zi=z1*(zL+j*z1*tan(beta*LQ))/(z1+j*zL*tan(beta*LQ))
         s11=(zi-z0)/(zi+z0) ; s11m=20*log10(abs(s11)) ; s11p=phase(s11)*180/pi
         print(f,s11m,s11p) 