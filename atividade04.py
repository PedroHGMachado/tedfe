"""
Disciplina: Tratamento Estatístico de Dados em Física Experimental
Atividade: 04
Author: pedro.machado
"""

import matplotlib.pyplot as plt
import numpy as np

# FUNCOES


def plot_hist(array, title, mean_array=None, std_array=None, bins=30):
    count_n, _, _ = plt.hist(array, bins=bins)

    if mean_array and std_array:
        max_count = max(count_n)
        plt.vlines([mean_array, mean_array + std_array, mean_array - std_array],
                   0, max_count, ['red', 'yellow', 'yellow'],
                   label=f'Média: {mean_array:.5}\nDesvP {std_array:.5}')
        plt.legend()

    plt.title(title)
    plt.ylabel('Contagens')
    plt.xlabel('Medida')
    plt.show()


"""
1) Considere uma grandeza 𝑦 cuja relação com os dados 𝑥 é dada por 𝑧 = sin(𝑥). 
Suponha que os dados 𝑥 sejam gaussianos com valor verdadeiro 𝑥0 = 85° e 𝜎𝑥 = 10°.
Estime a incerteza de 𝑦 usando o “Toy Monte Carlo” com 𝑁 = 10.000 simulações.
Escreva também o valor médio de 𝑦 com sua respectiva incerteza
"""

N = 10000  # simulações

x_zero = 85  # graus
s_x = 10  # graus

x = x_zero + s_x * np.random.randn(N)
stdev_x = np.std(x, ddof=1)
mean_x = np.mean(x)
stdev_xm = stdev_x / np.sqrt(N)

y = np.sin(np.deg2rad(x))
stdev_y = np.std(y, ddof=1)
mean_y = np.mean(y)
stdev_ym = stdev_y / np.sqrt(N)

plot_hist(x, '1 - Histograma de x', mean_x, stdev_x)
plot_hist(y, '1 - Histograma de y', mean_y, stdev_y)

print('-'*30, 'Resultados 1)', '-'*30)
print('y_médio:', mean_y)
print('y_incerteza:', stdev_y)
print('y_incerteza_da_média:', stdev_ym)
print('-'*80)


"""
2) Considere um experimento em que são medidos 𝑛 = 50 dados sujeitos à erros aleatórios
de desvio-padrão 28 e a um erro sistemático de desvio-padrão 3.
Considere que o valor verdadeiro da grandeza seja 𝑥0 = 100 e que os erros sejam gaussianos.
Simule 𝑴 = 𝟏𝟎.𝟎𝟎𝟎 repetições do experimento e registre os resultados finais, 𝒙𝒇, de cada
experimento (𝒙𝒇 é a média dos 𝒏 valores de 𝒙 obtidos em cada repetição do experimento).

a) Estime a incerteza de cada resultado final, 𝜎𝑓 (𝜎𝑓 é o desvio-padrão amostral dos valoresde 𝑥𝑓).
b) Em quantas das 𝑀 repetições o 𝑥𝑓 obtido foi maior que o valor verdadeiro da grandeza?
Nota: no Octave, isso pode ser calculado por 𝒔𝒖𝒎( 𝒙𝒇 > 𝒙𝟎)
c) Em quantas das 𝑀 repetições o módulo da diferença entre o valor de 𝑥𝑓 obtido e o valor
verdadeiro da grandeza foi menor que a incerteza do resultado final, 𝜎𝑓?
Nota: no Octave, isso pode ser calculado por 𝒔𝒖𝒎( 𝒂𝒃𝒔(𝒙𝒇 − 𝒙𝟎) < 𝒔𝒇 )

"""

M = 10000
N = 50

s_aleat = 28
s_sist = 3

x_zero = 100

real_data = np.zeros((M, N)) + x_zero
aleat_data = s_aleat * np.random.randn(M, N)
sist_data = s_sist * np.random.randn(M, 1)

data = (sist_data + real_data) + aleat_data

xfs = np.mean(data, axis=1)
# a)
stdev_xfs = np.std(xfs, ddof=1)
# b)
over_x_zero = np.sum(xfs > x_zero)
# c)
distance_less_std = np.sum(np.abs(xfs - x_zero) < stdev_xfs)


print('-'*30, 'Resultados 2)', '-'*30)
print('2)a) xf_inceteza:', stdev_xfs)
print('2)b) Valores Acima de x_zero:', over_x_zero)
print('2)c) Distância da média abaixo da incerteza:', distance_less_std)
print('-'*80)


