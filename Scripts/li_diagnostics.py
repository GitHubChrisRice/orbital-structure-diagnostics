import numpy as np
import matplotlib.pyplot as plt

# Load radial density data
data = np.loadtxt("radial_density_li.csv", delimiter=",", skiprows=1)
r = data[:, 0]
rho = data[:, 1]

# ---------- Canonical Summation ----------
s_values = [0.0, 1.0, 2.0]
S = {}
for s in s_values:
    S[s] = np.array([np.sum(rho[r <= L] * r[r <= L]**(2 - s)) for L in r])

# Plot Canonical Summation
plt.figure()
for s in s_values:
    plt.plot(r, S[s], label=fr"$s = {s}$")
plt.xlabel("Radius $L$ (Bohr)")
plt.ylabel(r"$\mathcal{S}_\psi(L; s)$")
plt.title("Canonical Summation $\mathcal{S}_\psi(L; s)$ for Li")
plt.legend()
plt.grid(True)
plt.savefig("summation_plot_li.png", dpi=300)

# ---------- Radial Entropy ----------
def radial_entropy(rho_bins):
    p = rho_bins / np.sum(rho_bins)
    p = p[p > 0]
    return -np.sum(p * np.log(p))

N_values = [20, 50, 100]
H = []
for N in N_values:
    bins = np.linspace(0, r.max(), N + 1)
    digitized = np.digitize(r, bins) - 1
    binned_rho = np.zeros(N)
    for i in range(N):
        binned_rho[i] = np.sum(rho[digitized == i])
    H.append(radial_entropy(binned_rho))

# Plot Radial Entropy
plt.figure()
plt.plot(N_values, H, marker='o')
plt.xlabel("Number of Shells $N$")
plt.ylabel(r"Entropy $\mathcal{H}_\psi(N)$")
plt.title(r"Radial Entropy $\mathcal{H}_\psi(N)$ for Li")
plt.grid(True)
plt.savefig("entropy_plot_li.png", dpi=300)

