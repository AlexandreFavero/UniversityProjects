D1=int(input('digite o valor do dinheiro:'))
N50=D1//50 
R50=D1%50
N10=R50//10
N1=R50%10 
print("voce deve %2.f notas de 50 reais, %2.f notas de 10 reais e %2.f moedas de um real" 
      %(N50, N10, N1))

