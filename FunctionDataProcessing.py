import statistics as st
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import glob
import matplotlib.cm as cm
from scipy.spatial import cKDTree
import matplotlib as mpl

def getData(dataset='S3'):
    dataFile = r"RegmaglyptsData" + str(dataset)
    fileMAIN = dataFile + "/RegA.txt"
    #fileMAIN = r"RegmaglyptsDataR/RegA.txt"  # used to obtain the first header
    data_pd = pd.read_csv(fileMAIN, header=0, sep=',')
    K = data_pd.keys()  # Get keys of 1, should be the same for all
    K = np.append([K[0], K[1], K[2], K[3]], [k[:-7] for k in K[4:]])
    Regms = {}
    regmKeys = [f[16+len(dataset):-4] for f in glob.glob(dataFile + "/*.txt")]  # Next: K
    files = glob.glob(dataFile + "/*.txt")
    # Big Doubt: H (compare to 1c), I, L, M
    # Need advise on: A,B,C
    # Happy with: G
    # Not happy with:

    # Left for later: P
    # Note: O is the weird one.
    j = 0
    for mainkey in regmKeys:
        i, tempdict = 0, {}
        data_pd = pd.read_csv(files[j], header=0, sep=',')
        data_arr = data_pd.to_numpy()
        for datakey in K:
            tempdict[datakey] = data_arr[:, i]
            i += 1
        Regms[mainkey] = tempdict
        j += 1

    regmKeys.sort()
    LSPs = K[5:]
    regmWO_comp = np.setdiff1d(regmKeys, np.array(["RegComp"]))
    if dataset[0] == 'S':
        areas = [0.388479, 0.411368, 0.262872, 0.512113, 0.424401, 0.226698, 0.207511, 0.124627, 0.212296, 0.312347,
                 0.331682, 0.42659, 0.174957, 0.326961, 0.266113, 0.147424, 0.336141, 0.446652, 0.247483, 0.166427,
                 0.115028, 0.212635, 0.097461, 0.170194, 0.236973]
        i = 0
        for k in regmWO_comp:
            Regms[k]["Area"] = areas[i]
            i += 1
    return Regms, regmKeys, LSPs

def selectedStatistics(array, n_quant):
    mean_arr = st.mean(array)
    median_arr = st.median(array)
    stdev_arr = st.stdev(array)
    min_arr = min(array)
    max_arr = max(array)
    quantiles_arr = st.quantiles(array, n_quant)

    return mean_arr, median_arr, stdev_arr, min_arr, max_arr, quantiles_arr

