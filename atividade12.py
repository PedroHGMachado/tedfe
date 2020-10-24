"""
Disciplina: Tratamento Estatístico de Dados em Física Experimental
Atividade: 12
Author: pedro.machado
"""

import numpy as np


def generete_XDpoints(N=1, X=2):

    points = np.random.rand(X*N).reshape(N, X)
    return points


def count_inner_radius(points, r=1):

    n = np.sum(np.sum(points**2, axis=1) <= r)
    return n

"""
1) Um exemplo didático do uso de simulações Monte Carlo é a estimativa estocástica do valor de 𝜋. A
ideia consiste gerar pontos uniformemente distribuídos no quadrado [0, 1] × [0, 1] e calcular a
frequência relativa com que os pontos gerados pertencem ao círculo de raio unitário centrado na origem,
uma vez que a probabilidade, 𝑝, de cada ponto gerado estar dentro do círculo é igual à razão entre a área
da seção do círculo (𝐴𝑆 = 𝜋/4) e a área do quadrado onde os pontos são gerados (𝐴𝑄 = 1): 𝑝 = 𝐴𝑆/𝐴𝑄 = 𝜋/4.
Na prática, o que se faz é gerar 𝑁 pares de valores, 𝑢1 e 𝑢2, com 𝑢1 e 𝑢2 distribuídos uniforme entre 0 e 1,
e verificar o número de casos, 𝑛, em que a condição 𝑢1^2 + 𝑢2^2 ≤ 1 é satisfeita.
O valor de 𝜋 é estimado por 𝑥 = 4𝑛/𝑁.

Faça uma rotina para fazer uma simulação com 𝑵 = 𝟏. 𝟎𝟎𝟎 pontos e responda os itens abaixo:
1.a) Qual é o valor de 𝑛 obtido na primeira simulação.
1.b) Estime a incerteza no valor de 𝑛, 𝜎̃𝑛 ≅ √𝑁𝑝(1 − 𝑝) usando a frequência relativa obtida na
simulação, 𝑛/𝑁, como valor aproximado para a probabilidade de sucesso (isto é, considerando 𝑝 ≅ 𝑛/N).
Note que essa aproximação seria a única opção caso o valor de 𝜋 não fosse conhecido.
Escreva essa incerteza com o número correto de algarismos significativos.
1.c) Calcule o valor correspondente de 𝑥 = 4𝑛/N e sua incerteza estimada, 𝜎̃𝑥 = 4𝜎̃𝑛/𝑁
(use o 𝜎̃𝑛 estimado no item 1.b). Escreva o resultado com o número correto de algarismos significativos.
"""


N1 = 1000
points1 = generete_XDpoints(N1, X=2)  # N pontos aleatórios no quadrado de 1X1.

# 1.a)
n1 = count_inner_radius(points1)      # Pontos internos ao raio 1
print(f"Questão 1.a) n = {n1}")


# 1.b)
p_bar1 = n1/N1
sigma_n1 = np.sqrt(N1*p_bar1*(1-p_bar1))
print(f"Questão 1.b) sigma_n = {sigma_n1}")


# 1.c)
x = 4*p_bar1
sigma_x = 4*sigma_n1/N1
print(f"Questão 1.c) x = {x} +- {sigma_x}")


"""
2) Considere agora o caso de uma versão em três dimensões da simulação: ou seja, são gerados 𝑁 pontos
com coordenadas, 𝑢1, 𝑢2 e 𝑢3, distribuídas uniformemente entre 0 e 1, e se contabiliza o número 𝑛 de
vezes em que os pontos gerados pertencem à esfera de raio unitário centrada na origem (isto é, quando
𝑢1^2 + 𝑢2^2 + 𝑢3^2 ≤ 1). Note que a razão entre os volumes é 𝑝 = 𝜋/6, de modo que neste caso o valor de 𝜋 é
estimado por 𝑦 = 6𝑛/𝑁.
Faça uma rotina para fazer uma simulação com 𝑵 = 𝟓𝟎𝟎 pontos e responda
(Atenção: o N é diferente do usado na questão 1):
2.a) Qual é o valor de 𝑛 obtido na primeira simulação efetuada.
2.b) Estime a incerteza no valor de 𝑛, 𝜎̃𝑛 ≅ √𝑁𝑝̃(1 − 𝑝̃), considerando a aproximação 𝑝 ≅ 𝑛/𝑁.
Escreva essa incerteza com o número correto de algarismos significativos.
2.c) Calcule 𝑦 = 6𝑛/𝑁 e estime sua incerteza (use o 𝜎̃𝑛 estimando no item 2.b).
Escreva o resultado como número correto de algarismos significativos.
"""

N2 = 500
points2 = generete_XDpoints(N2, X=3)

# 2.a)
n2 = count_inner_radius(points2)
print(f"Questão 2.a) n = {n2}")

# 2.b)
p_bar2 = n2/N2
sigma_n2 = np.sqrt(N2*p_bar2*(1-p_bar2))
print(f"Questão 2.b) sigma_n = {sigma_n2}")


# 2.c)
y = 6*p_bar2
sigma_y = 6*sigma_n2/N2
print(f"Questão 2.c) y = {y} +- {sigma_y}")


"""
3) Usando seus conhecimentos sobre binomial e sobre os problemas em questão, calcule os desviospadrões verdadeiros,
𝜎𝑛 = √𝑁𝑝(1 − 𝑝) de 𝑛 para os casos dos experimentos numéricos em duas e em três dimensões.
Escreva os desvios-padrões verdadeiros com dois algarismos significativos. Compare-os
com as incertezas de 𝑛 estimadas nos itens 1.b e 2.b.
"""

p1_real = np.pi/4
sigma_n1_real = np.sqrt(N1*p1_real*(1 - p1_real))


p2_real = np.pi/6
sigma_n2_real = np.sqrt(N2*p2_real*(1 - p2_real))

print(f"Questão 3)\n"
      f"sigma_n 1.b real = {sigma_n1_real}\n"
      f"sigma_n 2.b real = {sigma_n2_real}")

"""
4) Usando seus conhecimentos sobre binomial e sobre os problemas em questão, estime a quantidade de
pontos necessários no caso bidimensional para que a incerteza relativa na estimativa de 𝜋 seja de 0,1%
(ou seja, o valor de N para que 𝜎𝑥 = 0,001 ∗ 𝑥 ≈ 0,003, pois 𝑥 ≈ 𝜋 ≈ 3).

5) Repita a estimativa feita no item 4 para o caso de três dimensões.
"""

# 4)

# Formula obtida para obter precisão de 0,1% de x através de sigma_x
N4 = int(((4 - x)/x)*10**6)  # pontos
points4 = generete_XDpoints(N4, X=2)

n4 = count_inner_radius(points4)
p_bar4 = n4/N4
sigma_n4 = np.sqrt(N4*p_bar4*(1-p_bar4))

x4 = 4*p_bar4
sigma_x4 = 4*sigma_n4/N4

print(f"Questão 4) \n"
      f"N = {N4}\n"
      f"x = {x4}\n"
      f"sigma_x = {sigma_x4}")

# 5)

N5 = int(((6-x)/x)*10**6)
points5 = generete_XDpoints(N5, X=3)

n5 = count_inner_radius(points5)

p_bar5 = n5/N5
sigma_n5 = np.sqrt(N5*p_bar5*(1-p_bar5))

y5 = 6*p_bar5
sigma_y5 = 6*sigma_n5/N5

print(f"Questão 4) \n"
      f"N = {N5}\n"
      f"y = {y5}\n"
      f"sigma_y = {sigma_y5}")



