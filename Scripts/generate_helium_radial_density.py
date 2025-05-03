import numpy as np
import matplotlib.pyplot as plt

# Parameters
Z = 2
r = np.linspace(0, 15, 1000)
rho = 8 * Z**3 * np.exp(-2 * Z * r)

# Save to file (same format as smoothed DFT data)
np.savetxt("helium_radial_density.csv", np.column_stack((r, rho)), delimiter=',', header='r,rho(r)', comments='')

# Optional plot
plt.plot(r, rho)
plt.xlabel("Radius r (Bohr)")
plt.ylabel("Radial Density ρ(r)")
plt.title("Heuristic Helium Radial Density")
plt.grid(True)
plt.tight_layout()
plt.savefig("helium_density_plot.png", dpi=300)