def scatter3d(x,y,z, i, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cs = z
    #cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    #scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure(i)
    ax = Axes3D(fig)
    ax.scatter3D(x, y, z, c=cs, cmap=cm)

    #fig.colorbar(scalarMap)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    #scalarMap.set_array(cs)
    plt.show()


def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues

def boxplots(regmKeys, LSPs, Regms):
    secKeys = regmKeys
    fig, axs = plt.subplots(len(LSPs))
    fig.suptitle('Boxplots for different LSPs')
    bp_data = {}
    i = 0
    for param in LSPs:
        bp = []
        for k in secKeys:
            bp.append(Regms[k][param])
        axs[i].boxplot(bp, notch=True)
        axs[i].title.set_text(param)
        axs[i].xaxis.set_visible(False)
        bp_data[param] = bp
        i += 1
    axs[i - 1].xaxis.set_visible(True)
    plt.xticks(np.arange(1, len(secKeys) + 1, 1), secKeys)
    plt.subplots_adjust(hspace=1)
    return bp_data

def corrMatrix(Regms, LSPs, regmKeys, mode=0):
    Regms["cb"] = {}
    #Regms["cb"]["Regmaglypt_ID"] = []
    for param in LSPs:
        Regms["cb"][param] = []
        for k in regmKeys:
            Regms["cb"][param] = np.append(Regms["cb"][param], Regms[k][param])
            #Regms["cb"]["Regmaglypt_ID"] = np.append(Regms["cb"]["Regmaglypt_ID"], np.array([k]*len(Regms["cb"][param])))
    # Assign matrix
    fig, axs = plt.subplots(len(LSPs) - 1, len(LSPs) - 1)
    i = 0
    for X in LSPs:
        j = 0
        for Y in LSPs:
            if j > i:
                # do the plotting
                if mode == 0:
                    # normal scatter plot
                    axs[j - 1, i].scatter(Regms["RegComp"][X], Regms["RegComp"][Y], s=np.ones(len(Regms["RegComp"][Y])), color='b')
                    axs[j - 1, i].scatter(Regms["cb"][X], Regms["cb"][Y], s=np.ones(len(Regms["cb"][Y])) * 0.5, color='r')

                elif mode == 1:
                    # heatmap
                    heatMap(Regms["cb"][X], Regms["cb"][Y], axs[j - 1, i], sigma=20)
                elif mode == 2:
                    # coloured map

                    pass
                else:
                    axs[j - 1, i].scatter(Regms["cb"][X], Regms["cb"][Y], s=np.ones(len(Regms["cb"][Y])) * 0.5)
                axs[j - 1, i].set(xlabel=X, ylabel=Y)
            else:
                # do nothing
                pass
            j += 1
        i += 1
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    # plt.show()

    # Find correlation coefficients
    frame = np.zeros((len(Regms["cb"][LSPs[0]]), len(LSPs)))
    i = 0
    for param in LSPs:
        frame[:, i] = Regms["cb"][param]
        i += 1

    data = pd.DataFrame(frame, columns=LSPs)
    corrFrame = data.corr()
    pvalFrame = calculate_pvalues(data)
    return corrFrame, pvalFrame


def heatMap(xs, ys, ax, sigma):
    def data_coord2view_coord(p, resolution, pmin, pmax):
        dp = pmax - pmin
        dv = (p - pmin) / dp * resolution
        return dv

    def kNN2DDens(xv, yv, resolution, neighbours, dim=2):
        # Create the tree
        tree = cKDTree(np.array([xv, yv]).T)
        # Find the closest nnmax-1 neighbors (first entry is the point itself)
        grid = np.mgrid[0:resolution, 0:resolution].T.reshape(resolution ** 2, dim)
        dists = tree.query(grid, neighbours)
        # Inverse of the sum of distances to each grid point.
        inv_sum_dists = 1. / dists[0].sum(1)

        # Reshape
        im = inv_sum_dists.reshape(resolution, resolution)
        return im

    resolution = 250
    extent = [np.min(xs), np.max(xs), np.min(ys), np.max(ys)]
    xv = data_coord2view_coord(xs, resolution, extent[0], extent[1])
    yv = data_coord2view_coord(ys, resolution, extent[2], extent[3])

    neighbours = sigma
    im = kNN2DDens(xv, yv, resolution, neighbours)


    #----------
    # create a colormap that consists of
    # - 1/5 : custom colormap, ranging from white to the first color of the colormap
    # - 4/5 : existing colormap

    # set upper part: 4 * 256/4 entries
    upper = mpl.cm.jet(np.arange(256))

    # set lower part: 1 * 256/4 entries
    # - initialize all entries to 1 to make sure that the alpha channel (4th column) is 1
    lower = np.ones((int(256 / 4), 4))
    # - modify the first three columns (RGB):
    #   range linearly between white (1,1,1) and the first color of the upper colormap
    for i in range(3):
        lower[:, i] = np.linspace(1, upper[0, i], lower.shape[0])

    # combine parts of colormap
    cmap = np.vstack((lower, upper))

    # convert to matplotlib colormap
    cmap = mpl.colors.ListedColormap(cmap, name='myColorMap', N=cmap.shape[0])
    #----------


    ax.imshow(im, origin='lower', extent=extent, cmap=cmap)
    ratio = 1
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    # ax.set_title("Smoothing over %d neighbours" % neighbours)
    # plt.savefig('new.png', dpi=150)
    return True

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)