import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def round_to_significatives(number, algs=2):
    ten_factor = 0
    while number * (10 ** ten_factor) // 1 == 0:
        ten_factor += 1

    n_decimals = ten_factor + (algs - 1)

    return round(number, n_decimals), n_decimals


def calculate_n(case, table):
    total = len(table)

    if case == 'home':
        nx = np.sum(table.HG > table.AG)
    elif case == 'away':
        nx = np.sum(table.HG < table.AG)
    elif case == 'draw':
        nx = np.sum(table.HG == table.AG)
    else:
        raise ValueError(f'Case "{case}" not supported!')

    fx = nx / total
    sigma_nx = np.sqrt(total * fx * (1 - fx))
    sigma_fx = sigma_nx / total
    signf_sigma_fx, n_decs = round_to_significatives(sigma_fx)

    print(f"n-{case}: {nx} ± {round(sigma_nx)} | "
          f"f-{case}: {round(fx, n_decs)} ± {signf_sigma_fx}\n")

    return nx, sigma_nx, fx, sigma_fx


def binomial(total, fx, nx):
    total_fact = np.math.factorial(total)
    nx_fact = np.math.factorial(nx)
    total_nx_fact = np.math.factorial(total - nx)

    factorial_term = total_fact / (nx_fact * total_nx_fact)
    probs_term = (fx ** nx) * ((1 - fx) ** (total - nx))

    return factorial_term * probs_term


eua_table = pd.read_excel("new_leagues_data.xlsx", "USA")
eua_table_tfev = eua_table[eua_table.Date <= "2020-02-29"]

min_date = eua_table_tfev.Date.min()
max_date = eua_table_tfev.Date.max()
N = len(eua_table_tfev)
print(f'Considerando N = {N} registros de {min_date} até {max_date}')

print("-" * 20, "HOME", "-" * 20)
nh, sigma_nh, fh, sigma_fh = calculate_n('home', eua_table_tfev)
print("-" * 20, "AWAY", "-" * 20)
na, sigma_na, fa, sigma_fa = calculate_n('away', eua_table_tfev)
print("-" * 20, "DRAW", "-" * 20)
nd, sigma_nd, fd, sigma_fd = calculate_n('draw', eua_table_tfev)

assert ((nh + na + nd) == N)

n_holiday_games = 10


def bin_draw_pf(x): return binomial(n_holiday_games, fd, x)


n_draws = np.arange(0, n_holiday_games + 1)
probability = np.array([bin_draw_pf(nx) for nx in n_draws])

plt.xlabel('Número de Empates')
plt.ylabel('Probabilidade')
plt.title('Probabilidade de "n" Empates nos Jogos do Feriado.')
plt.plot(n_draws, probability, 'ro')
plt.show()

draw_pf = dict(zip(n_draws, probability))

print("PROBABILIDADE DE EMPATES")
print("P(n <= 2):", round(sum([p for n, p in draw_pf.items() if n <= 2]), 5))
print("P(n = 10):", round(draw_pf[10], 5))
