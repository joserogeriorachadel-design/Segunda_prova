while True:
    try:
        dimensoes = int(input())
    except EOFError:
        break #testa até nao ter mais entradas
    else:
        matriz = []
        for _ in range(dimensoes):
            linha = list('3' * dimensoes) #forma a matriz so com 3
            matriz.append(linha)
        for i in range(dimensoes):
            for j in range(dimensoes): 
                if i == j:
                    matriz[i][j] = '1' #troca a diagonal principal por 1s
                if i + j == dimensoes - 1: 
                    matriz[i][j] = '2' #troca a secundaria por 2s, mesmo que o 3 ja tenha sido trocado por 1(elementro central)
                    
        for linha in matriz:
            print(*linha, sep='')