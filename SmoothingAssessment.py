from FunctionDataProcessing import scatter3d, calculate_pvalues, boxplots, corrMatrix, getData
import matplotlib.pyplot as plt
import numpy as np
RegmsR = getData(dataset='R')[0]
RegmsS1 = getData(dataset='S1')[0]
RegmsS3 = getData(dataset='S3')[0]
RegmsS5 = getData(dataset='S5')[0]
RegmsS7 = getData(dataset='S7')[0]
RegmsS10 = getData(dataset='S10')[0]
RegmsS15 = getData(dataset='S15')[0]
RegmsDA, regmKeys, LSPs = getData(dataset='DA')
remRegmKeys = np.array(["RegO", "RegComp"])
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)


lsp = LSPs[3]
print(lsp)
#iterations = ['R', 'S1', 'S3', 'S5', 'S7', 'S10', 'S15']
iterations = ['S5', 'DA']
# To change
# Smooting assessment
i = 0
for k in regmKeys:
    fig = plt.figure(i)
    #bp = [RegmsR[k][lsp], RegmsS1[k][lsp], RegmsS3[k][lsp], RegmsS5[k][lsp], RegmsS7[k][lsp], RegmsS10[k][lsp], RegmsS15[k][lsp]]
    bp = [RegmsS5[k][lsp], RegmsDA[k][lsp]]

    plt.boxplot(bp, notch=True)
    plt.title(k)
    plt.xticks(np.arange(1, len(iterations) + 1, 1), iterations, rotation="vertical")
    plt.xlabel("Smoothing iteration.")
    #plt.savefig(r"/Users/lorenz_veithen/Desktop/HPD_Research/LSPS_Assessment/Boxplots/BP_"+lsp, dpi=100)
    plt.ylabel("Mean Curvature")
    i += 1