import math
import matplotlib.pyplot as plt

#chapter 10 Rogawski Review, problem 29. plotting the curve

def f1(x):
    y = 4 - math.exp((-2)*x)
    return y

y = []
x = []
n = 100
for i in range(0,n):
    x.append(i)
    y.append(f1(i))

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(x, y)  # Plot some data on the Axes.
plt.show() 