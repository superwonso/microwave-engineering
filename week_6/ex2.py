from math import *

rad=pi/180
while True:
    z0=float(input('Impedance after matching: Z0 (ohm) (real) = '))
    L,C,rr,xx=map(float, input('Input Values: L,C,R,L2 = ').split())
    f0=float(input('Frequency Of Matching: f0 (Hz) = '))
    n=int(input('S11 Calculation Times'))
    r=rr/z0
    x=xx/z0
    y0=1/z0
    w0=2*pi*f0
    
    if r<=1:
        cs = C
        print(' Cs=',cs)
        Lp = L
        print(' Lp=',Lp) 
        
        f=0.8*f0-0.02*f0 
        for i in range(n):
            f=f+0.02*f0