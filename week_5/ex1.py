# Input : Is(RMS Source voltage, complex in polar form), Ys(source impedance, complex in real and imaginary form), Yl (load impedance, complex in real and imaginary form)
# Output : Il(RMS load current in polar form), Vl(RMS load voltage in polar form), Pl(power dissipated in Yl), Pg(power dissipatged in Ys), Ps(power supplied by Is)
import math 
import cmath

Is = complex(input("Enter the source current in polar form: "))
Ys = complex(input("Enter the source impedance in real and imaginary form: "))
Yl = complex(input("Enter the load impedance in real and imaginary form: "))

Il = Is/Ys
Vl = Is*Yl
Pl = Is*Yl*Ys
Pg = Is*Ys
Ps = Is*Ys*Yl

print("The load current is: ", Il)
print("The load voltage is: ", Vl)
print("The power dissipated in the load is: ", Pl)
print("The power dissipated in the source is: ", Pg)
print("The power supplied by the source is: ", Ps)