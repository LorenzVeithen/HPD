from FunctionDataProcessing import scatter3d, calculate_pvalues, boxplots, corrMatrix, getData
import matplotlib.pyplot as plt
import numpy as np
Regms, regmKeys, LSPs = getData()

# Let's get a simple heatmap first, for one regmaglypt
fig, ax = plt.subplots()
ax.scatter(Regms[regmKeys[1]]["MeanCurv"], Regms[regmKeys[1]]["Slope"])


# Generate some test data
fig, ax = plt.subplots()
x = Regms[regmKeys[1]]["MeanCurv"]
y = Regms[regmKeys[1]]["Slope"]

heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap.T, origin='lower')
plt.show()