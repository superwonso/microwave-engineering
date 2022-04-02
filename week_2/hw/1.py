# input : Coaxial cable with a(given above), b(given above), μr = 1, εr = 2, tanδ = 0.001, σ = 5.8e7 S/m, f = 5.8 GHz
# output : Z0, γ, R, L, G, C, αc (dB/m), αd (dB/m), α (dB/m), λg
import cmath
pi=cmath.pi
a=float(input('a(m)='))
b=float(input('b(m)='))
μr=1
εr=2
tanδ=0.001
σ=5.8e7
f=5.8e9
Z0=complex(1,2*pi*f*a)
γ=cmath.sqrt(Z0)
R=complex(1,2*pi*f*b)
L=complex(1,2*pi*f*tanδ)
G=complex(1,2*pi*f*σ)
C=complex(1,2*pi*f*μr*εr)
αc=20*cmath.log10(cmath.sqrt(Z0/R))
αd=20*cmath.log10(cmath.sqrt(Z0/L))
α=20*cmath.log10(cmath.sqrt(Z0/G))
λg=1/cmath.sqrt(G)
print('Z0=',Z0)
print('γ=',γ)
print('R=',R)
print('L=',L)
print('G=',G)
print('C=',C)
print('αc=',αc)
print('αd=',αd)
print('α=',α)
print('λg=',λg)