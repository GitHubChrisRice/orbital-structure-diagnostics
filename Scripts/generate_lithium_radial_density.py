import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.0001, 15, 1000)

# Core 1s² electrons (Z_eff ≈ 2.7)
Z1 = 2.7
rho_1s = 2 * (Z1**3) * np.exp(-2 * Z1 * r)

# Valence 2s¹ electron (Z_eff ≈ 1.3)
Z2 = 1.3
rho_2s = (1 - Z2 * r)**2 * np.exp(-Z2 * r)
rho_2s = rho_2s / np.trapz(rho_2s * r**2, r)  # Normalize
rho_2s *= 1  # one electron

# Total Li density: 2 (core) + 1 (valence)
rho = rho_1s + rho_2s

# Save
np.savetxt("lithium_radial_density.csv", np.column_stack((r, rho)), delimiter=',', header='r,rho(r)', comments='')

# Plot
plt.plot(r, rho)
plt.xlabel("Radius r (Bohr)")
plt.ylabel("Radial Density ρ(r)")
plt.title("Heuristic Lithium Radial Density (1s² + 2s¹)")
plt.grid(True)
plt.tight_layout()
plt.savefig("lithium_density_plot.png", dpi=300)

