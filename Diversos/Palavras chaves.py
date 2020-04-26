import keyword

#copia a lista de palavras chaves para uma lista
"""chaves=keyword.kwlist"""
#faz a interacao para cada palavra chave e imprime
"""
for i in chaves:
    print(i)
"""
#faz a interacao para cada palavra chave e imprime sem usar uma variavel fora do for
for i in keyword.kwlist:
    print(i)
#imprime a lista toda    
print(keyword.kwlist)
#conta quantas palavras chaves tem e a imprime
cont=len(keyword.kwlist)
print(cont)
