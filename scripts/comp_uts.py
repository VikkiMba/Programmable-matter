import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
fname = input('Please, enter file name: ')
if fname == 'done': quit()

data = np.loadtxt(fname, delimiter=',')

plt.xlabel('Composition')
plt.ylabel('UTS')
plt.title('UTS vs Extension')

plt.plot(data[3], data[0])
plt.plot(data[3], data[1])
plt.plot(data[3], data[2])
plt.show()