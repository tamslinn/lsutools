def unmix_nnls(pixels, endmembers):

    import scipy.optimize as opt
    import numpy as np

    num_pixels, num_bands1 = pixels.shape
    num_endmembers, num_bands2 = endmembers.shape

    if num_bands1 != num_bands2:
        raise ValueError(f'Endmember band count {num_bands2} does not match image band count {num_bands1}')

    result = np.zeros((num_pixels, num_endmembers), dtype=np.float32)

    for i in range(num_pixels):
        # for each pixel, call scipy nnls function
        result[i] = opt.nnls(endmembers.T, pixels[i])[0]

    return result
