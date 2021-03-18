#importações
import math 
V_inicial= float(input("digite a velocidade incial:"))
Angulo= float(input("digite a angulo de lnçamento em graus:"))
k= math.radians(Angulo)
S= (((V_inicial)**2)/9.81)*math.sin(2*k)
print("O alcance é %f" %S)