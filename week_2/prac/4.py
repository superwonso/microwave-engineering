# Input: β, L 
# Output: Zin
import cmath
pi=cmath.pi
beta = float(input('β='))
L = float(input('L='))
Zin = complex(1,2*pi*beta*L)
print('Zin=',Zin)