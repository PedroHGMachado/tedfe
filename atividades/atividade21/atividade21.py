import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


x_zero = 0
sigma_zero = 1

M = 10000
Ns = [2, 3, 4, 5, 10, 50, 100]

N_data = {}
for N in Ns:

    xs = (x_zero + sigma_zero*np.random.randn(M*N)).reshape((N, M))

    sigma_xs = np.std(xs, axis=0, ddof=1)
    var_xs = sigma_xs**2

    s_m = np.mean(sigma_xs)
    s_s = np.std(sigma_xs, ddof=1)

    s_sm = s_s/ np.sqrt(len(sigma_xs))

    v_m = np.mean(var_xs)
    s_v = np.std(var_xs, ddof=1)

    s_vm = s_v / np.sqrt(len(var_xs))

    n_s = np.sum(sigma_xs < sigma_zero)
    n_v = np.sum(var_xs < sigma_zero**2)

    s_ns = np.sqrt((n_s/M)*(M - n_s))
    s_nv = np.sqrt((n_v/M)*(M - n_v))


    N_data[N] = {'s_xs': sigma_xs, 's_s': s_s,
                 'v_xs': var_xs, 's_v': s_v,
                 's_m': s_m, 's_sm': s_sm,
                 'v_m': v_m, 's_vm': s_vm,
                 'n_s': n_s, 's_ns': s_ns,
                 'n_v': n_v, 's_nv': s_nv}


plot_Ns = Ns
fig, ax = plt.subplots(len(plot_Ns), 1, figsize = (10,(25/7)*len(plot_Ns)), sharex=True)
plot_kwargs = {'bins': 60, 'alpha': 0.7}

for i, N in enumerate(plot_Ns):

    label_s = '$\sigma$'
    label_v = '$V$'

    label_sm = '$\sigma_m$'
    label_vm = '$V_m$'

    label_ss = '$\sigma_m ± \sigma_{\sigma}$'
    label_sv = '$\sigma_v ± \sigma_{V}$'

    s = N_data[N]['s_xs']
    v = N_data[N]['v_xs']

    s_m = N_data[N]['s_m']
    v_m = N_data[N]['v_m']

    s_s = N_data[N]['s_s']
    s_v = N_data[N]['s_v']

    n_s = N_data[N]['n_s']
    n_v = N_data[N]['n_v']

    s_ns = N_data[N]['s_ns']
    s_nv = N_data[N]['s_nv']


    vhist, _, _ = ax[i].hist(v, color='red', label=label_v, **plot_kwargs)
    shist, _, _ = ax[i].hist(s, color='blue', label=label_s, **plot_kwargs)

    ax[i].axvline(v_m, color='red', label=label_vm)
    ax[i].axvline(s_m, color='blue', label=label_sm)

    ax[i].axvline(s_m + s_s, color='green',  label=label_ss, linestyle='--')
    ax[i].axvline(s_m - s_s, color='green', linestyle='--')
    ax[i].axvspan(s_m - s_s, s_m + s_s, alpha=0.2, color='green')

    ax[i].axvline(v_m + s_v, color='orange',  label=label_ss, linestyle='--')
    ax[i].axvline(v_m - s_v, color='orange', linestyle='--')
    ax[i].axvspan(v_m - s_v, v_m + s_v, alpha=0.2, color='orange')

    s = f'$\sigma < \sigma_0 = {n_s}({round(s_ns)})$\n'\
        f'$V < \sigma_0^{{2}} = {n_v}({round(s_nv)})$'

    ax[i].text(5, 0.8*max(max(vhist), max(shist)), s=s)

    ax[i].legend()
    ax[i].set_title(f'Histograma N={N}')
    ax[i].set_xlabel('Valor')
    ax[i].set_ylabel('Contagens')



ax[i].set_xlim([0,7])

plt.show()

table = pd.DataFrame(N_data)
table = table.drop(['s_xs', 'v_xs'])
table.to_excel('atividade21_tabela.xlsx')