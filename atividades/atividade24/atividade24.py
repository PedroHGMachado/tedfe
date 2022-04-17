import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def _mmq(y, gs, sigs):

    D = (1/np.power(sigs, 2)) * np.dot(y, gs.T)

    M = (1/np.power(sigs, 2)) * np.dot(gs, gs.T)

    covariance_matrix = np.linalg.inv(M)

    adjusted_params = np.dot(covariance_matrix, D)

    chi_square = np.sum(np.power((1/sigs)*(y - np.dot(adjusted_params.T, gs)), 2))

    degrees_of_freedom = gs.shape[1] - gs.shape[0]

    return adjusted_params, covariance_matrix, chi_square, degrees_of_freedom

fig, ax = plt.subplots(2, figsize=(20, 15))

data = pd.read_csv('dados_osciloscópio.tsv', sep='\t')
y = data['Tensão (V)']
t = data['Tempo (s)']
sigma_y = 0.06 #V

ax[0].errorbar(t, y, yerr=[sigma_y]*len(y), fmt='b-')

f = 2 #Hz

g1 = np.cos(2*np.pi*f*t)
g2 = np.sin(2*np.pi*f*t)

gs = np.array([g1, g2])

params, cov_mat, chi, ngl = _mmq(y, gs, sigma_y)

a1 = params[0]
a2 = params[1]

sigma_a1 = np.sqrt(cov_mat[0,0])
sigma_a2 = np.sqrt(cov_mat[1,1])

covariance = cov_mat[0,1]
correlation = covariance/(sigma_a1*sigma_a2)

A = np.sqrt(np.power(a1, 2) + np.power(a2, 2))

da1 = a1*sigma_a1/A
da2 = a1*sigma_a2/A

sigma_A = np.sqrt( np.power(da1, 2) + np.power(da2, 2) + 2*da1*da2*covariance)

F_t = a1*np.cos(2*np.pi*f*t) + a2*np.sin(2*np.pi*f*t)

sigma_F = np.sqrt(np.power(np.cos(2*np.pi*f*t)*sigma_a1, 2) + np.power(np.sin(2*np.pi*f*t)*sigma_a2, 2))

ax[0].errorbar(t, F_t, yerr=sigma_F, fmt='r-')

sigma_R = np.sqrt(sigma_y**2 + (sigma_F)**2)

ax[1].plot(t, y - F_t, 'o')
ax[1].axhline(y=0, c='black')

plt.show()