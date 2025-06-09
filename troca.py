lista = [91,58,-41,85,-81,87,9,10,-49,39]

lista2 = lista.copy()
lista3 = lista.copy()
menor = lista.index(min(lista))


if lista[0] > lista[menor]:
    lista2 [0] = lista[menor] 
    lista3[0] = lista2[0]
    lista3[menor] = lista[0]

    print('1')
    print(lista3)
else:
    print('0')

# def lista_troca_menor_primeiro(lista):

#     lista = [2,4,6,8,1,3,5,7]
#     lista2 = lista.copy()
#     lista3 = lista.copy()
#     menor = lista.index(min(lista))

    
#     if lista[0] > lista[menor]:
#         lista2 [0] = lista[menor] 
#         lista3[0] = lista2[0]
#         lista3[menor] = lista[0]

#         return 1
    
#     else:
#         return 0
   