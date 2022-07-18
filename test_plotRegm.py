from FunctionDataProcessing import scatter3d, getData
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
sns.set_theme()
Regms, regmKeys, LSPs = getData(dataset='S15')
# ----------
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
# ----------

j = 1
k = 'RegC'
X = (np.array(Regms[k]["X"])-min(np.array(Regms[k]["X"])))*10**2
Y = (np.array(Regms[k]["Y"])-min(np.array(Regms[k]["Y"])))*10**2
Z = np.array(Regms[k]["MeanCurv"])
print(f"j={j}: {k}")
#scatter3d(X,Y,Z, j)
plt.figure(j)
array = np.ones((int(max(X)), int(max(Y))))*(min(Z)-1)
for x, y, z in zip(X, Y, Z):
    x = int(x)
    y = int(y)
    array[x - 1, y - 1] = z
plt.imshow(array, cmap=cmap, interpolation="nearest")
plt.grid(False)
plt.show()
j += 1

