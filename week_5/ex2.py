# Input : S11, S12, S21, S22 , a1, a2 in polar form
# Output : b1 in polar form, p1i(port 1 incident power), p1r(port 1 reflected power), p1(power delivered to port 1)
import math
import cmath
S11 = complex(input("Enter the S11 in polar form: "))
S12 = complex(input("Enter the S12 in polar form: "))
S21 = complex(input("Enter the S21 in polar form: "))
S22 = complex(input("Enter the S22 in polar form: "))
a1 = complex(input("Enter the a1 in polar form: "))
a2 = complex(input("Enter the a2 in polar form: "))
b1 = (S11*a1 + S12*a2)/(S11*a1 + S12*a2 + S21*a1 + S22*a2)
p1i = (S11*a1 + S12*a2)*b1
p1r = (S21*a1 + S22*a2)*b1
p1 = p1i + p1r
print("The b1 in polar form is: ", b1)
print("The port 1 incident power is: ", p1i)
print("The port 1 reflected power is: ", p1r)
print("The power delivered to port 1 is: ", p1)