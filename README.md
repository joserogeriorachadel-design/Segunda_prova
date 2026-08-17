# Minha segunda prova da faculdade!
## Prova com 5 questões, feitas em python, questões escolhidas no beecrowd pelo professor:
- questão 1 - beecrowd | 1189
- questão 2 - beecrowd | 1534, mas com uma alteração: "Diferente do descrito, considere que os casos de teste se encerrem com o valor 0 (zero) para N."
- questão 3 - beecrowd | 2542, mas com uma alteração: "Diferente do descrito, considere que haja um único caso de teste a ser resolvido."
- questão 4 - foi feita pelo professor: descrição abaixo
- questão 5 - beecrowd | 2520, mas com uma alteração: "Diferente do descrito, considere que os casos de teste se encerrem com o valor 0 (zero) na entrada para ambas as variáveis m e n."
## Descrição questão 4:
### Sudoku
Sudoku é um jogo de lógica cujo objetivo é distribuir números de 1 a 9 em cada uma das células numa grade de 9x9 de tal forma que não haja repetição de um desses números em cada uma das linhas, em cada uma das colunas e em cada uma das subgrades (regiões) de 3x3 do tabuleiro.

O tabuleiro abaixo apresenta uma solução parcial, ou seja, uma distribuição parcial destes valores, faltando completar vários deles.

<img width="226" height="224" alt="sudoku" src="https://github.com/user-attachments/assets/19036915-d2c3-44f7-a718-8b8f8c992da3" />

Dado, agora, um valor k (1 ≤ k ≤ 9), queremos saber em quais linha e em quais colunas este valor NÃO aparece.

**Entrada**: Há nove linhas, cada uma delas contendo os nove números correspondentes à linha do tabuleiro, separados por um espaço em branco, onde o valor 0 (zero) indica que a célula ainda não foi preenchida. Após essas linhas está o valor  (1 ≤ k ≤ 9).
0 0 0 8 0 0 0 0 9

0 1 9 0 0 5 8 3 0

0 4 3 0 1 0 0 0 7

4 9 0 1 5 0 0 0 3

0 0 2 7 0 4 0 1 0

0 8 0 0 9 0 6 0 0

0 7 0 0 0 6 3 0 0

0 3 0 0 7 0 0 8 0

9 0 4 5 0 0 0 0 1

3

**Saída**: é composta por duas linhas, a primeira listando as linhas (valores entre 1 e 9, nesta ordem) do tabuleiro  nas quais o valor k não aparece, seguida de outra que lista as colunas (valor entre 1 e 9, nesta ordem) nas quais o valor k não aparece.
1 5 6 9

1 4 5 6
