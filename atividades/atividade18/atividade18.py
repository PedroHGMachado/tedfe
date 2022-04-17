import matplotlib.pyplot as plt
import numpy as np

a_zero = 30
b_zero = 20

sigma_a = 2
sigma_b = 2

N = 500

print('Exercício A')
rho = 0.75

r1 = np.random.randn(N)
r2 = np.random.randn(N)

a = a_zero + sigma_a*r1
b = b_zero + sigma_b*(rho*r1 + np.sqrt(1 - rho**2)*r2)

plt.plot(a, b, 'rx')
plt.title('ρ = 0.75')
plt.xlabel('a')
plt.ylabel('b')
plt.show()

error_a = a - a_zero
error_b = b - b_zero

n_sinal = np.sum(error_a*error_b > 0)
sigma_n_sinal = np.sqrt(n_sinal*(N - n_sinal)/N)
print('n:', n_sinal, '#', sigma_n_sinal)


f = n_sinal/N
sigma_f = sigma_n_sinal/N
print('f:', f, '#', sigma_f)

a_m = np.mean(a)
b_m = np.mean(b)

Sa = np.std(a, ddof=1)
Sb = np.std(b, ddof=1)

V_ab = (1/(N-1))*np.sum((a - a_m)*(b - b_m))
R = V_ab/(Sa*Sb)

incV = Sa*Sb*np.sqrt(((1 + R**2)/(N - 1)))
incR = (1 - R**2)/(np.sqrt(N-1))

print('V_ab:', V_ab, '#', incV)
print('R:', R, '#', incR)

w = a + b
Sw = np.std(w, ddof=1)
incSw = Sw/(np.sqrt(2*(N-1)))
print('Sw:', Sw, '#', incSw)

z = a - b
Sz = np.std(z, ddof=1)
incSz = Sz/(np.sqrt(2*(N-1)))
print('Sz:', Sz, '#', incSz)

print('-'*100)


print('Exercício B')
rho = -0.75

r1 = np.random.randn(N)
r2 = np.random.randn(N)

a = a_zero + sigma_a*r1
b = b_zero + sigma_b*(rho*r1 + np.sqrt(1 - rho**2)*r2)

plt.plot(a, b, 'g^')
plt.title('ρ = -0.75')
plt.xlabel('a')
plt.ylabel('b')
plt.show()

error_a = a - a_zero
error_b = b - b_zero

n_sinal = np.sum(error_a*error_b > 0)
sigma_n_sinal = np.sqrt(n_sinal*(N - n_sinal)/N)
print('n:', n_sinal, '#', sigma_n_sinal)


f = n_sinal/N
sigma_f = sigma_n_sinal/N
print('f:', f, '#', sigma_f)

a_m = np.mean(a)
b_m = np.mean(b)

Sa = np.std(a, ddof=1)
Sb = np.std(b, ddof=1)

V_ab = (1/(N-1))*np.sum((a - a_m)*(b - b_m))
R = V_ab/(Sa*Sb)

incV = Sa*Sb*np.sqrt(((1 + R**2)/(N - 1)))
incR = (1 - R**2)/(np.sqrt(N-1))

print('V_ab:', V_ab, '#', incV)
print('R:', R, '#', incR)

w = a + b
Sw = np.std(w, ddof=1)
incSw = Sw/(np.sqrt(2*(N-1)))
print('Sw:', Sw, '#', incSw)

z = a - b
Sz = np.std(z, ddof=1)
incSz = Sz/(np.sqrt(2*(N-1)))
print('Sz:', Sz, '#', incSz)


fig, ax = plt.subplots(5, figsize=(15/3,10*5/3))

for i, rho in enumerate([0, -0.25, 0.5, -0.9, 0.95]):

    r1 = np.random.randn(N)
    r2 = np.random.randn(N)

    a = a_zero + sigma_a * r1
    b = b_zero + sigma_b * (rho * r1 + np.sqrt(1 - rho ** 2) * r2)

    ax[i].plot(a, b, 'o')
    ax[i].set_title(f'ρ = {rho}')
    ax[i].set_xlabel('a')
    ax[i].set_ylabel('b')

plt.show()
