import numpy as np
import matplotlib.pyplot as plt

Z1 = 2.69
Z2 = 1.28
A1 = 2.0
A2 = 0.5

def rho_Li(r):
    return A1 * np.exp(-2 * Z1 * r) + A2 * r**2 * np.exp(-2 * Z2 * r)

def compute_entropy(L, N):
    r_edges = np.linspace(0, L, N+1)
    p_vals = []
    total = 0

    for i in range(N):
        r1 = r_edges[i]
        r2 = r_edges[i+1]
        dr = r2 - r1
        r_mid = (r1 + r2) / 2
        shell_volume = 4 * np.pi * r_mid**2 * dr
        p = rho_Li(r_mid) * shell_volume
        p_vals.append(p)
        total += p

    p_vals = [p / total for p in p_vals if p > 0]
    entropy = -sum(p * np.log(p) for p in p_vals)
    return entropy

L_vals = np.linspace(0.1, 10, 30)
H_vals = [compute_entropy(L, 20) for L in L_vals]

plt.plot(L_vals, H_vals, marker='o', color='darkred')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{H}_{\mathrm{Li}}(L; 20)$')
plt.title('Entropy of Lithium Approximate Density')
plt.grid(True)
plt.show()
