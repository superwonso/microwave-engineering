# Poynting's Theorem
# Input : εr, tanδe : medium's dielectric constant and dielectric loss tangent, μr, tanδm : medium's relative permittivity and magnetic loss tangent, f : frequency(Hz), E : electric field strength(V/m)
# Output : Pr : radiated power(planewave power) per unit area(W/m^2), Pl : loss power per unit volume(W/m^3), Wm : stored magnetic energy per volume(J/m^3), We : stored electric energy per volume(J/m^3)
from math import *
ε0=8.854e-12; μ0=4*pi*1e-7 
εr = float(input("Medium's dielectric constant : "))
tanδe = float(input("Medium's dielectric loss tangent : "))
μr = float(input("Medium's relative permittivity : "))
tanδm = float(input("Medium's magnetic loss tangent : "))
f = float(input("Frequency(Hz) : "))
E = float(input("Electric field strength(V/m) : "))
w=2*pi*f; e=ε0*εr; u=μ0*μr 
eta= sqrt(u/e)
H = E/eta
Pr = E*H/ 2
e_prime = ε0*εr*tanδe
e_prime_prime = e_prime*tanδm
σ = w*e_prime_prime
u_prime = u*tanδm
u_prime_prime = u_prime*tanδe
Pl =(σ+w*e_prime_prime)*(E**2)+w*u_prime_prime*(H**2)/ 2
Wm = u_prime*(H**2) / 4
We =e_prime*(E**2) / 4
print("Radiated power(planewave power) per unit area(W/m^2) : ",Pr)
print("Loss power per unit volume(W/m^3) : ",Pl)
print("Stored magnetic energy per volume(J/m^3) : ",Wm)
print("Stored electric energy per volume(J/m^3) : ",We)
