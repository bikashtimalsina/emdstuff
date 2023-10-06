from pylab import *
from ase.build import graphene_nanoribbon
from ase.io import read,write
from gpyumd.load import load_hac
from gpyumd.atoms import GpumdAtoms
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

aw = 2
fs = 16
font = {'size'   : fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes' , linewidth=aw)

def set_fig_properties(ax_list):
    tl = 8
    tw = 2
    tlm = 4
    
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='in', right=True, top=True)

rundir=glob.glob("./Run[0-9]*")
rundir_hac=[]
for i in range(len(rundir)):
    dirlist=os.listdir(rundir[i])
    for j in range(len(dirlist)):
        if dirlist[j] == 'hac.out':
            rundir_hac.append(rundir[i])
rundir_hac_out=[rundir_hac[i]+"/hac.out" for i in range(len(rundir_hac))]
heat_current=[]
for i in range(len(rundir_hac_out)):
    hac=load_hac([50000]*1,[10]*1,rundir_hac_out[i])
    heat_current.append(hac)
print(hac.keys())
kappa_in=[]
kappa_out=[]
kxx=[]
kyy=[]
kzz=[]
for i in range(len(heat_current)):
    t=heat_current[0]['run0']['t']
    hac_ave_i=np.zeros(hac['run0']['jxijx'].shape[0])
    hac_ave_o=np.zeros_like(hac_ave_i)
    ki_ave, ko_ave=np.zeros_like(hac_ave_i),np.zeros_like(hac_ave_o)
    for runkey in hac.keys():
        hac_ave_i += heat_current[i][runkey]['jxijx']+heat_current[i][runkey]['jyijy']
        hac_ave_o += heat_current[i][runkey]['jxojx']+heat_current[i][runkey]['jyojy']
        ki_ave += (heat_current[i][runkey]['kxi']+heat_current[i][runkey]['kyi'])/2
        ko_ave += (heat_current[i][runkey]['kxo']+heat_current[i][runkey]['kyo'])/2+heat_current[i][runkey]['kz']
    hac_ave_i /= hac_ave_i.max()
    hac_ave_o /= hac_ave_o.max()
    kappa_in.append(ki_ave)
    kappa_out.append(ko_ave)
kappa_in_ave=[]
kappa_out_ave=[]
for j in range(len(kappa_in[0])):
    kappa_ens_in_total=0
    kappa_ens_out_total=0
    for i in range(len(kappa_in)):
        kappa_ens_in_total += kappa_in[i][j]
        kappa_ens_out_total += kappa_out[i][j]
    kappa_in_ave.append(kappa_ens_in_total/len(kappa_in))
    kappa_out_ave.append(kappa_ens_out_total/len(kappa_in))
plt.plot(t,kappa_in[0],color='C7',alpha=0.5)
plt.plot(t,kappa_in[1],color='C7',alpha=0.5)
plt.plot(t,kappa_in[2],color='C7',alpha=0.5)
plt.plot(t,kappa_in[3],color='C7',alpha=0.5)
plt.plot(t,kappa_in[4],color='C7',alpha=0.5)
#plt.plot(t,kappa_in[5],color='C7',alpha=0.5)
#plt.plot(t,kappa_in[6],color='C7',alpha=0.5)
#plt.plot(t,kappa_in[7],color='C7',alpha=0.5)
#plt.plot(t,kappa_in[8],color='C7',alpha=0.5)
#plt.plot(t,kappa_in[9],color='C7',alpha=0.5)
#plt.plot(t,kappa_in_ave,color='C3',linewidth=2)
#plt.ylim([0,50])
plt.show()
plt.plot(t,kappa_out[0],color='C7',alpha=0.5)
plt.plot(t,kappa_out[1],color='C7',alpha=0.5)
plt.plot(t,kappa_out[2],color='C7',alpha=0.5)
plt.plot(t,kappa_out[3],color='C7',alpha=0.5)
plt.plot(t,kappa_out[4],color='C7',alpha=0.5)
#plt.plot(t,kappa_out[5],color='C7',alpha=0.5)
#plt.plot(t,kappa_out[6],color='C7',alpha=0.5)
#plt.plot(t,kappa_out[7],color='C7',alpha=0.5)
#plt.plot(t,kappa_out[8],color='C7',alpha=0.5)
#plt.plot(t,kappa_out[9],color='C7',alpha=0.5)
#plt.plot(t,kappa_out_ave,color='C3',linewidth=2)
#plt.ylim([0,25])
plt.show()
