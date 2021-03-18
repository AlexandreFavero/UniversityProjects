# Importação dos módulos
from math import trunc, log10

# Definição das funções
def exibeFração(n, d):
    """exibe a fração na forma bonitinha"""
    ndig_n = trunc(log10(n)) + 1
    ndig_d = trunc(log10(d)) + 1
    ndig = max(ndig_n, ndig_d)
    print("%s%i" %(" "*(ndig - ndig_n), n))
    print("-"*ndig)
    print("%s%i" %(" "*(ndig - ndig_d), d))

# Programa principal
n1 = int(input("Digite o numerador da fração 1: "))
d1 = int(input("Digite o denominador da fração 1: "))

exibeFração(n1, d1)

n2 = int(input("Digite o numerador da fração 2: "))
d2 = int(input("Digite o denominador da fração 2: "))

exibeFração(n2, d2)

n = n1*d2 + n2*d1 
d = d1*d2

print("A soma das frações é:")
exibeFração(n, d)

