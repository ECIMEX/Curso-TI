#funcoes 

#print() #funcao que imprime na tela
#input() #funcao que recebe dados do usuario
#len() #funcao que retorna o tamanho de um dado
#max() #funcao que retorna o maior valor


#2 criação de funções

#funçao inicial

#def saudacao(): 
 #   print("seja bem vindo")
 #   print("olá, e um prazer ter voce fazendo parte do curso")

#saudacao()

#função com parametro

#def saudacao(nome, curso):
#    print(f"seja bem vindo", nome)
#    print(f"olá, e um prazer ter voce fazendo parte do curso de ", curso)
#    print("ola", nome)

#saudacao("Bayron","Phyton")


#função com parametros default

def saudacao(nome, curso ="Phyton"):
    print(f"seja bem vindo", nome)
    print(f"olá, e um prazer ter voce fazendo parte do curso de ", curso)
    print("ola", nome)
saudacao("Bayron","C++") #notar que o paramentro default é Phyton, mas foi alterado para C++ no momento da chamada da função

#função com retorno

#def soma(num1, num2):
#    return num1 + num2
#resultado = soma(5, 7)
#print("o resultado da soma é ", resultado)

def calculadora (num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "operacao invalida"
    
resultado = calculadora(10 , 20 , "*")
print(resultado)

