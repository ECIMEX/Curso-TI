"""for variavel in range(10):
    print(variavel)"""

"""for variavel in range(1 , 11):
    print(variavel)
"""

"""for variavel in range(1, 112, 4):
    print(variavel)
"""

"""
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
"""
soma = 0 

for i in range(1, 4):
    nota=float(input(f"informe a sua nota{i}:"))
    soma = soma + nota

print(soma / 3)