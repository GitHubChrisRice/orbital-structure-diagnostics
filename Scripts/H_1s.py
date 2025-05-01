import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import tplquad

a0 = 1.0  # Bohr radius

def rho_1s(r):
    return (1 / (np.pi * a0**3)) * np.exp(-2 * r / a0)

def integrand_1s(r, theta, phi, s):
    return rho_1s(r) * r**(2 - s) * np.sin(theta)

def compute_S_1s(L, s):
    result, _ = tplquad(
        lambda r, theta, phi: integrand_1s(r, theta, phi, s),
        0, 2*np.pi,
        lambda phi: 0, lambda phi: np.pi,
        lambda phi, theta: 0, lambda phi, theta: L
    )
    return result

L_vals = np.linspace(0.1, 5, 10)
s = 1.0
S_vals = [compute_S_1s(L, s) for L in L_vals]

plt.plot(L_vals, S_vals, marker='o')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{S}_{1s}(L; 1.0)$')
plt.title('Quick Test: Hydrogen 1s Summation')
plt.grid(True)
plt.show()
