#metodos de listas
lista=[1,3,12,8,2]

#append
print("antes do append:",lista)
lista.append(3)

print("depois do append: ",lista)

#insert

lista.insert(2,10)
print("depois do insert: ",lista)


#extend

lista2=[1,2,3,4,5]
lista.extend(lista2)
print("depois do extend: ",lista)

#pop

lista.pop()
print("depois do pop: ",lista)

lista.pop(0)
print("depois do pop: ",lista)

#remove

lista.remove(3)
print("depois do remove: ",lista)

#count

print("quantidade de 2 na lista", lista.count(2))

#index

print("indice do elemento 12:", lista.index(12))

#sort

lista.sort(reverse=True)

print("depois do sort: ",lista)

#funçoes para listas 


#len
print(len(lista))

#sum

print(sum(lista))


#max

print(max(lista))


#min

print(min(lista))

#sorted

print(sorted(lista))

