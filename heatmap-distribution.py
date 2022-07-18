import numpy as np
import matplotlib.pyplot as plt
from FunctionDataProcessing import getData, heatMap

def makeHist(data):
    n = len(data)
    nbBins = int(np.ceil(np.sqrt(n)))
    print(np.sqrt(n), nbBins)
    counts, bins = np.histogram(data, bins=nbBins)
    i = 0; binPoints = []
    while i < len(bins) - 1:
        binPoint = (bins[i] + bins[i + 1]) / 2
        binPoints.append(binPoint)
        i += 1

    return binPoints, counts

Regms, regmKeys, LSPs = getData()
lsp1 = "MeanCurv"
lsp2 = "TanCurv"

# prep histogram

points1, counts1 = makeHist(Regms[regmKeys[1]][lsp1])
points2, counts2 = makeHist(Regms[regmKeys[1]][lsp2])

fig, ax1 = plt.subplots()
heatMap(Regms[regmKeys[1]][lsp1], Regms[regmKeys[1]][lsp2], ax1, 32)
ax2 = ax1.twinx()
#ax3 = ax1.twiny()

ax2.plot(points1, counts1, 'w-')
#ax3.plot(counts2, points2, 'w-')
plt.show()
