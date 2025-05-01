import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Z1 = 2.69
Z2 = 1.28
A1 = 2.0  # 2 core electrons
A2 = 0.5  # 1 outer electron

def rho_Li(r):
    return A1 * np.exp(-2 * Z1 * r) + A2 * r**2 * np.exp(-2 * Z2 * r)

def integrand(r, s):
    return rho_Li(r) * r**(2 - s) * 4 * np.pi

def compute_S_Li(L, s):
    result, _ = quad(lambda r: integrand(r, s), 0, L, limit=100)
    return result

L_vals = np.linspace(0.1, 10, 30)
s = 1.0
S_vals = [compute_S_Li(L, s) for L in L_vals]

plt.plot(L_vals, S_vals, marker='o', color='darkred')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{S}_{\mathrm{Li}}(L; 1.0)$')
plt.title('Canonical Summation for Lithium Approximate Density')
plt.grid(True)
plt.show()
