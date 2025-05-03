import psi4

psi4.set_memory('500 MB')
psi4.core.set_output_file('h2_output.dat', False)

# Define the H2 molecule
h2 = psi4.geometry("""
0 1
H 0.0 0.0 0.0
H 0.0 0.0 0.74
""")

# Set options
psi4.set_options({
    'basis': 'sto-3g',
    'scf_type': 'pk',
    'cubeprop_tasks': ['orbitals'],
    'cubeprop_orbitals': [5]  # Orbital 5 is usually HOMO in minimal basis for H2
})

# Perform DFT calculation and generate cube file
psi4.energy('B3LYP')
psi4.cubeprop(h2)

