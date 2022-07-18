from FunctionDataProcessing import scatter3d, calculate_pvalues, boxplots, corrMatrix, getData, heatMap
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
Regms, regmKeys, LSPs = getData(dataset='S7')
#lsp1 = "MeanCurv"
#lsp2 = "TanCurv"
remRegmKeys = np.array(["RegComp"])
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)

def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    heatMap(x, y, ax, 64)
    #ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = (max(x)-min(x))/np.sqrt(len(x))
    xmax = np.max(np.abs(x))
    lim = (int(xmax/binwidth) + 1) * binwidth

    binsX = np.arange(min(x)-binwidth, lim + binwidth, binwidth)

    binwidth = (max(y)-min(y))/np.sqrt(len(y))
    ymax = np.max(np.abs(y))
    lim = (int(ymax/binwidth) + 1) * binwidth

    binsY = np.arange(min(y)-binwidth, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=len(binsX))
    ax_histy.hist(y, bins=len(binsY), orientation='horizontal')

def ht_hist(lsp1, lsp2):
    x, y = [], []
    for reg in regmKeys:
        x += list(Regms[reg][lsp1])
        y += list(Regms[reg][lsp2])
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.1]
    rect_histy = [left + width + spacing, bottom, 0.1, height]

    # start with a square Figure
    fig = plt.figure(figsize=(8,8))

    ax = fig.add_axes(rect_scatter)
    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histy = fig.add_axes(rect_histy, sharey=ax)

    # use the previously defined function
    scatter_hist(x, y, ax, ax_histx, ax_histy)
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    #ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * 1)
    ax.set_xlabel(lsp1)
    ax.set_ylabel(lsp2)
    plt.savefig(r"/Users/lorenz_veithen/Desktop/HPD_Research/LSPS_Assessment/Heatmaps/" + lsp1 + "vs" + lsp2, dpi=100)



i = 0
for X in LSPs:
    j = 0
    for Y in LSPs:
        if j > i:
            # do the plotting
            ht_hist(X, Y)
        else:
            # do nothing
            pass
        j += 1
    i += 1