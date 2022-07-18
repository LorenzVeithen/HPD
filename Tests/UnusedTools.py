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

# test a few functions
PATH_Smoothed_DEM = r"/Users/lorenz_veithen/Desktop/HPD_Research/SmoothingTest/DEM_Large_S3.tif"
PATH_LSP = r"/Users/lorenz_veithen/Desktop/HPD_Research/TestWBT"
wbt.pennock_landform_class(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/PLC",
    slope=3.0,
    prof=0.1,
    plan=0.0,
)  # WATCH OUT: sensitive to the smoothing, make sure it is optimised before proceeding

# Tool can be used to perform a simple landform classification based on measures of
# slope gradient and curvature derived from a user-specified digital elevation model (DEM).
# The classification scheme is based on the method proposed by Pennock, Zebarth, and DeJong (1987).
# The scheme divides a landscape into seven element types, including: convergent footslopes (CFS),
# divergent footslopes (DFS), convergent shoulders (CSH), divergent shoulders (DSH), convergent
# backslopes (CBS), divergent backslopes (DBS), and level terrain (L).

wbt.geomorphons( # Very promising as well as a way to spot regmaglypts, loook into making the tool work!!!
    PATH_Smoothed_DEM, # OK
    PATH_LSP + "/Geomorphon",
    search=50,
    threshold=0.0,
    tdist=0,
)

### For sure not use
wbt.num_downslope_neighbours(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/NDN",
)

wbt.maximal_curvature( # OK
     PATH_Smoothed_DEM,
     PATH_LSP + r"/MaxCurv",
     log=False,
     zfactor=None,
 ) # included in Gaussian curvature

wbt.minimal_curvature( # OK
     PATH_Smoothed_DEM,
     PATH_LSP + r"/MinCurv",
     log=False,
     zfactor=None,
 ) # included in Gaussian curvature

wbt.plan_curvature(  # OK
    PATH_Smoothed_DEM,
    PATH_LSP + r"/PlanCurv",
    # log=False,
    zfactor=None,
)# Similar to tangential curvature

wbt.percent_elev_range(dem=PATH_Smoothed_DEM,  # OK
                       output=PATH_LSP + "/PER",
                       filterx=3,
                       filtery=3)






