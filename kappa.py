from pylab import *
from ase.build import graphene_nanoribbon
from ase.io import read,write
from gpyumd.load import load_hac
from gpyumd.atoms import GpumdAtoms
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

rundir=glob.glob("./Run[0-9]*")
rundir_hac=[]
for i in range(len(rundir)):
    dirlist=os.listdir(rundir[i])
    for j in range(len(dirlist)):
        if dirlist[j]=='hac.out':
            rundir_hac.append(rundir[i])
rundir_hac_out=[rundir_hac[i]+"/hac.out" for i in range(len(rundir_hac))]
hac_current=[]
for i in range(len(rundir)):
    hac=load_hac([50000]*1,[10]*1,rundir_hac_out[i])
    hac_current.append(hac)
kxx=[]
kyy=[]
kzz=[]
for j in range(len(hac_current[i]['run0']['t'])):
    kxx_avg=0
    kyy_avg=0
    kzz_avg=0
    for i in range(len(hac_current)):
        kxx_avg += (hac_current[i]['run0']['kxi'][j]+hac_current[i]['run0']['kxo'][j])
        kyy_avg += (hac_current[i]['run0']['kyi'][j]+hac_current[i]['run0']['kyo'][j])
        kzz_avg += hac_current[i]['run0']['kz'][j]
    kxx_avg = kxx_avg/len(hac_current)
    kyy_avg = kyy_avg/len(hac_current)
    kzz_avg = kzz_avg/len(hac_current)
    kxx.append(kxx_avg)
    kyy.append(kyy_avg)
    kzz.append(kzz_avg)
t=hac_current[0]['run0']['t']
plt.plot(t,kxx,color='red')
plt.plot(t,kyy,color='blue')
plt.plot(t,kzz,color='green')
plt.show()      
