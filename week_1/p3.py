# Complex number calculations
# input = z1, z2
# output = z3 = z1+z2, abs(z2),abs(z3)

z1= complex(input("Enter the first complex number: "))
z2 = complex(input("Enter the second complex number: "))
z3 = z1+z2
print("The sum of the two complex numbers is: ", z3)
print("The absolute value of the second complex number is: ", abs(z2))
print("The absolute value of the sum of the two complex numbers is: ", abs(z3))
