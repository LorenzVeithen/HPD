from FunctionDataProcessing import getData, get_cmap
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import pearsonr
Regms, regmKeys, LSPs = getData(dataset='S5')
remRegmKeys = np.array(["RegO", "RegC", "RegE", "RegP", "RegComp"])
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)

print(regmKeys)

j=0
for lsp in LSPs:
    avglsp = np.array([])
    areas = []
    i = 0
    for k in regmKeys:
        areas.append(Regms[k]["Area"])
        avglsp = np.append(avglsp, np.mean(Regms[k][lsp]))
        i += 1

    plt.figure(j)
    plt.scatter(areas, avglsp)
    #for i in range(1, len(regmKeys), 1):
    #    regmKeys[i] = regmKeys[i][3:]

    for i, txt in enumerate(regmKeys):
        plt.annotate(txt, (areas[i], avglsp[i]))
    plt.title("Correlation coefficient= " + f"{np.round(pearsonr(areas, avglsp)[0], 3)}" + "; p = " + f"{np.round(pearsonr(areas, avglsp)[1], 3)}")
    plt.xlabel("Areas")
    plt.ylabel("Regmaglypt avg " + lsp)
    plt.grid(True)
    plt.savefig(r"/Users/lorenz_veithen/Desktop/HPD_Research/LSPS_Assessment/AreaScatter/"+lsp+"vsArea", dpi=100)
    plt.show()
    j += 1
