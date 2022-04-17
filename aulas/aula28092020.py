import matplotlib.pyplot as plt
import numpy as np

def metodo_exclusao(G, N=1):
    """
    Gera um vetor de N elementos
    """

    xmin = -1
    xmax = 1
    ymax = (G + 1)/(2*G)

    f = lambda x : ymax*(1 - abs(x)**G)

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
    inv_g = lambda g: np.sqrt(g)

    # gera N valores de g com distribuicao uniforme entre 0 e 1
    g = np.random.rand(N)
    # calcula os valores de x correspondentes
    x = inv_g(g)

    return x


def show_results(results):
    print(f'Média: {np.mean(results)}')
    print(f'Std: {np.std(results, ddof=1)}')
    plt.hist(results, bins=20)
    plt.show()