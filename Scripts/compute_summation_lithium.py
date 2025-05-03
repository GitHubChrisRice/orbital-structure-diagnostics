import numpy as np
import matplotlib.pyplot as plt

# Load Li radial density
data = np.loadtxt("lithium_radial_density.csv", delimiter=",", skiprows=1)
r = data[:, 0]
rho = data[:, 1]

# Parameters
s_values = [0.0, 1.0, 2.0]
summations = {}

for s in s_values:
    integrand = r**s * rho
    S = np.cumsum(integrand * np.gradient(r))
    summations[s] = S

# Plot
plt.figure()
for s, S in summations.items():
    plt.plot(r, S, label=f"$s={s}$")
plt.xlabel("Radius $L$ (Bohr)")
plt.ylabel(r"$\mathcal{S}_\psi(L; s)$")
plt.title("Canonical Summation $\mathcal{S}_\psi(L; s)$ for Lithium")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("summation_plot_lithium.png", dpi=300)

