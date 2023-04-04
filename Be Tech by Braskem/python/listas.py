# > listas
#antes
nota1 = 7.9
nota2=9.7
nota3=8.2

#com listas
notas = [7.9, 9.7, 8.2]

#criando listas
lista=[] #lista vazia
lista= list() #lista vazia
lista=[26, "bayron", 3.1415, False]
lista_de_listas= [10, [1,2,3]]

#indexação e slices 

lista=[26, "bayron", 3.1415, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

#slices

lista=[10,50,30,40,25,60,5]
print(lista[0:3])
print(lista[3:6])
print(lista[0:7:2])
print(lista[::2])
print(lista[2:6:2])

#interaçoes com for
#1 utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

#2 utilizando os indices da lista
print("comprimento da lista: ", len(lista))
for i in range(len(lista)):
    print(lista[i])
    