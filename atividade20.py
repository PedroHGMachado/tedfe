import numpy as np

N = 100
N_rep = 10000

x_zero = 50 # metros
sigma_zero = 1 # metro

xs = x_zero + sigma_zero * np.random.randn(N_rep * N).reshape((N_rep, N))

xs_m = np.mean(xs, axis=1, keepdims=True)
xs_M = np.median(xs, axis=1, keepdims=True)
sigma_xs = np.std(xs, ddof=1, axis=1, keepdims=True)

xs_m_mean = np.mean(xs_m)
desv_m = np.std(xs_m, ddof=1)
desv_m_mean = desv_m/np.sqrt(N_rep)
print(f'm_mean = {xs_m_mean} # {desv_m_mean}')

xs_M_mean = np.mean(xs_M)
desv_M = np.std(xs_M, ddof=1)
desv_M_mean = desv_M/np.sqrt(N_rep)
print(f'M_mean = {xs_M_mean} # {desv_M_mean}')


print('a.1.1) Desvio-padrão amostrais das médias, s_xm.')
print(f'\t s_xm = {desv_m}')

print('a.1.2) Desvio-padrão amostrais das medianas, s_xM.')
print(f'\t s_xM = {desv_M}')


ns = np.sum(abs(xs - x_zero) - sigma_zero <= 0, axis=1)
ms = np.sum(abs(xs - xs_m) - sigma_xs <= 0, axis=1)

z = (xs_m + xs_M)/2

z_mean = np.mean(z)
desv_z = np.std(z)
desv_z_mean = desv_z/np.sqrt(N_rep)
print(f'z_mean = {z_mean} # {desv_z_mean}')

print('a.2) Desvio-padrão amostral de z, s_z.')
print(f'\t s_z = {desv_z}')

print('b.1.1) Valor médio de n com sua incerteza.')
mean_n = np.mean(ns)
desv_n_mean = np.std(ns, ddof=1)/(np.sqrt(len(ns)))
print(f'\t n = {mean_n} # {desv_n_mean}')

print('b.1.2) Valor médio de m com sua incerteza.')
mean_m = np.mean(ms)
desv_m_mean = np.std(ms, ddof=1)/(np.sqrt(len(ms)))
print(f'\t m = {mean_m} # {desv_m_mean}')


print('b.2) Usando seus conhecimentos sobre binomial, calcule o valor esperado para o número de sucessos em N tentativas'
      ' independentes com probabilidade individual de sucesso, p =0,6826 (correspondente à integral da gaussiana padrão '
      'entre -1 e +1).')
p = 0.6826
n_zero = N*p
print(f'\t n_zero = {n_zero}')

print('b.3.1) Desvio-padrão amostral de n.')
desv_n = np.std(ns, ddof=1)
print(f'\t desv_n = {desv_n}')

print('b.3.2) Desvio-padrão amostral de m.')
desv_m = np.std(ms, ddof=1)
print(f'\t desv_m = {desv_m}')

print('b.4) Usando seus conhecimentos sobre binomial, calcule o valor esperado para o desvio-padrão do número de '
      'sucessos em N tentativas independentes com probabilidade individual de sucesso, p =0,6826.')
real_desv_n = np.sqrt(N*p*(1 - p))
print(f'\t desv_n_zero = {real_desv_n}')
