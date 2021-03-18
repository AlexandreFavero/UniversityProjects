#importar módulos

#Definição de funções
def Exibe_em_hexagemal(h, m, s) :
    """Verifica se é possivel simplificar os dados fornecidos de horario"""
    nmin_sec=s//60
    rsec=s%60
    nhora_min=(m+nmin_sec)//60
    rmin=(m+nmin_sec)%60
    rh=h%24
    nhora=rh+nhora_min

    print("%02ih%02im%02is"%(nhora, rmin, rsec))
#Programa principal

H=int(input('Escreva o número de horas:'))
M=int(input('Escreva o número de minutos:'))
S=int(input('Escreva o número de segundos:'))

print("O horário é: ")
Exibe_em_hexagemal(H, M, S)
 