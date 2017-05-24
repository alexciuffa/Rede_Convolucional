import arquivos as Dados

def get_matriz_forma(arquivo):
	if(Dados.existe_arq(arquivo)):
		matriz_forma = Dados.le_txt(arquivo)
		return matriz_forma
	#else:
	print("ERRO: arquivo não encontrado")
	print("Arquivo da matriz forma não encontrado")
	return None

def muda_type_da_matriz_str_para_float(matriz):
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			matriz[i][j] = float(matriz[i][j])
	return matriz

def get_submatriz_quadrada(matriz, tamanho, pos_inicial_x, pos_inicial_y):
	submatriz = []
	for i in range(pos_inicial_x, (pos_inicial_x + tamanho)):
		linha = []
		for j in range(pos_inicial_y, (pos_inicial_y + tamanho)):
			linha.append(matriz[i][j])
		submatriz.append(linha)
	return submatriz

def printa_matriz(matriz):
    for i in range(0, len(matriz)):
        print(matriz[i])

def get_menor_tamanho_x_y(matriz):
	tamanho_x = len(matriz)
	tamanho_y = len(matriz[0])
	for i in range(0, tamanho_x):
		if tamanho_y > len(matriz[i]):
			tamanho_y = len(matriz[i])
	return tamanho_x, tamanho_y

def menor_valor(valor1, valor2):
	if valor1<valor2:
		return valor1
	#else:
	return valor2

def get_menor_tamanho_entre_duas_matrizes(matriz_A, matriz_B):
	tamanho_x_A, tamanho_y_A = get_menor_tamanho_x_y(matriz_A)
	tamanho_x_B, tamanho_y_B = get_menor_tamanho_x_y(matriz_B)
	tamanho_x = menor_valor(tamanho_x_A, tamanho_x_B)
	tamanho_y = menor_valor(tamanho_y_A, tamanho_y_B)
	return tamanho_x, tamanho_y

def multiply_pixels(matriz_A, matriz_B, tamanho_x, tamanho_y):
	matriz_multiplicacao = []
	for i in range(0, len(matriz_A)):
		linha = []
		for j in range(0, len(matriz_A[i])):
			linha.append(matriz_A[i][j]*matriz_B[i][j])
		matriz_multiplicacao.append(linha)
	return matriz_multiplicacao

def soma_numeros_da_matriz(matriz):
	soma = 0
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			soma += matriz[i][j]
	return soma

def get_maior_numero_da_matriz(matriz):
	maior_num = matriz[0][0]
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			if maior_num < matriz[i][j]:
				maior_num = matriz[i][j]
	return maior_num

def filtering(parte_da_imagem, feature):
	tamanho_x, tamanho_y = get_menor_tamanho_entre_duas_matrizes(parte_da_imagem, feature)
	matriz_filtrada = multiply_pixels(parte_da_imagem, feature, tamanho_x, tamanho_y)
	valor_final = soma_numeros_da_matriz(matriz_filtrada)/(len(matriz_filtrada)*len(matriz_filtrada[0]))
	return valor_final

def convolucao(imagem, feature, tamanho):
	matriz_valores_finais = []
	for i in range (0, len(imagem)-2):#TIRAR ESSE -2 E GENERALIZAR
		linha = []
		for j in range(0, len(imagem[i])-2):#TIRAR ESSE -2 E GENERALIZAR
			parte_da_imagem = get_submatriz_quadrada(imagem, tamanho, i, j)
			linha.append(filtering(parte_da_imagem, feature))
		matriz_valores_finais.append(linha)
	return matriz_valores_finais

def printa_imagem(matriz):
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			if matriz[i][j] == -1:
				print("0 ", end = '')
			else:
				print("X ", end='')
		print()

def Rectified_Linear_Units(matriz):
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			if matriz[i][j] < 0:
				matriz[i][j] = 0
	return matriz

def pooling(matriz, tamanho):
	matriz_pooling = []
	for i in range(0, len(matriz)-1, tamanho):#TIRAR ESSE -1 E ARRUMAR
		linha = []
		for j in range(0, len(matriz[i])-1, tamanho):#TIRAR ESSE -1 E ARRUMAR
			#print("i: ", i, "j: ", j)
			submatriz = get_submatriz_quadrada(matriz, tamanho, i, j)
			linha.append(get_maior_numero_da_matriz(submatriz))
		matriz_pooling.append(linha)
	return matriz_pooling

def transforma_matriz_em_lista(matriz):
	lista = []
	for i in range(0, len(matriz)):
		for j in range(0, len(matriz[i])):
			lista.append(matriz[i][j])
	return lista

def acerta_dimensao_de_duas_matrizes(matriz_A, matriz_B):
	pass

'''
matriz = get_matriz_forma("x.txt")
printa_matriz(matriz)
matriz = muda_type_da_matriz_str_para_float(matriz)
tamanho = 3
pos_inicial_x = 4
pos_inicial_y = 4
parte_da_imagem = get_submatriz_quadrada(matriz, tamanho, pos_inicial_x, pos_inicial_y)
print("parte_da_imagem")
printa_imagem(parte_da_imagem)

tamanho = 3
pos_inicial_x = 1
pos_inicial_y = 1
feature = get_submatriz_quadrada(matriz, tamanho, pos_inicial_x, pos_inicial_y)
print("feature")
printa_imagem(feature)

tamanho_x, tamanho_y = get_menor_tamanho_entre_duas_matrizes(parte_da_imagem, feature)

matriz_final = multiply_pixels(parte_da_imagem, feature, tamanho_x, tamanho_y)
print("matriz_final")
printa_matriz(matriz_final)
print(soma_numeros_da_matriz(matriz_final))

print(filtering(parte_da_imagem, feature))
'''

imagem = get_matriz_forma("x.txt")
imagem = muda_type_da_matriz_str_para_float(imagem)
printa_imagem(imagem)

tamanho = 3
pos_inicial_x = 1
pos_inicial_y = 1
feature = get_submatriz_quadrada(imagem, tamanho, pos_inicial_x, pos_inicial_y)

matriz = convolucao(imagem, feature, tamanho)
print("Convolução")
printa_matriz(matriz)

matriz = Rectified_Linear_Units(matriz)
print("ReLU")
printa_matriz(matriz)

matriz_pool = pooling(matriz, 2)
print("Pooling")
printa_matriz(matriz_pool)