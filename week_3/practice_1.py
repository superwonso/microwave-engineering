# Input : f(Hz), w(mm), h(mm), er, tand, sigma(S/m)
# Output : Z0(ohm), ere, R(ohm/m), L(H/m), G(Ohm/m), C(F/m), ac(dB/m), ad(dB/m), a(dB/m), beta(rad/m), lambda_g(m)
import math
mu=4*math.pi*1e-7 
v=3e8 
e0=8.854e-12
f=float(input("f(Hz): "))
w=float(input("w(mm): "))
h=float(input("h(mm): "))
er=float(input("er: "))
tand=float(input("tand: "))
sigma=float(input("sigma(S/m): "))
u=w/h
Z0_air=30*math.log10(1+(4/u)*(8/u)+math.sqrt((8/u)**2+(math.pi)**2))
ere=(er+1/2)+(er-1/2)*1/(math.sqrt(1+(12/u)))
Z0=Z0_air/math.sqrt(ere)
lambda_0=3e8/f
lambda_g=lambda_0/math.sqrt(ere)
beta=2*math.pi/lambda_g
rs=math.sqrt(math.pi*f*mu/sigma)
r=2*rs/(w*1e-3)
L=Z0_air/v
c=ere/(v*Z0_air)
g=2*math.pi*f*e0*er*tand*w/h
ac=r/(2*Z0)
ad=g/(2/Z0)
a=ac+ad
print("Z0: ",Z0)
print("ere: ",ere)
print("R: ",r)
print("G: ",g)
print("L: ",L)
print("C: ",c)
print("ac: ",ac)
print("ad: ",ad)
print("a: ",a)
print("beta: ",beta)
print("lambda_g: ",lambda_g)

