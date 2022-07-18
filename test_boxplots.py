from FunctionDataProcessing import scatter3d, calculate_pvalues, boxplots, corrMatrix, getData
import matplotlib.pyplot as plt
import numpy as np
Regms, regmKeys, LSPs = getData(dataset='S5')
remRegmKeys = np.array(["RegO", "RegC", "RegE", "RegP"])
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)


# print(data["NUN"])
def bp_LSP(dt, lsp):
    fig, ax = plt.subplots()
    ax.boxplot(dt[lsp])
    plt.xticks(np.arange(1, len(regmKeys) + 1, 1), regmKeys, rotation="vertical")
    plt.xlabel("Regmaglypts")
    #plt.savefig(r"/Users/lorenz_veithen/Desktop/HPD_Research/LSPS_Assessment/Boxplots/BP_"+lsp, dpi=100)

lsp = LSPs[4]
#for lsp in LSPs:
print(LSPs)

print(Regms[regmKeys[1]][LSPs[4]])
# Boxplots
data = boxplots(regmKeys, LSPs, Regms)
bp_LSP(data, lsp)
plt.ylabel('Total Curvature')