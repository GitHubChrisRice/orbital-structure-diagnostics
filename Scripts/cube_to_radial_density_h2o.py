import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d  # <-- Added for smoothing

def load_cube_density(filename):
    with open(filename, 'rb') as f:
        lines = f.read().decode('latin1').splitlines()

    origin = np.array([float(x) for x in lines[2].split()[1:]])
    num_points = []
    axes = []
    for i in range(3):
        parts = lines[3 + i].split()
        num_points.append(int(parts[0]))
        axes.append(np.array([float(x) for x in parts[1:]]))

    nx, ny, nz = num_points
    total_points = nx * ny * nz
    num_atoms = abs(int(lines[2].split()[0]))
    start_line = 6 + num_atoms + 1

    raw_floats = []
    for line in lines[start_line:]:
        raw_floats.extend(line.split())
        if len(raw_floats) >= total_points:
            break

    if len(raw_floats) != total_points:
        print(f"Warning: Expected {total_points} points, got {len(raw_floats)} — padding with zeros.")
        raw_floats += [0.0] * (total_points - len(raw_floats))

    data = np.array([float(val) for val in raw_floats[:total_points]])
    x = np.arange(nx) * axes[0][0] + origin[0]
    y = np.arange(ny) * axes[1][1] + origin[1]
    z = np.arange(nz) * axes[2][2] + origin[2]
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    R = np.sqrt((X - origin[0])**2 + (Y - origin[1])**2 + (Z - origin[2])**2)
    R = R.flatten()
    density = data.flatten()

    return R, density

def radial_average(R, density, num_bins=300):
    r_max = np.max(R)
    bins = np.linspace(0, r_max, num_bins + 1)
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    radial_density = np.zeros(num_bins)
    counts = np.zeros(num_bins)

    bin_indices = np.digitize(R, bins) - 1
    for i in range(len(R)):
        if 0 <= bin_indices[i] < num_bins:
            radial_density[bin_indices[i]] += density[i]
            counts[bin_indices[i]] += 1

    with np.errstate(divide='ignore', invalid='ignore'):
        radial_density = np.where(counts > 0, radial_density / counts, 0)

    return bin_centers, radial_density

if __name__ == "__main__":
    cube_file = "h2o_density.cube"
    R, rho = load_cube_density(cube_file)
    r_bins, rho_r = radial_average(R, rho, num_bins=300)

    # Apply Gaussian smoothing
    rho_r_smooth = gaussian_filter1d(rho_r, sigma=2)

    np.savetxt("radial_density.csv", np.column_stack((r_bins, rho_r_smooth)), delimiter=',', header='r,rho(r)', comments='')

    plt.plot(r_bins, rho_r_smooth)
    plt.xlabel("Radius r (Bohr)")
    plt.ylabel("Radial Density ρ(r)")
    plt.title("Spherically Averaged Electron Density (Smoothed)")
    plt.grid(True)
    plt.savefig("radial_density_plot.png", dpi=300)
    plt.show()

