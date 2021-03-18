# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:39:11 2021

@author: Alexandre Del Fávero
"""

a=float(input("Digite a medida do primeiro lado do triângulo:"))
b=float(input("Digite a medida do segundo lado do triângulo:"))
c=float(input("Digite a medida do terceiro lado do triângulo:"))
s=(a+b+c)/2
k=((s*(s-a)*(s-b)*(s-c))**0.5)
print("a área do triângulo é %f"%(k))
