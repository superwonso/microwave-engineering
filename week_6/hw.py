import math

def zin(zl,z0,l):
    zin=z0*complex(zl,z0*math.tan(2*math.pi*l))/complex(z0,zl*math.tan(2*math.pi*l)) 
    return zin
print('Zin of ZL + transmission line:')
zl=complex(10*2,40*1)
z0=float(50)
l1=0; l2=0.5; n=100; dl=(l2-l1)/n 
print('\nl(wavelength), zin(complex)(ohm)') 
for i in range(1,n+2):
    l=(i-1)*dl
    print('{0:.3f} {1.real:.4f}+({1.imag:.4f}j)'.format(l,zin(zl,z0,l)))