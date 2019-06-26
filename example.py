import seekpath as skp
import numpy as np
from simphony.data.phonon import PhononData
from simphony.data.interpolation import InterpolationData
from simphony.plot.dispersion import plot_dispersion, plot_sqw_map

seedname = 'quartz'

pdata = PhononData(seedname)
idata = InterpolationData(seedname)

# There are multiple ways to get the q-points. Choose one:
###############
# 1) This uses the q-points already in the .phonon file
qpts = pdata.qpts
###############
# 2) This generates a new 'recommended' q-point path
#_, unique_ions = np.unique(idata.ion_type, return_inverse=True)
#structure = (idata.cell_vec.magnitude, idata.ion_r, unique_ions)
#qpts = skp.get_explicit_k_path(structure)["explicit_kpoints_rel"]
###############
# 3) This reads q-points from a .txt file
#qpts = np.loadtxt('qpts.txt')

# Calculate phonons for provided q-points
idata.calculate_fine_phonons(qpts)

# Plot dispersion
fig1 = plot_dispersion(idata)
fig1.show()

# Calculate S(Q,w) map: this is what the inelastic neutron scattering data
# looks like
scattering_lengths = {'La': 8.24,
                      'Zr': 7.16,
                      'O': 5.803,
                      'C': 6.646,
                      'Si': 4.1491,
                      'H': -3.7390,
                      'N': 9.36,
                      'S': 2.847}
ebins = np.arange(0, 150, 1.0)
idata.calculate_sqw_map(scattering_lengths, ebins)
fig2, ims = plot_sqw_map(idata, ratio=1.0, ewidth=1.0, qwidth=0.001)
fig2.show()

