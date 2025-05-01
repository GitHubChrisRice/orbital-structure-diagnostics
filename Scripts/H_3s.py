import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def rho_3s(r):
    psi = (1 / (81 * np.sqrt(3 * np.pi))) * (27 - 18*r + 2*r**2) * np.exp(-r/3)
    return psi**2

def integrand_3s(r, s):
    return rho_3s(r) * r**(2 - s) * 4 * np.pi

def compute_S_3s(L, s):
    result, _ = quad(lambda r: integrand_3s(r, s), 0, L, limit=100)
    return result

L_vals = np.linspace(0.1, 10, 20)
s = 1.0
S_vals = [compute_S_3s(L, s) for L in L_vals]

plt.plot(L_vals, S_vals, marker='o', color='green')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{S}_{3s}(L; 1.0)$')
plt.title('Hydrogen 3s Orbital (Summation)')
plt.grid(True)
plt.show()
