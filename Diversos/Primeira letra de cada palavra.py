#imprimir a primeira letra de cada palavra da frase
st = 'Print only the words that with s in the sentence'
list_st=st.split(" ")
print(list_st)
for i in list_st:
    print(i[0:1])
