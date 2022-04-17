"""
Disciplina: Tratamento Estatístico de Dados em Física Experimental
Atividade: 03
Author: pedro.machado
"""

# IMPORTS

import numpy as np
import matplotlib.pyplot as plt


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


# EXERCÍCIOS

"""
1) Considere uma grandeza 𝑥 cuja relação com os dados 𝑟 é dada por 𝑥 = 𝜋. 𝑟^2.
Suponha que os dados 𝑟 sejam gaussianos com valor verdadeiro 𝑟0 = 15,0 e desvio-padrão 𝜎𝑟 = 1,0.
Estime a incerteza de 𝑥 usando o “Toy Monte Carlo” com 𝑁 = 10.000 simulações.
Escreva também o valor médio de 𝑥 obtido nas simulações com sua respectiva incerteza.
"""

N = 10000  # Número de simulações

r_zero = 15.0  # Valor verdadeiro
s_r = 1.0  # Desvio padrão de r

r = r_zero + s_r * np.random.randn(N)  # Valores de r "medidos"

# Plotagem da distribuição dos r medidos.
mean_r = np.mean(r)
stdev_r = np.std(r, ddof=1)  # Equivalente a s_r
stdev_rm = stdev_r / np.sqrt(N)

assert (abs(stdev_r - s_r) < 1)  # Garante que sejam valores próximos

plot_hist(r, '1) Valores de r "medidos"', mean_r, stdev_r)

# Valores pedidos na atividade
x = np.pi * (r ** 2)  # Valores de x "medidos"
mean_x = np.mean(x)  # Valor médio de x
stdev_x = np.std(x, ddof=1)  # s_x
stdev_xm = stdev_x / np.sqrt(N)

# Plotagem da distribuição dos x medidos.
plot_hist(x, '1) Valores de x "medidos"', mean_x, stdev_x)

# Resultado final
r_value = f'{round(mean_r, 5)} ± {round(stdev_rm, 5)}'
x_value = f'{round(mean_x, 5)} ± {round(stdev_xm, 5)}'

print('-' * 20)
print('Resultados 1)')
print('Valor de r médio:', r_value)
print('Valor de x médio:', x_value)
print('Incerteza de x:', round(stdev_x, 5))
print('-' * 20)

"""
2) Considere uma grandeza 𝑦 cuja relação com os dados 𝑑 é dada por 𝑦 = 𝑑^3.
Suponha que os dados 𝑑 sejam gaussianos com valor verdadeiro 𝑑0 = 5,0 e 𝜎𝑑 = 1,0.
Estime a incerteza de 𝑦 usando o “Toy Monte Carlo” com 𝑁 = 10.000 simulações.
Escreva também o valor médio de 𝑦 com sua respectiva incerteza.
"""

N = 10000  # Número de simulações

d_zero = 5.0
s_d = 1.0

d = d_zero + s_d * np.random.randn(N)

mean_d = np.mean(d)
stdev_d = np.std(d, ddof=1)
stdev_dm = stdev_d / np.sqrt(N)

# Plotagem da distribuição dos d medidos.
assert (abs(stdev_d - s_d) < 1)  # Garante que sejam valores próximos

plot_hist(d, '2) Valores de d "medido"', mean_d, stdev_d)

y = d ** 3
mean_y = np.mean(y)
stdev_y = np.std(y, ddof=1)
stdev_ym = stdev_y / np.sqrt(N)

# Plotagem da distribuição dos y medidos.
plot_hist(y, '2) Valores de y "medido"', mean_y, stdev_y)

# Resultado Final
d_value = f'{round(mean_d, 5)} ± {round(stdev_dm, 5)}'
y_value = f'{round(mean_y, 5)} ± {round(stdev_ym, 5)}'

print('-' * 20)
print('Resultados 2)')
print('Valor de d médio:', d_value)
print('Valor de y médio:', y_value)
print('Incerteza de y:', round(stdev_y, 5))
print('-' * 20)

