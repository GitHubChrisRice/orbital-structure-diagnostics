import numpy as np
import matplotlib.pyplot as plt

# Load Li radial density
data = np.loadtxt("lithium_radial_density.csv", delimiter=",", skiprows=1)
r = data[:, 0]
rho = data[:, 1]

# Entropy for various N
L_max = r.max()
N_values = [20, 50, 100]
entropy_profiles = {}

for N in N_values:
    edges = np.linspace(0, L_max, N + 1)
    shell_mass = np.zeros(N)

    for i in range(N):
        mask = (r >= edges[i]) & (r < edges[i+1])
        shell_mass[i] = np.sum(rho[mask] * np.gradient(r[mask]))

    total_mass = np.sum(shell_mass)
    p = shell_mass / total_mass
    p = p[p > 0]
    entropy = -np.sum(p * np.log(p))
    entropy_profiles[N] = entropy

# Plot
plt.figure()
plt.plot(list(entropy_profiles.keys()), list(entropy_profiles.values()), marker='o')
plt.xlabel("Number of Shells $N$")
plt.ylabel(r"Entropy $\mathcal{H}_\psi(N)$")
plt.title("Radial Entropy $\mathcal{H}_\psi(N)$ for Lithium")
plt.grid(True)
plt.tight_layout()
plt.savefig("entropy_plot_lithium.png", dpi=300)

