tabuleiro = []
for _ in range(9):
    linhas = [int(x) for x in input().split()]
    tabuleiro.append(linhas) #le as linhas e bota no tabuleiro
    
k = int(input())
lista_de_linhas = [] #usado para adicionar as linhas que nao tenham k
lista_de_colunas = [] #usado para adicionar as colunas que nao tenham k

for i in range(9):
    if not k in tabuleiro[i]: #confere se o k nao esta na linha 
        lista_de_linhas.append(i+1) #se nao tiver adiciona a linha sem k, com o indice da vida real
        
for j in range(9):
    nao_tem_k = True #supoe que nao tenha k
    for i in range(9):
        if tabuleiro[i][j] == k: #vai conferindo cada item da coluna para ver se tem k na coluna
            nao_tem_k = False  #se tiver, a suposicao de nao tem é falsa
            break
    if nao_tem_k: #se continuar verdadeira, é porque nao tem k na coluna
        lista_de_colunas.append(j+1) #adiciona essa coluna na lista, com o indice da vida real
        
print(*lista_de_linhas)
print(*lista_de_colunas)