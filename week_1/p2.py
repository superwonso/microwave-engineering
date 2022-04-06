# input : Z,Beta
# output : L,C of lossless transmission line, f
import cmath
pi=3.141592653589793
Z=complex(input("Enter the impedance of the line: "))
Beta=complex(input("Enter the Beta of the line: "))
f=Beta/(2*pi)
w=2*pi*f
R=Z.real
C=1/(w*Z.imag)
L=Z.imag*C
print("The length of the line is: ", L)
print("The capacitance of the line is: ", C)
print("The frequency of the line is: ", f)