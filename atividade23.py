import numpy as np

def _mmq(y, gs, sigs):

    D = (1/np.power(sigs, 2)) * np.dot(y, gs.T)

    M = (1/np.power(sigs, 2)) * np.dot(gs, gs.T)

    covariance_matrix = np.linalg.inv(M)

    adjusted_params = np.dot(covariance_matrix, D)

    chi_square = np.sum(np.power((1/sigs)*(y - np.dot(adjusted_params.T, gs)), 2))

    degrees_of_freedom = gs.shape[1] - gs.shape[0]

    return adjusted_params, covariance_matrix, chi_square, degrees_of_freedom

# Exemplo da aula! Validado :)
# y = np.array([42.4, 28, 34.3, 36.5, 29.5])
#
# g1 = np.array([120.3, 195.1, 10.2, 320.9, 110.6])
# g2 = np.array([451.6, 115.3, 523.5, 54.2, 277.4])
#
# gs = np.array([g1, g2])
#
# _mmq(y, gs, 0.5)

# Atividade 24
for case in [0, 3]:

    print(f"CASO X = T - {case}")

    y = np.array([1.7, 3.0, 4.2, 4.8, 5.4])
    sig = 0.2

    t = np.array([1, 2, 3, 4, 5]) - case

    g1 = np.power(t, 0)
    g2 = np.power(t, 1)

    gs = np.array([g1, g2])

    params, cov_mat, chi_sqr, dgs = _mmq(y, gs, sig)

    sigmas = np.sqrt(np.diag(cov_mat))

    print("Parâmetros")
    print(f"a = {params[0]} +- {sigmas[0]}")
    print(f"b = {params[1]} +- {sigmas[1]}")

    print('Matriz de covariâncias')
    print(cov_mat)

    covariance = cov_mat[0,1]
    covariance_relation = covariance / np.prod(sigmas)

    print(f"Covariância = {covariance} => relação = {covariance_relation}")

    print(f"Chi^2 = {chi_sqr} & NGL = {dgs}")

    for ti in [1.5, 6]:
        tif = ti - case
        h = params[0] + params[1]*tif
        sigma_ti = np.sqrt(np.power(sigmas[0], 2) + np.power(sigmas[1]*tif, 2) + 2*tif*covariance)
        print(f'h({ti}) = {h} +- {sigma_ti}')

    print('-'*200)
    print('-'*200)