from scipy.spatial import cKDTree
import numpy as np
from FunctionDataProcessing import getData
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

def scatter_hist(x, y, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # now determine nice limits by hand:
    binwidth = (max(x)-min(x))/np.sqrt(len(x))
    xmax = np.max(np.abs(x))
    lim = (int(xmax/binwidth) + 1) * binwidth

    binsX = np.arange(min(x)-binwidth, lim + binwidth, binwidth)

    binwidth = (max(y)-min(y))/np.sqrt(len(y))
    ymax = np.max(np.abs(y))
    lim = (int(ymax/binwidth) + 1) * binwidth
    print(binsX)
    binsY = np.arange(min(y)-binwidth, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=len(binsX))
    ax_histy.hist(y, bins=len(binsY), orientation='horizontal')

lsp1 = "MeanCurv"
lsp2 = "TanCurv"
sigma = 64
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

rect_scatter = [left, bottom, width, height]
Regms, regmKeys, LSPs = getData()
xs = Regms[regmKeys[3]][lsp1]
ys = Regms[regmKeys[3]][lsp2]

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes(rect=rect_scatter)
resolution = 250
extent = [np.min(xs), np.max(xs), np.min(ys), np.max(ys)]
xv = data_coord2view_coord(xs, resolution, extent[0], extent[1])
yv = data_coord2view_coord(ys, resolution, extent[2], extent[3])

neighbours = sigma
im = kNN2DDens(xv, yv, resolution, neighbours)
ax.imshow(im, origin='lower', extent=extent, cmap=cm.jet)
ratio = 1
x_left, x_right = ax.get_xlim()
y_low, y_high = ax.get_ylim()
ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
# ax.set_title("Smoothing over %d neighbours" % neighbours)
# plt.savefig('new.png', dpi=150)

rect_histx = [left, bottom + height + spacing, width, 0.1]
rect_histy = [left + width + spacing, bottom, 0.1, height]

ax_histx = fig.add_axes(rect_histx, sharex=ax)
#ax_histx.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

ax_histy = fig.add_axes(rect_histy, sharey=ax)
#ax_histy.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

scatter_hist(xs, ys, ax_histx, ax_histy)
ax.set_xlabel(lsp1)
ax.set_ylabel(lsp2)