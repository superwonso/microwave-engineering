# inpput : L,C of lossless transmission line, f
# output : Z,Beta
# Z= sqrt(LC)/C
# Beta= (w*sqrt(LC))/C
import cmath
pi=3.141592653589793
L=float(input("Enter the length of the line in meters: "))
C=float(input("Enter the capacitance of the line in Farads: "))
f=float(input("Enter the frequency of the line in Hertz: "))
w=2*pi*f
Z=cmath.sqrt(L*C)/C
Beta=w*cmath.sqrt(L*C)/C
print("The impedance of the line is: ", Z)
print("The Beta of the line is: ", Beta)

