import numpy as np

N = 100
N_rep = 10000

x_zero = 50 # metros
sigma_zero = 1 # metro

xs = x_zero + sigma_zero * np.random.randn(N_rep * N).reshape((N_rep, N))

xs_m = np.mean(xs, axis=1, keepdims=True)
xs_M = np.median(xs, axis=1, keepdims=True)
sigma_xs = np.std(xs, ddof=1, axis=1, keepdims=True)

ns = np.sum(abs(xs - x_zero) - sigma_zero <= 0, axis=1)
ms = np.sum(abs(xs - xs_m) - sigma_xs <= 0, axis=1)

desv_m = np.std(xs_m, ddof=1)
desv_M = np.std(xs_M, ddof=1)

z = (xs_m + xs_M)/2

desv_z = np.std(z)

mean_n = np.mean(ns)
desv_n_mean = np.std(ns, ddof=1)/(np.sqrt(len(ns)))

mean_m = np.mean(ms)
desv_m_mean = np.std(ms, ddof=1)/(np.sqrt(len(ms)))

p = 0.6826
real_desv_n_mean = np.sqrt(N*p*(1 - p))/N


desv_n = np.std(ns, ddof=1)
desv_m = np.std(ms, ddof=1)
real_desv_n = np.sqrt(N*p*(1 - p))
