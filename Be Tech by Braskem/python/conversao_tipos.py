#conversão de tipos

idade = "26"
numero1 = "10"
numero2 = "20"

print(numero1 + numero2)
print(int(numero1) + int(numero2))

idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira))

#int() converte para inteiro
#float() converte para float
#str() converte para string
#bool() converte para booleano

altura = float (input( "informe a sua altura: " ))

print(altura, type(altura))
