import math
import matplotlib.pyplot as plt

p = 2*math.pi
N = 10
def f(x):
    return math.sin(x)
x = []
y = []
for i in range(N):
    x.append(f(0 + i*p/N))
    y.append(f(0 + i*p/N))
    
#fig, ax = plt.subplots()             # Create a figure containing a single Axes.
#ax.plot(x, y)  # Plot some data on the Axes.
#plt.show() 

print(x)
