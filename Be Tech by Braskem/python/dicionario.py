#dicionarios 

#criando dicionario

dicionario= {}
dicionario= dict()


dicionario= { "nome": "bayron", "idade": 36, "altura": 1.71 , "curso": "Python"}	

print(dicionario)
print(dicionario["idade"])

#adicionando elementos no dicionario

dicionario["programador"] = True
print(dicionario)

dicionario["altura"] = 2.00
print(dicionario)


for chave in dicionario:
    print(chave, dicionario[chave])


#testando a existencia de uma chave

print("peso" in dicionario)
print("nome" in dicionario)