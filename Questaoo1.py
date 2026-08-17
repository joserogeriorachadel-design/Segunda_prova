operacao = input()
matriz = []
soma = 0
for _ in range(12):
    linha = []
    for _ in range(12):
        elemento = float(input())
        linha.append(elemento)
    matriz.append(linha) #faz a leitura da matriz
for j in range(5): #percorre cada coluna ate a 4(ultima que tem elemento a ser somado)
    for i in range(j+1 ,13 + j - 2*(j+1)):#percorre em cada coluna, pegando os itens que devem ser somados
        soma += matriz[i][j]
        
resultado = soma if operacao == 'S' else soma /  30 #confere se a operacao pedida é soma ou media(divide pela quantidade de elementos)

print(f'{resultado:.1f}')