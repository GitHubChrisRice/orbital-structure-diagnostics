import psi4

# Set memory and output file
psi4.set_memory('1 GB')
psi4.core.set_output_file('h2o_output.dat', False)

# Define H₂O geometry (approx 104.5° angle, in Angstroms)
h2o = psi4.geometry("""
0 1
O    0.000000    0.000000    0.000000
H    0.758602    0.000000    0.504284
H   -0.758602    0.000000    0.504284
units angstrom
""")

# Psi4 options
psi4.set_options({
    'basis': 'sto-3g',
    'scf_type': 'pk',
    'cubeprop_tasks': ['density'],
})

# Energy calculation and cube output
energy, wfn = psi4.energy('B3LYP', return_wfn=True)
psi4.cubeprop(wfn)

