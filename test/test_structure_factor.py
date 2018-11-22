import unittest
import numpy.testing as npt
import numpy as np
from casteppy.data.phonon import PhononData
from casteppy.data.interpolation import InterpolationData
from casteppy.calculate.scattering import structure_factor


class TestStructureFactorPhononDataLZO(unittest.TestCase):

    def setUp(self):
        seedname = 'La2Zr2O7'
        phonon_path = 'test/data/'
        self.sf_path = 'test/data/scattering/'
        self.data = PhononData(seedname, phonon_path)
        self.scattering_lengths = {'La': 8.24, 'Zr': 7.16, 'O': 5.803}

    def test_sf_T5(self):
        sf = structure_factor(self.data, self.scattering_lengths, T=5)
        expected_sf = np.loadtxt(self.sf_path + 'sf_T5.txt')
        npt.assert_allclose(sf, expected_sf)

    def test_sf_T100(self):
        sf = structure_factor(self.data, self.scattering_lengths, T=100)
        expected_sf = np.loadtxt(self.sf_path + 'sf_T100.txt')
        npt.assert_allclose(sf, expected_sf)

class TestStructureFactorInterpolationDataLZO(unittest.TestCase):

    def setUp(self):
        # Need to separately test SF calculation with interpolated phonon data
        # to test eigenvector calculations
        seedname = 'La2Zr2O7'
        phonon_path = 'test/data/'
        interpolation_path = 'test/data/interpolation/LZO'
        self.sf_path = 'test/data/scattering/'
        pdata = PhononData(seedname, phonon_path)
        self.data = InterpolationData(seedname, interpolation_path)
        self.data.calculate_fine_phonons(pdata.qpts)
        self.scattering_lengths = {'La': 8.24, 'Zr': 7.16, 'O': 5.803}

    def test_sf_T5(self):
        sf = structure_factor(self.data, self.scattering_lengths, T=5)
        expected_sf = np.loadtxt(self.sf_path + 'sf_T5.txt')
        npt.assert_allclose(sf[:,3:], expected_sf[:, 3:], atol=1e0)

    def test_sf_T100(self):
        sf = structure_factor(self.data, self.scattering_lengths, T=100)
        expected_sf = np.loadtxt(self.sf_path + 'sf_T100.txt')
        npt.assert_allclose(sf[:,3:], expected_sf[:, 3:], atol=1e0)