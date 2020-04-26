def main():
	a = input('Digite a variável que deseja verificar')
	print('Tem espaço?', a.isspace())
	print('É número', a.isnumeric())
	print('É decimal', a.isdecimal())
	print('É um digito', a.isdigit())
	print('É um caractere ASCII', a.isascii())
	print('É'.isdecimal())
	print('É alfabético', a.isalpha())
	print('É alfanumerico', a.isalnum())
	print('Está em letra maúscula?', a.isupper())
	print('Está em letra minuscula?', a.islower())
	print('Está capitalizado?', a.istitle())


main()
