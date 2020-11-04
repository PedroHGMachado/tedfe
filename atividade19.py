import matplotlib.pyplot as plt
import numpy as np

print('-'*100)
print('Exercício 1')
N = 1000

rx = np.random.randn(N)
ry = np.random.randn(N)
rc = np.random.randn(N)

sigma_c = 4
sigma_l = 3

x_zero = 110
y_zero = 100

erro_c = sigma_c*rc

x = x_zero + sigma_l*rx + erro_c
y = y_zero + sigma_l*ry + erro_c

plt.plot(x, y, 'o')
plt.title('Erro de calibração erro_c=4')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

error_x = x - x_zero
error_y = y - y_zero

n_sinal = np.sum(error_x*error_y > 0)
sigma_n_sinal = np.sqrt(n_sinal*(N - n_sinal)/N)
print('n_sinal:', n_sinal, '#', sigma_n_sinal)

f = n_sinal/N
sigma_f = sigma_n_sinal/N
print('f:', f, '#', sigma_f)

x_m = np.mean(x)
y_m = np.mean(y)

Sx = np.std(x, ddof=1)
Sy = np.std(y, ddof=1)

V_xy = (1/(N-1))*np.sum((x - x_m)*(y - y_m))
R = V_xy/(Sx*Sy)

incV = Sx*Sy*np.sqrt(((1 + R**2)/(N - 1)))
incR = (1 - R**2)/(np.sqrt(N-1))

print('V_xy:', V_xy, '#', incV)
print('R:', R, '#', incR)

w = x + y
Sw = np.std(w, ddof=1)
incSw = Sw/(np.sqrt(2*(N-1)))
print('Sw:', Sw, '#', incSw)

z = x - y
Sz = np.std(z, ddof=1)
incSz = Sz/(np.sqrt(2*(N-1)))
print('Sz:', Sz, '#', incSz)

sigma_w_pe = np.sqrt(2*(sigma_c**2 + sigma_l**2))
print('Propagação de Erros => Sw = Sz:', sigma_w_pe)

print('-'*100)

print('-'*100)
print('Exercício 2')

M = 10000
N = 25

d_zero = 200

sigma_s = 4
sigma_a = 3

erro_s = (np.random.randn(M)*sigma_s).reshape((M, 1))

erro_a = (np.random.randn(M*N)*sigma_a).reshape((M, N))

d = np.zeros((M, N)) + d_zero + erro_a + erro_s

d_m = np.mean(d, axis=1)

S_dm = np.std(d_m, ddof=1)
IncSdm = S_dm/(np.sqrt(2*(M - 1)))
print('S_dm:', S_dm, '#', IncSdm)