from FunctionDataProcessing import getData, get_cmap
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

lsp1 = 'MeanCurv'
lsp2 = 'TotCurv'

Regms, regmKeys, LSPs = getData(dataset='S5')
remRegmKeys = np.array(['RegO'])  # ["RegComp", "RegO", "RegP", "RegC", "RegE", "RegL2", "RegQ1"]
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)

print(regmKeys)
def colourPlot(regmK):
    cmap = get_cmap(len(regmK))
    colors = [cmap(i) for i in range(0, len(regmK))]
    x, y, color_indices = np.array([]), np.array([]), np.array([])
    l = 0
    for k in regmK:
        x = np.append(x, Regms[k][lsp1])
        y = np.append(y, Regms[k][lsp2])
        color_indices = np.append(color_indices, np.ones(len(Regms[k][lsp1])) * l)
        l += 1
    print(x, y)
    colormap = matplotlib.colors.ListedColormap(colors)
    return x, y, color_indices, colormap
# L1-S2

x1, y1, color_indices_1, colormap_1 = colourPlot(regmKeys[:14])
x2, y2, color_indices_2, colormap_2 = colourPlot(regmKeys[14:])

xlim = [min([min(x1), min(x2)]), max([max(x1), max(x2)])]
ylim = [min([min(y1), min(y2)]), max([max(y1), max(y2)])]

plt.figure(1)
scatter = plt.scatter(x1, y1, c=color_indices_1, cmap=colormap_1, s=np.ones(len(color_indices_1)) * 1)
plt.legend(handles=scatter.legend_elements()[0], labels=list(regmKeys[:14]), title="regmagplyts")
plt.xlabel('Mean Curvature')
plt.ylabel('Total Curvature')
ax = plt.gca()
ax.set_xlim(xlim)
ax.set_ylim(ylim)

plt.figure(2)
scatter = plt.scatter(x2, y2, c=color_indices_2, cmap=colormap_2, s=np.ones(len(color_indices_2)) * 1)
plt.legend(handles=scatter.legend_elements()[0], labels=list(regmKeys[14:]), title="regmagplyts")
plt.xlabel('Mean Curvature')
plt.ylabel('Total Curvature')
ax = plt.gca()
ax.set_xlim(xlim)
ax.set_ylim(ylim)