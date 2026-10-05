import numpy
import scipy
import csv
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("menu-breakdown-may1-27-2021.csv",delimiter = ",",index_col = False)

df.dropna(subset = ["Item Name"],inplace = True)
x = df["Avg Price"]
y = df["Quantity"]
p = df["Item Name"]

plt.figure()
plt.scatter(x,(100*y/sum(y)))
plt.show()
        
