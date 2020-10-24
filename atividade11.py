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


def metodo_inversao(N=1):
    """
    Gera um vetor de N elementos
    """

    # PDF do exemplo do roteiro: f(x) = 2 * x com x entre 0 e 1
    #  para a qual, g(x)=x^2, cuja inversa eh x(g)=sqrt(g)
    inv_g = lambda g: ((g*125)**(1/3))

    # gera N valores de g com distribuicao uniforme entre 0 e 1
    g = np.random.rand(N)
    # calcula os valores de x correspondentes
    x = inv_g(g)

    return x


def show_results(results):

    print(f'Média: {np.mean(results)}')
    print(f'Std: {np.std(results, ddof=1)}')

    total = 0
    for a in range(5):
        b = a + 1
        n = np.sum((results >= a) & (results < b))
        total += n
        print(f'[{a},{b}[ => n = {n}')

    print(f'total = {total}')

    plt.hist(results, bins= np.arange(5))
    plt.show()

print("Atividade 11")

int_pdf11 = lambda inter: (1/125)*(inter[1]**3 - inter[0]**3)

for a in range(5):
    b = a + 1
    integral = int_pdf11((a, b))
    n = 200 * integral
    print(f'integral: {integral} | n: {n}')

for i in range(3):
    print(f'Valores para coluna ({i+3}) -----------------------')

    xs = metodo_inversao(N=200)
    show_results(xs)

    print('-----------------------------------------------')


bigN = 10000
print(f'Gerando {bigN} simulações!')
bigxs = np.array([metodo_inversao(N=200) for i in range(bigN)])
print(f'Contabilizando as {bigN} simulações ebtre intervalos!')
bigns = np.array([[np.sum((row >= a) & (row < (a + 1))) for a in range(5)] for row in bigxs])

n_means = np.mean(bigns, axis=0)
n_stds = np.std(bigns, axis=0, ddof=1)
n_stds_means = n_stds/np.sqrt(bigN)

for a in range(5):
    b = a + 1
    print(f'Intervalo [{a}, {b}[ => ñ = {round(n_means[a],3)} +- {round(n_stds_means[a], 3)} | '
          f'sn = {round(n_stds[a], 3)}')