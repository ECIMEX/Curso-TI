cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)

""" resultado correto da questao é A soma dos n (no caso, n = 1000) 
primeiros termos da série 1, 1/2, 1/4, 1/8,... """