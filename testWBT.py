import os
import pkg_resources
import numpy as np
import whitebox

wbt = whitebox.WhiteboxTools()
# Tools that have a great potential but require a paid license, for detailed descriptions
# see https://www.whiteboxgeo.com/manual/wbt_book/available_tools/geomorphometric_analysis.html#FetchAnalysis
## Accumulation Curvature
## Difference Curvature
## Curvedness
## Openness
## Ring curvature
## Rotor
## Shape index
# wbt.difference_curvature(dem=PATH_Smoothed_DEM,output=PATH_LSP + "\DC",log=False,zfactor=1.0)

### ==> Keep in mind for recommendations

# Looks cool but probably out of the scope
## ExposureTowardsWindFlux

#print(wbt.version())
#print(wbt.help())

smoothing = False
N_smoothing = 5
if smoothing:
    print("Starting Smoothing")
    PATH = r"/Users/lorenz_veithen/Desktop/HPD_Research/SmoothingTest/DEM_Small_S5_60.tif"
    for n in range(0, N_smoothing):
        New_Filtered_DEM = wbt.edge_preserving_mean_filter(
                                i=PATH,
                                output=PATH,
                                threshold=0.6,
                                filter=11)
        if n % 5 == 0: print(f"{(n/N_smoothing) * 100}% done")
    print(f"Smoothing: done")
# Give coordinate system

# test a few functions
PATH_Smoothed_DEM = r"/Users/lorenz_veithen/Desktop/HPD_Research/SmoothingTest/DEM_Small_S5_60.tif"
PATH_LSP = r"/Users/lorenz_veithen/Desktop/HPD_Research/TestWBT/Small"

### Use for sure
wbt.elev_percentile(PATH_Smoothed_DEM, PATH_LSP + "/EP", filterx=11,
        filtery=11, sig_digits=2, )

wbt.slope(PATH_Smoothed_DEM, PATH_LSP + r"/Slope",
    zfactor=None,units="degrees",)

wbt.mean_curvature(PATH_Smoothed_DEM, PATH_LSP + r"/MeanCurv",
    log=False, zfactor=None,)


wbt.tangential_curvature(PATH_Smoothed_DEM, PATH_LSP + r"/TanCurv",
    # log=False,
    zfactor=None,)

wbt.profile_curvature(PATH_Smoothed_DEM, PATH_LSP + r"/ProfCurv",
    # log=False,
    zfactor=None,)

wbt.diff_from_mean_elev(dem=PATH_Smoothed_DEM, output=PATH_LSP + "/DFME",
                        filterx=11, filtery=11)

wbt.surface_area_ratio(
    PATH_Smoothed_DEM,
    PATH_LSP + r"/SAR",)

wbt.num_upslope_neighbours(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/NUN",)

wbt.gaussian_curvature(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + "/GC",
    log=False,
    zfactor=None,
)

wbt.total_curvature(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/TotCurv",
    # log=False,
    zfactor=None,
)
