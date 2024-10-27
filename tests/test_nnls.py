import numpy as np
import pytest

from lsutools.lsu import unmix_nnls


def test_unmix_nnls():
    endmembers = np.array([[1, 1, 0], [0, 0, 1]])
    pixels = np.array([[2, 1, 1]])
    result = unmix_nnls(pixels, endmembers)

    np.testing.assert_array_equal([[1.5, 1. ]], result)

def test_unmix_nnls_band_mismatch():
    endmembers = np.array([[1, 1, 0], [0, 0, 1]])
    pixels = np.array([[2, 1, 1, 1]])

    with pytest.raises(Exception):
        unmix_nnls(pixels, endmembers)