import random
numero_sorteado = random.randint(1, 20)

numero_escolhido = int(input("informe um numero entre 1 e 20:"))

"""
ex 01 if else
if numero_escolhido == numero_sorteado:
    print("voce acertou o numero")
else:
    print("voce errou o numero")
"""
"""
ex 02 while
while numero_escolhido != numero_sorteado:
    print("voce errou o numero escolha novamente")
    numero_escolhido = int(input("informe um numero entre 1 e 20:"))

print("voce acertou o numero e o numero escolhido foi:", numero_sorteado)
"""

#ex 03 while com contador

contador = 0 

while contador <=5: 
    print(contador)
    contador = contador + 1

    if numero_escolhido == numero_sorteado:
        print("voce acertou o numero")
    else:
        print("voce errou o numero, escolha novamente")
    numero_escolhido = int(input("informe um numero entre 1 e 20:"))