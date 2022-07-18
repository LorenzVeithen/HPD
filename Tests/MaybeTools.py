import whitebox

wbt = whitebox.WhiteboxTools()
### Not use - but for recommendations of automatic delineation
smoothing = False
N_smoothing = 3
if smoothing:
    print("Starting Smoothing")
    PATH = r"/Users/lorenz_veithen/Desktop/HPD_Research/SmoothingTest/DEM_Large_S3.tif"
    for n in range(0, N_smoothing):
        New_Filtered_DEM = wbt.edge_preserving_mean_filter(
                                i=PATH,
                                output=PATH,
                                threshold=0.1,
                                filter=11)
        if n % 5 ==0: print(f"{(n/N_smoothing) * 100}% done")
    print(f"Smoothing: done")
# Give coordinate system

# PATHs
PATH_Smoothed_DEM = r"/Users/lorenz_veithen/Desktop/HPD_Research/SmoothingTest/DEM_Large_S3.tif"
PATH_LSP = r"/Users/lorenz_veithen/Desktop/HPD_Research/TestWBT"
### Maybe use



wbt.standard_deviation_of_slope(  # Measure of surface roughness # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/SlopeStd",
    zfactor=None,
    filterx=11,
    filtery=11,
)

wbt.dev_from_mean_elev(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + "/DevFME",
    filterx=11,
    filtery=11,
) # another view on the same DiffFromMeanElevation

wbt.max_downslope_elev_change(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + "/MDEC",
)

wbt.edge_density( PATH_Smoothed_DEM,PATH_LSP + "/ED", filter=11,
    norm_diff=0.1,  # This value will need quite some experimentation to find an optimal value very promising
    zfactor=None,)  # provides one of the best measures of surface texture of any of the available roughness tools