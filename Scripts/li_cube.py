import psi4

# Define the lithium atom
psi4.geometry("""
Li 0.0 0.0 0.0
units angstrom
""")

# Set DFT and cube output options
psi4.set_options({
    'basis': 'sto-3g',
    'scf_type': 'pk',
    'cubeprop_tasks': ['density']
})

# Perform DFT calculation and get wavefunction
energy, wfn = psi4.energy('B3LYP', return_wfn=True)

# Output density cube
psi4.cubeprop(wfn)

