"""
Disciplina: Tratamento Estatístico de Dados em Física Experimental
Atividade: 05
Author: pedro.machado
"""

import numpy as np
import matplotlib.pyplot as plt


def print_result(vm, s_vm, s_v, num_s_v, num_2s_v, num_3s_v, letter='v', n_exercise=None):

    print(f"Exercício {n_exercise}")
    text = f"{n_exercise}.1) {letter}𝑚 = {vm} ± {s_vm}\n"\
           f"{n_exercise}.2) 𝜎{letter} = {s_v}\n"\
           f"{n_exercise}.3) entre {letter}𝑚 − 𝜎{letter} e {letter}𝑚 + 𝜎{letter} = {num_s_v}\n" \
           f"{n_exercise}.4) entre {letter}𝑚 − 2𝜎{letter} e {letter}𝑚 + 2𝜎{letter} = {num_2s_v}\n" \
           f"{n_exercise}.4) entre {letter}𝑚 − 3𝜎{letter} e {letter}𝑚 + 2𝜎{letter} = {num_3s_v}\n" \
    
    print(text)


"""
1) Gere 𝑁 = 10.000 dados 𝑥 com distribuição gaussiana com valor
verdadeiro 𝑥0 = 0 e desvio-padrão (verdadeiro) 𝜎0 = 1.
Em seguida, calcule:
1.1) O valor médio de 𝑥, 𝑥𝑚, e sua correspondente incerteza, 𝜎𝑥𝑚;
1.2) O desvio-padrão amostral de 𝑥, 𝜎𝑥;
1.3) O número de dados 𝑥 no intervalo entre 𝑥𝑚 − 𝜎𝑥 e 𝑥𝑚 + 𝜎𝑥;
1.4) O número de dados 𝑥 no intervalo entre 𝑥𝑚 − 2𝜎𝑥 e 𝑥𝑚 + 2𝜎𝑥;
1.5) O número de dados 𝑥 no intervalo entre 𝑥𝑚 − 3𝜎𝑥 e 𝑥𝑚 + 3𝜎𝑥;
"""

N = int(1e4)
x = np.random.randn(N)

# 1.1
xm = np.mean(x)
s_xm = np.std(x, ddof=1) / np.sqrt(N)

# 1.2
s_x = np.std(x, ddof=1)

# 1.3
num_s_x = np.sum(np.abs(x - xm) <= s_x)

# 1.4
num_2s_x = np.sum(np.abs(x - xm) <= 2*s_x)

# 1.5
num_3s_x = np.sum(np.abs(x - xm) <= 3*s_x)

print_result(xm, s_xm, s_x, num_s_x, num_2s_x, num_3s_x, letter='x', n_exercise=1)

plt.hist(x, bins=30)
plt.show()

"""
2) Gere 𝑁 = 10.000 dados 𝑦 com distribuição uniforme no intervalo entre -0,5 e +0,5
[no Octave, isso pode ser conseguido com o comando y = -0.5 + rand(1e4,1),
onde se usa rand (e não randn) porque os dados têm distribuição uniforme].
Em seguida, calcule:
2.1) O valor médio de 𝑦, 𝑦𝑚, e sua correspondente incerteza, 𝜎𝑦𝑚;
2.2) O desvio-padrão amostral de 𝑦, 𝜎𝑦;
2.3) O número de dados 𝑦 no intervalo entre 𝑦𝑚 − 𝜎𝑦 e 𝑦𝑚 + 𝜎𝑦;
2.4) O número de dados 𝑦 no intervalo entre 𝑦𝑚 − 2𝜎𝑦 e 𝑦𝑚 + 2𝜎𝑦;
2.5) O número de dados 𝑦 no intervalo entre 𝑦𝑚 − 3𝜎𝑦 e 𝑦𝑚 + 3𝜎𝑦;
"""

N = int(1e4)
y = -0.5 + np.random.rand(N)

# 1.1
ym = np.mean(y)
s_ym = np.std(y, ddof=1) / np.sqrt(N)

# 1.2
s_y = np.std(y, ddof=1)

# 1.3
num_s_y = np.sum(np.abs(y - ym) <= s_y)

# 1.4
num_2s_y = np.sum(np.abs(y - ym) <= 2*s_y)

# 1.5
num_3s_y = np.sum(np.abs(y - ym) <= 3*s_y)

print_result(ym, s_ym, s_y, num_s_y, num_2s_y, num_3s_y, letter='y', n_exercise=2)


plt.hist(y, bins=30)
plt.show()

"""
3) Gere 𝑁 = 10.000 dados 𝑧 com distribuição triangular no intervalo entre -1 e +1 a partir da
soma de dois dados com distribuição uniforme no intervalo entre -0.5 e +0.5 (isto é, cada 
valor de 𝑧 pode ser gerado como a soma de dois valores gerados como no exercício anterior
[no Octave, z = -1 + rand(1e4,1) + rand(1e4,1)]).
Em seguida, calcule:
3.1) O valor médio de 𝑧, 𝑧𝑚, e sua correspondente incerteza, 𝜎𝑧𝑚;
3.2) O desvio-padrão amostral de 𝑧, 𝜎𝑧;
3.3) O número de dados 𝑧 no intervalo entre 𝑧𝑚 − 𝜎𝑧 e 𝑧𝑚 + 𝜎𝑧;
3.4) O número de dados 𝑧 no intervalo entre 𝑧𝑚 − 2𝜎𝑧 e 𝑧𝑚 + 2𝜎𝑧;
3.5) O número de dados 𝑧 no intervalo entre 𝑧𝑚 − 3𝜎𝑧 e 𝑧𝑚 + 3𝜎𝑧;
"""

N = int(1e4)
z = -1 + np.random.rand(N) + np.random.rand(N)

# 1.1
zm = np.mean(z)
s_zm = np.std(z, ddof=1) / np.sqrt(N)

# 1.2
s_z = np.std(z, ddof=1)

# 1.3
num_s_z = np.sum(np.abs(z - zm) <= s_z)

# 1.4
num_2s_z = np.sum(np.abs(z - zm) <= 2*s_z)

# 1.5
num_3s_z = np.sum(np.abs(z - zm) <= 3*s_z)

print_result(zm, s_zm, s_z, num_s_z, num_2s_z, num_3s_z, letter='z', n_exercise=3)

plt.hist(z, bins=30)
plt.show()
