#gnarly_eqn.py

import pandas as pd
import math

df = pd.read_csv("/home/guest/fall_20/lab/oildrops/drops.csv")

#Constants in eqn 10 with proper units:
d = .96
rho = 8.86*10**-4
g= 980
eta = 1.822*10**-4
b = 6.17*10*8-4
p = 76.2
V = 450

v_rise = df['v_rise'].tolist() # list
v_fall = df['v_fall'].tolist() 

#a = math.sqrt((9*eta*v_fall)/(2*g*rho))
a=[]
for i in range(0, len(v_fall)):
    a.append(math.sqrt((9*eta*abs(v_fall[i]))/(2*g*rho)))


#### Equation 10 brackets:
    
bracket_1 = 400*math.pi*d*(math.sqrt((1/g*rho)*(9*eta/2)**3))

#bracket_2 = (1/(1 + b/(p*a)))**(3/2) 
#bracket_3 = (v_fall + v_rise*math.sqrt(v_fall))/V

bracket_2 = []
bracket_3 = []
for i in range(0, len(v_fall)):
    bracket_2.append((1/(1 + b/(p*a[i])))**(3/2))
    bracket_3.append((v_fall[i] + v_rise[i]*math.sqrt(abs(v_fall[i])))/V)
    
esu_conv = (1.6*10**-19)/(4.803*10**-10) # no vel


####
#q= bracket_1 * bracket_2 * bracket_3 * esu_conv

q = []

for i in range(0, len(v_fall)):
    q.append(bracket_1*bracket_2[i]*bracket_3[i]*esu_conv)

q_real = []

for i in range(0,10):
    q_real.append(i*(1.6*10**-19))
