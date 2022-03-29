# Input : f,a,b, εr, tanδ, μr, σ (Parameters of a coaxial cable)
# Output : Z0, R, L, G, C, αc (dB/m), αd (dB/m), α (dB/m), β, λg 
import math
f=float(input("f(Hz): "))
a=float(input("a(mm): "))
b=float(input("b(mm): "))
er=float(input("εr: "))
tand=float(input("tanδ: "))
mur=float(input("μr: "))
sigma=float(input("σ(S/m): "))
u=a/b
L=(u/(math.pi*2))*math.log(b/a)
C=(2*math.pi*(er*(8.854e-12)))/math.log(b/a)
u0=4*math.pi*1e-7
Rs=math.sqrt((math.pi*f*u0)/sigma)
R=(Rs/2*math.pi)*((1/a)+(1/b))
w=(2*math.pi*math.sqrt(er*mur))/math.sqrt(L*C)
G=(2*math.pi*w*er*8.854e-12*tand)/math.log(b/a)
Z0=math.sqrt(L/C)
ac=R/(2*Z0)
ad=G/(2/Z0)
a=ac+ad
beta=w*math.sqrt(L*C)
lambda_g=2*math.pi/beta
print("Z0: ",Z0)
print("R: ",R)
print("L: ",L)
print("G: ",G)
print("C: ",C)
print("ac: ",ac)
print("ad: ",ad)
print("a: ",a)
print("beta: ",beta)
print("lambda_g: ",lambda_g)