"""
3) Considere uma grandeza 𝑧 cuja relação com os dados 𝑎 e 𝑏 é dada por 𝑧 = 𝑎𝑏.
Suponha que 𝑎 e 𝑏 sejam gaussianos com valores verdadeiros 𝑎0 = 10,0 e 𝑏0 = 20,0
com desvios-padrões 𝜎𝑎 = 2,0 e 𝜎𝑏 = 2,0.

a) Estime a incerteza de 𝑧 usando o “Toy Monte Carlo” com 𝑁 = 10.000 simulações.
   Escreva também o valor médio de 𝑧 com sua respectiva incerteza.
   
b) Refaça as simulações considerando o valor de 𝑏 fixo (isto é, sem incerteza, 𝜎𝑏 = 0)
   para estimar a incerteza que 𝑧 tem apenas por causa da incerteza de 𝑎 (isto é, 𝜎𝑧[𝑎]).

c) Refaça novamente as simulações fixando agora o valor de 𝑎 e estime a incerteza de 𝑧
   apenas por causa de 𝑏 (isto é, 𝜎𝑧[𝑏]).
"""

N = 10000  # Número de simulações

# a)

a_zero = 10.0
s_a = 2.0

b_zero = 20.0
s_b = 2.0

a = a_zero + s_a * np.random.randn(N)
b = b_zero + s_b * np.random.randn(N)

# Não irei plotar as distribuições de a e b.

z = a / b  # Divisãoo elemento a elemento

mean_z = np.mean(z)
stdev_z = np.std(z)
stdev_zm = stdev_z / np.sqrt(N)

plot_hist(z, '3) Valores de z "medidos"', mean_z, stdev_z)

z_value = f'{round(mean_z, 5)} ± {round(stdev_zm, 5)}'

print('-' * 20)
print('Resultados 3) a)')
print('Valor de z médio:', z_value)
print('Incerteza de z:', stdev_z)
print('-' * 20)

# b)

a_zero = 10.0
s_a = 2.0

b_zero = 20.0
s_b = 0

a = a_zero + s_a * np.random.randn(N)
b = b_zero + s_b * np.random.randn(N)

# Não irei plotar as distribuições de a e b.

z = a / b  # Divisãoo elemento a elemento

mean_z = np.mean(z)
stdev_z = np.std(z)
stdev_zm = stdev_z / np.sqrt(N)

plot_hist(z, '3) Valores de z "medidos" com b fixo', mean_z, stdev_z)

z_value = f'{round(mean_z, 5)} ± {round(stdev_zm, 5)}'

print('-' * 20)
print('Resultados 3) b)')
print('Valor de z médio:', z_value)
print('Incerteza de z:', stdev_z)
print('-' * 20)

# c)

a_zero = 10.0
s_a = 0

b_zero = 20.0
s_b = 2.0

a = a_zero + s_a * np.random.randn(N)
b = b_zero + s_b * np.random.randn(N)

# Não irei plotar as distribuições de a e b.

z = a / b  # Divisãoo elemento a elemento

mean_z = np.mean(z)
stdev_z = np.std(z)
stdev_zm = stdev_z / np.sqrt(N)

plot_hist(z, '3) Valores de z "medidos" com a fixo', mean_z, stdev_z)

z_value = f'{round(mean_z, 5)} ± {round(stdev_zm, 5)}'

print('-' * 20)
print('Resultados 3) c)')
print('Valor de z médio:', z_value)
print('Incerteza de z:', stdev_z)
print('-' * 20)

"""
4) Calcule as incertezas de todas as questões usando a Lei Geral de Propagação de Incertezas
e compare-as com as estimativas obtidas por “Toy Monte Carlo”. Indique os casos em que há
diferenças importantes.
"""

s_r = 1
s_d = 1
s_a = 2
s_b = 2

dx_dr = 2*np.pi*r_zero
s_x = abs(dx_dr) * s_r

dy_dd = 3*(d_zero**2)
s_y = abs(dy_dd) * s_d

dz_da = 1/b_zero
dz_db = -(a_zero/(b_zero**2))

s_z_a = abs(dz_da) * s_a
s_z_b = abs(dz_db) * s_b

s_z = np.sqrt(s_z_a**2 + s_z_b**2)


print('-'*20)
print('Resultados da 4)')
print('Valor de s_x:', round(s_x, 5))
print('Valor de s_y:', round(s_y, 5))
print('Valor de s_z_a:', round(s_z_a, 5))
print('Valor de s_z_b:', round(s_z_b, 5))
print('Valor de s_z:', round(s_z, 5))
