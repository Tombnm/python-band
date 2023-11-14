#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np

figx,figy,gamma,gamma_ticks = [],[],[],[]
tmp = []

#gamma data
with open("gamma.txt",'r+') as fd:
    for fread in fd.readlines():
        gamma.append(float(fread.split()[1]))
        gamma_ticks.append(fread.split()[0])
#print(gamma)
#print(gamma_ticks)

#x data
with open("band.txt",'r+') as fd:
    finda = "--"
    for fread in fd.readlines():
        if(fread.split()[1] != "--"):
            figx.append(float(fread.split()[0]))
        elif(fread.split()[1] == "--"):
            break

#y data
with open("band.txt",'r+') as fd:
    finda = "--"
    tmp.clear()
    for fread in fd.readlines():
        if(fread.split()[1] != "--"):
            tmp.append(float(fread.split()[1]))
        elif(fread.split()[1] == "--"):
            figy.append(tmp.copy())
            tmp.clear()
            continue

#print(figx)
#print(figy)

#bands
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for i in range(len(figy)):
    plt.plot(figx,figy[i],color = 'b')

#gamma
for i in range(len(gamma)):
    plt.plot([gamma[i],gamma[i]],[-10,10],color='grey',linestyle='--')
plt.plot([0,1],[0,0],color='grey',linestyle='--')

plt.xlim(0,1)
plt.ylim(-10,10)
plt.ylabel("Energy(eV)",fontsize=15)
plt.xticks([])
y_ticks = np.arange(-10,10.1,5)
plt.yticks(y_ticks)
ax.set_xticks(gamma)
ax.set_xticklabels(gamma_ticks,fontsize=15)



fig.savefig("./figure.svg")
