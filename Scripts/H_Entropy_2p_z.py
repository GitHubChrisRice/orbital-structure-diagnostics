import numpy as np
import matplotlib.pyplot as plt

a0 = 1.0
def rho_2pz(r, theta):
    prefactor = 1 / (32 * np.pi * a0**5)
    return prefactor * r**2 * np.exp(-r / a0) * (np.cos(theta))**2

def rho_2pz_radial(r):
    # Average over angle: ⟨cos²θ⟩ = 1/3
    return (1/3) * (1 / (32 * np.pi * a0**5)) * r**2 * np.exp(-r / a0)

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
        p = rho_2pz_radial(r_mid) * shell_volume
        p_vals.append(p)
        total += p

    p_vals = [p / total for p in p_vals if p > 0]
    entropy = -sum(p * np.log(p) for p in p_vals)
    return entropy

L_vals = np.linspace(0.1, 10, 30)
H_vals = [compute_entropy(L, 20) for L in L_vals]

plt.plot(L_vals, H_vals, marker='o', color='orange')
plt.xlabel('L (Bohr radii)')
plt.ylabel(r'$\mathcal{H}_{2p_z}(L; 20)$')
plt.title('Entropy of Hydrogen 2p_z Orbital')
plt.grid(True)
plt.show()
