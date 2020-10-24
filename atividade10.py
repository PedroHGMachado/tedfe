import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class ProbabilityDensity(object):

    def __init__(self, func, domain: tuple, max_value: float):

        self.domain = domain
        self.max_value = max_value
        self.func = func


def metodo_exclusao(prob_density, N=1):
    """
    Gera um vetor de N elementos
    """

    xmin, xmax = prob_density.domain
    ymax = prob_density.max_value

    f = prob_density.func

    i = 0
    x = np.zeros(N)
    while i < N:
        # gera um possivel x com distribuicao uniforme entre xmim e mxmax
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        # gera um valor de y para comparacao com a PDF no ponto x gerado
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1

    return x


def show_results(results):

    print(f'Média: {np.mean(results)}')
    print(f'Std: {np.std(results, ddof=1)}')

    summup_list = []
    for l in [1, 1.5, 2, 2.5, 3]:
        summup = sum(abs(results) <= (l * np.std(results, ddof=1)))
        summup_list.append(summup)
        print(f'lambda = {l} => sum = {summup}')


    plt.hist(results, bins=30)
    plt.show()
    return summup_list


def sum_n_results(n=1):

    max_value = 3 / 2
    domain = (-1, 1)
    func = lambda x: max_value * (x ** 2)

    if n == 'inf':

        results_sum = np.random.randn(10000)

    else:

        pd_func_atv10 = ProbabilityDensity(func, domain, max_value)

        results_sum = 0
        for i in range(n):
            results = metodo_exclusao(pd_func_atv10, N=10000)
            results_sum += results

    final_results = show_results(results_sum)

    return final_results


n_sums = [1, 2, 3, 5, 10, 100, 'inf']
table = pd.DataFrame()

for n_sum in n_sums:

    final_results_n = sum_n_results(n_sum)

    table[f'M={n_sum}'] = final_results_n

table.to_csv('atividade_10_tabela.csv', header=False, index=False)