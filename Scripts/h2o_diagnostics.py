
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Load radial data
data = np.loadtxt("radial_density_data.csv", delimiter=",", skiprows=1)
r = data[:, 0]
rho = data[:, 1]

# Smooth
rho_smoothed = gaussian_filter1d(rho, sigma=2)

# Canonical Summation: Sψ(L; s)
s_values = [0.0, 1.0, 2.0]
for_s = {}
for s in s_values:
    S = np.array([np.trapz(rho_smoothed[:i] * r[:i]**(2 - s), r[:i]) for i in range(2, len(r))])
    for_s[s] = S

plt.figure()
for s in s_values:
    plt.plot(r[2:], for_s[s], label=f"$s = {s}$")
plt.xlabel("Radius $L$ (Bohr)")
plt.ylabel("$\\mathcal{{S}}_\\psi(L; s)$")
plt.title("Canonical Summation $\\mathcal{{S}}_\\psi(L; s)$ for H$_2$O")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("summation_plot_h2o.png")

# Radial Entropy: Hψ(N)
N_values = [20, 50, 100]
entropies = []

for N in N_values:
    bins = np.linspace(r[0], r[-1], N + 1)
    hist, _ = np.histogram(r, bins=bins, weights=rho_smoothed)
    prob = hist / np.sum(hist)
    prob = prob[prob > 0]
    entropy = -np.sum(prob * np.log(prob))
    entropies.append(entropy)

plt.figure()
plt.plot(N_values, entropies, marker="o")
plt.xlabel("Number of Shells $N$")
plt.ylabel("Entropy $\\mathcal{{H}}_\\psi(N)$")
plt.title("Radial Entropy $\\mathcal{{H}}_\\psi(N)$ for H$_2$O")
plt.grid(True)
plt.tight_layout()
plt.savefig("entropy_plot_h2o.png")
