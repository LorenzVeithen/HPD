import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from FunctionDataProcessing import scatter3d, calculate_pvalues, boxplots, corrMatrix, getData
import statistics as s
import glob

Regms, regmKeys, LSPs = getData(dataset='3')
# Remove unnecessary LSPs
remLSPs = np.array(["NUN", "EP", "SAR", "Slope"]) # LSPs to remove
LSPs = np.setdiff1d(LSPs, remLSPs)

# Matrix
# First combine all regmaglypts
print(regmKeys)
remRegmKeys = np.array(["RegO", "RegComp"])
regmKeys = np.setdiff1d(regmKeys, remRegmKeys)
corrFrame1, pvalFrame1 = corrMatrix(Regms, LSPs, regmKeys, mode=1)
print(corrFrame1, pvalFrame1)
# Find correlation coefficients per regmaglypt

# not efficient but whatever
# regmKeys that you want to use
corrPerRegm = {}
for param1 in LSPs:
    for param2 in LSPs:
        if param1 == param2:
            pass
        else:
            corrPerRegm[param1 + "vs" + param2] = []
            for k in regmKeys:
                regmCoeff = np.corrcoef(Regms[k][param1], Regms[k][param2])[0, 1]
                corrPerRegm[param1 + "vs" + param2].append(regmCoeff)

print(corrPerRegm["DFMEvsMeanCurv"])
print(s.fmean(corrPerRegm["DFMEvsMeanCurv"]))
print(s.stdev(corrPerRegm["DFMEvsMeanCurv"]))

# Take each versus and find the average
# Find the standard deviation (large variations indicate a bad LSP or bad delineation of some regmaglypts)
# Make a coloured matrix with the distance of each remgmaglypt with respect to the mean to see if it is due to bad delineation or due to bad LSP

# Probably need to reduce the total number of LSPs to make it possible to use by hand

# What if instead of comparing the values from the total surfaces, we compare the values per regmaglypt as a data set ?