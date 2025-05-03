import numpy as np
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt

# Load radial density CSV
data = np.loadtxt("radial_density_h2o_ccpvtz.csv", delimiter=',', skiprows=1)
r_vals, rho_vals = data[:, 0], data[:, 1]

def compute_entropy(r, rho, N):
    bins = np.linspace(0, np.max(r), N + 1)
    hist = np.histogram(r, bins=bins, weights=rho)[0]
    prob = hist / np.sum(hist)
    prob = prob[prob > 0]
    return -np.sum(prob * np.log(prob))

# Compare entropy at two bin sizes
N1, N2 = 100, 200
H1 = compute_entropy(r_vals, rho_vals, N1)
H2 = compute_entropy(r_vals, rho_vals, N2)
delta = abs(H1 - H2)

print(f"H(N=100) = {H1:.5f}, H(N=200) = {H2:.5f}, Δ = {delta:.5f}")

