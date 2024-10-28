def unmix(in_file, out_file, endmembers):

    import rasterio
    import numpy as np
    from lsutools.lsu import unmix_nnls

    with rasterio.open(in_file, 'r') as ds:
        data = ds.read()           
        profile = ds.profile  

    bands, height, width = data.shape
    em_count = endmembers.shape[0]

    # switch shape from (bands, height, width) to (height, width, bands)
    pixels = np.moveaxis(data, 0, 2)
    
    #flatten, as unixing expects 2D array
    pixels = np.reshape(pixels, (width*height, bands))

    #unmix
    result = unmix_nnls(pixels, endmembers)

    #unflatten
    result = np.reshape(result, (height, width, em_count))
    
    #revert reshape for rasterio
    result = np.moveaxis(result, 2, 0)

    with rasterio.open(
        out_file,
        "w",
        count=len(endmembers),
        driver="GTiff",
        height=height,
        width=width,
        dtype=result.dtype,
        crs=profile["crs"],
        transform=profile["transform"],
    ) as dst:
        dst.write(result)

