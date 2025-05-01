import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Z_eff = 1.6875  # Effective nuclear charge

def rho_He(r):
    return (Z_eff**3 / np.pi) * np.exp(-2 * Z_eff * r)

def integrand_He(r, s):
    return rho_He(r) * r**(2 - s) * 4 * np.pi

def compute_S_He(L, s):
    result, _ = quad(lambda r: integrand_He(r, s), 0, L, limit=100)
    return result

L_vals = np.linspace(0.1, 10, 20)
s = 1.0
S_vals = [compute_S_He(L, s) for L in L_vals]

plt.plot(L_vals, S_vals, marker='o', color='blue')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{S}_{\mathrm{He}}(L; 1.0)$')
plt.title('Helium Approximate Density (Summation)')
plt.grid(True)
plt.show()
