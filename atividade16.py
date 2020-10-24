import matplotlib.pyplot as plt
import numpy as np

# Funções Auxiliares


def round_to_significatives(number, algs=2):
    ten_factor = 0
    while number * (10 ** ten_factor) // 1 == 0:
        ten_factor += 1

    n_decimals = ten_factor + (algs - 1)

    return round(number, n_decimals), n_decimals


def measure_value(v_zero, sigma_v, M, N_times=1):
    v = (v_zero + np.random.randn(N_times * M) * sigma_v)
    v = v.reshape((N_times, M))
    v = v.mean(axis=0)

    return v


def print_result(n_exercise, final_value):

    fv_mean = np.mean(final_value)
    sigma_fv = np.std(final_value, ddof=1)
    sigma_fvm = sigma_fv / np.sqrt(len(final_value))

    sigma_fvm_rounded, ndecs = round_to_significatives(sigma_fvm)
    sigma_fv_rounded = round(sigma_fv, ndecs)
    fv_mean_rounded = round(fv_mean, ndecs)

    str_mean_fv = f'{fv_mean_rounded}({int(sigma_fvm_rounded * (10 ** ndecs))})'

    print('-' * 100)
    print(f'Resultado do Exercício [{n_exercise}]')
    print(f'Média de W: {str_mean_fv}')
    print(f'Desvio Padrão de W: {sigma_fv_rounded}')
    print('-' * 100)

    return str_mean_fv, sigma_fv_rounded


# Dados do Exercício

M = 10000

x_zero = 15
sigma_x = 2

y_zero = 40
sigma_y = 3

# Início da atividade 1)a)

x = measure_value(x_zero, sigma_x, M)
y = measure_value(y_zero, sigma_y, M)

print_result('1)a)', x*y)

# Início da atividade 1)b)

# b.1)

x = measure_value(x_zero, sigma_x, M, N_times=2)
y = measure_value(y_zero, sigma_y, M)

print_result('1)b.1)', x*y)

# b.2)

x = measure_value(x_zero, sigma_x, M)
y = measure_value(y_zero, sigma_y, M, N_times=2)

print_result('1)b.2)', x*y)

# c)

N_times_max = 11

sigmas_ws = []

for Nx in range(1, N_times_max):
    Ny = N_times_max - Nx
    x = measure_value(x_zero, sigma_x, M, N_times=Nx)
    y = measure_value(y_zero, sigma_y, M, N_times=Ny)
    w = x*y

    mean_w, sigma_w = print_result(f'1)c) => Nx = {Nx} e Ny = {Ny}', w)
    sigmas_ws.append(sigma_w)

print('Sigmas Ws')
print(sigmas_ws)
