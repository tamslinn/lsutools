import numpy as np
import os.path
import tempfile

from lsutools.lsu import unmix


def test_unmix():
    endmembers = np.array([[1240.0,1666.0,1952.0,1976.0,2601.0,2790.0,3082.0,3025.0,3283.0,2649.0],
                           [422.0,678.0,452.0,1055.0,3236.0,3901.0,3606.0,4264.0,2096.0,986.0],
                           [692,648,543,502,387,375,327,283,52,51]])

    with tempfile.TemporaryDirectory() as tmp:
        out_file = os.path.join(tmp, "nnls_output.tif")
        unmix("./tests/data/sample1.tif", out_file, endmembers)
        assert os.path.isfile(out_file)

