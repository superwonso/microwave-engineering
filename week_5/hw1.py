# Problem 1. Find the power PL (W) at ZL
# Problem 2. Modify ZL for maximum power transfer.
# Problem 3. Find the power PL (W) at ZL when ZL is modified for the maximum power transfer.
import math
Vs = complex(10*2*math.exp(j*math.pi/9))
Zs = complex(10*1 + j*10*4) #ohm, connected in series with Vs
ZL = complex(30*2 - j*40*9) # ohm, connected in series with Zs
PL= Vs*Vs/ZL
ZL_for_maximum_power_transfer = complex(30*2 - j*40*9)
PL_for_maximum_power_transfer = Vs*Vs/ZL_for_maximum_power_transfer
print("The power PL is: ", PL)
print("Modified ZL for maximum power transfer is: ", ZL_for_maximum_power_transfer)
print("The power PL for maximum power transfer is: ", PL_for_maximum_power_transfer)