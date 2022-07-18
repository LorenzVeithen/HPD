from FunctionDataProcessing import getData, get_cmap
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

ALL = True
Regms, regmKeys, LSPs = getData(dataset='S5')
regmKeys = regmKeys[:14]
remRegmKeys = np.array(['RegO'])  # ["RegComp", "RegO", "RegP", "RegC", "RegE", "RegL2", "RegQ1"]
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)

if ALL:
    cmap = get_cmap(len(regmKeys))
    colors = [cmap(i) for i in range(0, len(regmKeys))]
    r=0
    i = 0
    for X in LSPs:
        j = 0
        lsp1 = X
        for Y in LSPs:
            lsp2 = Y
            if j > i:
                # do the plotting
                # make a coloured scattered plot
                plt.figure(r)
                x, y, color_indices = np.array([]), np.array([]), np.array([])
                l = 0
                for k in regmKeys:
                    x = np.append(x, Regms[k][lsp1])
                    y = np.append(y, Regms[k][lsp2])
                    color_indices = np.append(color_indices, np.ones(len(Regms[k][lsp1])) * l)
                    l += 1

                colormap = matplotlib.colors.ListedColormap(colors)
                print(regmKeys)
                scatter = plt.scatter(x, y, c=color_indices, cmap=colormap, s=np.ones(len(color_indices)) * 1)
                plt.legend(handles=scatter.legend_elements()[0], labels=list(regmKeys), title="regmagplyts")
                plt.xlabel(lsp1)
                plt.ylabel(lsp2)
                plt.savefig(r"/Users/lorenz_veithen/Desktop/HPD_Research/LSPS_Assessment/Colour/" + lsp1 + "vs" + lsp2 + "_A-K",
                            dpi=100)
            else:
                # do nothing
                pass
            j += 1
            r += 1
        i += 1
    print('---END---')
