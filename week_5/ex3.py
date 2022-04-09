# Scattering parameters of a series element on a transmission line
# Input : z0(transmission line charaetrtistic impedance, ohm), z(Series impedance, ohm)
# Output : S11, S12, S21, S22 in polar form
import math
import cmath
z0 = complex(input("Enter the transmission line characteristic impedance: "))
z = complex(input("Enter the Series impedance: "))
S11 = (z0 + z)/(z0 + z)
S12 = (z0 - z)/(z0 + z)
S21 = (z0 - z)/(z0 + z)
S22 = (z0 + z)/(z0 + z)
print("The S11 in polar form is: ", S11)
print("The S12 in polar form is: ", S12)
print("The S21 in polar form is: ", S21)
print("The S22 in polar form is: ", S22)
