import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import tplquad

a0 = 1.0  # Bohr radius

def rho_2pz(r, theta):
    prefactor = 1 / (32 * np.pi * a0**5)
    return prefactor * r**2 * np.exp(-r / a0) * (np.cos(theta))**2

def integrand_2pz(r, theta, phi, s):
    return rho_2pz(r, theta) * r**(2 - s) * np.sin(theta)

def compute_S_2pz(L, s):
    result, _ = tplquad(
        lambda r, theta, phi: integrand_2pz(r, theta, phi, s),
        0, 2*np.pi,
        lambda phi: 0, lambda phi: np.pi,
        lambda phi, theta: 0, lambda phi, theta: L
    )
    return result

L_vals = np.linspace(0.1, 5, 10)
s = 1.0
S_vals = [compute_S_2pz(L, s) for L in L_vals]

plt.plot(L_vals, S_vals, marker='o', color='orange')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{S}_{2p_z}(L; 1.0)$')
plt.title('Quick Test: Hydrogen 2p_z Summation')
plt.grid(True)
plt.show()
