import psi4

psi4.set_options({
    'basis': 'sto-3g',
    'scf_type': 'pk',
    'cubeprop_tasks': ['density'],
})

# Ammonia geometry (C3v)
nh3 = psi4.geometry("""
0 1
N     0.000000     0.000000     0.000000
H     0.000000     0.9377       0.3816
H     0.8121      -0.4688       0.3816
H    -0.8121      -0.4688       0.3816
units angstrom
""")

# Capture wavefunction
wfn = psi4.energy('B3LYP', return_wfn=True)[1]

# Generate cube files
psi4.cubeprop(wfn)