"""
3) Considere o experimento de queda das bolinhas do alto do edifício Oscar Sala (Pelletron)
mostrado na 1ª aula (slides na página da disciplina no Moodle).
Supondo que o valor verdadeiro do tempo de queda seja 𝑡0 = 2,525 𝑠, simule experimentos onde
são medidos 𝑛 = 287 tempos sujeitos apenas a erros aleatórios gaussianos de desvio-padrão 𝜎𝑡 = 0,15 𝑠.
Simule 𝑴 = 𝟏𝟎.𝟎𝟎𝟎 repetições do experimento (cada experimento como sendo composto por 𝒏 = 𝟐𝟖𝟕
medições do tempo, 𝒕) e registre os resultados finais, 𝒕𝒇, de cada experimento
(𝒕𝒇 é a média dos 𝒏 valores de 𝒕 obtidos em cada repetição do experimento).

a) Usando o valor médio de tempo de cada simulação, 𝑡𝑓, calcule a aceleração de queda considerando
que a altura seja Δ𝐻 = 34,0 𝑚 e que a velocidade vertical inicial seja nula, 𝑎 = 2Δ𝐻 / (𝑡𝑓)^2.
Estime a incerteza dessas acelerações, 𝜎𝑎 (𝜎𝑎 é o desvio-padrão amostral dos
valores de 𝑎).
b) Calcule o valor verdadeiro da aceleração de queda, 𝑎0, usando o valor verdadeiro do
tempo de queda. Em quantas das 𝑀 repetições, o valor calculado de 𝑎 é maior que 𝑎0?
Em quantas o módulo da diferença entre 𝑎 e 𝑎0 é menor que a incerteza de 𝑎?
"""

M = 10000  # Número de experimentos
N = 287  # Número de rep. no experimento

t_zero = 2.525  # segundos
s_t = 0.15  #segundos

t = t_zero + s_t * np.random.randn(M, N)
tf = np.mean(t, axis=1)


# a)
delta_h = 34  # metros.
acceleration = (2 * delta_h) / (np.power(tf, 2))
mean_acce = np.mean(acceleration)
stdev_acce = np.std(acceleration, ddof=1)
stdev_acce_m = stdev_acce / np.sqrt(M)
plot_hist(acceleration, '3)a - Aceleração Peletron', mean_acce, stdev_acce)

# b)
a_zero = (2 * delta_h) / (t_zero**2)
over_a_zero = np.sum( acceleration > a_zero)
distance_less_a = np.sum( np.abs(a_zero - acceleration) < stdev_acce)


print('-'*30, 'Resultados 3)', '-'*30)
print('3)a) Incerteza da aceleração:', stdev_acce)
print('3)b) Valores acima de a_zero:', over_a_zero)
print('3)b) Distância média abaixo da incerteza:', distance_less_a)
print('-'*80)


"""
4) Refaça o exercício anterior, mas com a aceleração final de cada experimento, 𝑎𝑓′, calculada
como a média dos 𝑛 = 287 valores de aceleração correspondentes a cada um dos tempos
medidos (𝑎′ = 2Δ𝐻/𝑡^2). Note que no exercício 3 primeiro se calcula a média dos 𝑛 tempos de
queda e depois a aceleração correspondente ao tempo médio, ao passo que neste exercício
primeiro se calcula a aceleração correspondente a cada um dos tempos de queda e depois a
média dessas 𝑛 acelerações.
Simule 𝑴 = 𝟏𝟎.𝟎𝟎𝟎 repetições do experimento usando este procedimento e calcule a
incerteza dos valores de 𝑎′𝑓 obtidos. Em quantos casos 𝑎′𝑓 é maior que 𝑎0? Em quantos casos
a diferença entre 𝑎′𝑓 e 𝑎0 é menor que a incerteza de 𝑎′𝑓?
"""

M = 10000  # Número de experimentos
N = 287  # Número de rep. no experimento

t_zero = 2.525  # segundos
s_t = 0.15  #segundos

t = t_zero + s_t * np.random.randn(M, N)

delta_h = 34  # metros.
acceleration = (2 * delta_h) / (np.power(t, 2))

af = np.mean(acceleration, axis=1)

mean_acce = np.mean(af)
stdev_acce = np.std(af, ddof=1)
stdev_acce_m = stdev_acce / np.sqrt(M)
plot_hist(af, '4 - Aceleração Peletron', mean_acce, stdev_acce)

a_zero = (2 * delta_h) / (t_zero**2)
over_a_zero = np.sum( af > a_zero)
distance_less_a = np.sum( np.abs(a_zero - af) < stdev_acce)

print('-'*30, 'Resultados 3)', '-'*30)
print('4)a) Incerteza da aceleração:', stdev_acce)
print('4)b) Valores acima de a_zero:', over_a_zero)
print('4)b) Distância média abaixo da incerteza:', distance_less_a)
print('-'*80)