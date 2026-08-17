while  True:
    n_linhas, n_colunas = [int(x) for x in input().split()] 
    if n_linhas == 0 or n_colunas == 0:
        break 
    for i in range(n_linhas):
        linhas = [int(x) for x in input().split()] #le cada linha
        if 1 in linhas: #confere se a pessoa esta na linha
            linha_pessoa = i #ve qual linha ela ta
            coluna_pessoa = linhas.index(1)#ve qual coluna ela ta
        if 2 in linhas: #confere se o analogimon esta na linha
            linha_analogimon = i #ve qual linha ele ta
            coluna_analogimon = linhas.index(2) #ve qual coluna ele ta
            
    distancia = abs(linha_pessoa - linha_analogimon) + abs(coluna_pessoa - coluna_analogimon) #a distancia total é a soma da distancia das linhas e das colunas
    print(distancia)