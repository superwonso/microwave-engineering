# RLC Circuit , C in series with a paralle circult of R and L
# input : R,L,C,f
# output : Z (impedance of the circuit)
pi = 3.141592653589793
R = float(input("Enter the resistance of the circuit in Ohms: "))
L = float(input("Enter the inductance of the circuit in Henrys: "))
C = float(input("Enter the capacitance of the circuit in Farads: "))
f = float(input("Enter the frequency of the circuit in Hertz: "))
w = 2*pi*f
Z = (R*L)/(R*L+1j*w*C)
print("The impedance of the circuit is: ", Z)
