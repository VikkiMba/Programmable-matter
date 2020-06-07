import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
fname = input('Please, enter file name: ')
if fname == 'done': quit()
#data = pd.read_csv(fname)
#data.head()
data = np.loadtxt(fname, delimiter=',')

area = data[3]*data[4]
uts = data[0]/area

#print(uts)
plt.xlabel('Extension')
plt.ylabel('UTS')
plt.title('UTS vs Extension')
#plt.plot(uts, data[1]) 
plt.scatter(data[1], uts)
#plt.scatter(data[5], uts)
#plt.scatter(data[7], uts)
plt.show()
    

