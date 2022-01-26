#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:44:01 2021

@author: nolangrieves
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

lowmass = pd.read_csv('13-150Mjuptransitingcompanions.csv',sep=',',header=0,skiprows=[1])
print(lowmass.columns)
print('# 13-15 Mjup transiting companions: ',len(lowmass['Name']))

#tmig_lowmass = lowmass['M2']**-1.0 * lowmass['M1']**(8.0/3.0) * lowmass['R1']**-5.0 * lowmass['Period']**(13.0/3.0)


######### Grieves 2021 #########

M2_148 = lowmass['M2'][lowmass['Name'] == 'TOI-148b'].values[0]
M2err_148 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['M2_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)
teff_148 = lowmass['Teff'][lowmass['Name'] == 'TOI-148b'].values[0]
eteff_148 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)

feh_148 = lowmass['FeH'][lowmass['Name'] == 'TOI-148b'].values[0]
efeh_148 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)



M2_587 = lowmass['M2'][lowmass['Name'] == 'TOI-587b'].values[0]
M2err_587 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
teff_587 = lowmass['Teff'][lowmass['Name'] == 'TOI-587b'].values[0]
eteff_587 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
feh_587 = lowmass['FeH'][lowmass['Name'] == 'TOI-587b'].values[0]
efeh_587 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)

M2_681 = lowmass['M2'][lowmass['Name'] == 'TOI-681b'].values[0]
M2err_681= np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
teff_681 = lowmass['Teff'][lowmass['Name'] == 'TOI-681b'].values[0]
eteff_681 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
feh_681 = lowmass['FeH'][lowmass['Name'] == 'TOI-681b'].values[0]
efeh_681 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)


M2_746 = lowmass['M2'][lowmass['Name'] == 'TOI-746b'].values[0]
M2err_746 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
teff_746 = lowmass['Teff'][lowmass['Name'] == 'TOI-746b'].values[0]
eteff_746 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
feh_746 = lowmass['FeH'][lowmass['Name'] == 'TOI-746b'].values[0]
efeh_746 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)

M2_1213 = lowmass['M2'][lowmass['Name'] == 'TOI-1213b'].values[0]
M2err_1213 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
teff_1213 = lowmass['Teff'][lowmass['Name'] == 'TOI-1213b'].values[0]
eteff_1213 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
feh_1213 = lowmass['FeH'][lowmass['Name'] == 'TOI-1213b'].values[0]
efeh_1213 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)



######### Exoplanets ###########

exop = pd.read_csv('PS_2021.04.13_12.38.17.csv',sep=',',header=292)
pname = exop['pl_name']
list(exop.columns)
mass_planet = exop['pl_bmassj']
mass_ue = np.array(abs(exop['pl_bmassjerr1']))
mass_le = np.array(abs(exop['pl_bmassjerr2']))

giantpcut = ((exop['pl_bmassj'] > 0.5) &
             (exop['pl_bmassj'] < 13.0) &
             (exop['rv_flag'] == 1) &
             (exop['tran_flag'] == 1))

mass_gp = exop['pl_bmassj'][giantpcut]
metal_gp = exop['st_met'][giantpcut]
teff_gp = exop['st_teff'][giantpcut]
period_gp = exop['pl_orbper'][giantpcut]
mstar_gp = exop['st_rad'][giantpcut]
rstar_gp = exop['st_mass'][giantpcut]

#tmig_gp = mass_gp**-1.0 * mstar_gp**(8.0/3.0) * rstar_gp**-5.0 * period_gp**(13.0/3.0)

#### plots ####
fsize = 28
fsize2 = 14
fsize3 = 20

################ [Fe/H] vs Mass ################

#fig = plt.figure(figsize=(18,14))
fig = plt.figure(figsize=(14,10))
grid = gridspec.GridSpec(20, 20)
grid.update(wspace=0.0, hspace=0.0) # set the spacing between axes. 
ax1 = fig.add_subplot(grid[3:,:17])
hist1 = fig.add_subplot(grid[:3,:17])


hist1.spines["top"].set_visible(False)  
hist1.spines["right"].set_visible(False)
hist1.spines["left"].set_visible(False)
hist1.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
hist1.xaxis.set_minor_formatter(ticker.NullFormatter())
hist1.set_xticks([])
hist1.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
hist1.yaxis.set_minor_formatter(ticker.NullFormatter())
hist1.set_yticks([])

#ax1.plot(metal_gp,mass_gp,'b.',label=r'0.5-13 M$_{\rm Jup}$')

#ax1.errorbar(lowmass['FeH'],lowmass['M2'], 
#            xerr=np.array([lowmass['FeH_err_low'],lowmass['FeH_err_high']]),
#            yerr=np.array([lowmass['M2_err_low'],lowmass['M2_err_high']]),
#            fmt='k.',elinewidth=1.5,ms=10,label=r'13-150 M$_{\rm Jup}$')#,alpha=0.3)

#ax1.errorbar(lowmass['FeH'],lowmass['M2'], 
#            xerr=np.array([lowmass['FeH_err_low'],lowmass['FeH_err_high']]),
#            yerr=np.array([lowmass['M2_err_low'],lowmass['M2_err_high']]),
#            fmt='k.',elinewidth=1.5,ms=10,label=r'13-150 M$_{\rm Jup}$')#,alpha=0.3)
#
#ax1.errorbar(lowmass['FeH'][lowmass['M2'] < 42.5],lowmass['M2'][lowmass['M2'] < 42.5], 
#            xerr=np.array([lowmass['FeH_err_low'][lowmass['M2'] < 42.5],lowmass['FeH_err_high'][lowmass['M2'] < 42.5]]),
#            yerr=np.array([lowmass['M2_err_low'][lowmass['M2'] < 42.5],lowmass['M2_err_high'][lowmass['M2'] < 42.5]]),
#            fmt='g.',elinewidth=1.5,ms=10,label=r'13-42.5 M$_{\rm Jup}$')#,alpha=0.3)

cut1 = 42.5
cut2 = 80

ax1.errorbar(lowmass['FeH'][lowmass['M2'] < cut1],lowmass['M2'][lowmass['M2'] < cut1], 
            xerr=np.array([lowmass['FeH_err_low'][lowmass['M2'] < cut1],lowmass['FeH_err_high'][lowmass['M2'] < cut1]]),
            yerr=np.array([lowmass['M2_err_low'][lowmass['M2'] < cut1],lowmass['M2_err_high'][lowmass['M2'] < cut1]]),
            fmt='g.',elinewidth=1.5,ms=10,label=r'13-42.5 M$_{\rm Jup}$')#,alpha=0.3)

ax1.errorbar(lowmass['FeH'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)],lowmass['M2'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)], 
            xerr=np.array([lowmass['FeH_err_low'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)],lowmass['FeH_err_high'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)]]),
            yerr=np.array([lowmass['M2_err_low'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)],lowmass['M2_err_high'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)]]),
            fmt='b.',elinewidth=1.5,ms=10,label=r'42.5-80 M$_{\rm Jup}$')#,alpha=0.3)

ax1.errorbar(lowmass['FeH'][lowmass['M2'] > cut2],lowmass['M2'][lowmass['M2'] > cut2], 
            xerr=np.array([lowmass['FeH_err_low'][lowmass['M2'] > cut2],lowmass['FeH_err_high'][lowmass['M2'] > cut2]]),
            yerr=np.array([lowmass['M2_err_low'][lowmass['M2'] > cut2],lowmass['M2_err_high'][lowmass['M2'] > cut2]]),
            fmt='k.',elinewidth=1.5,ms=10,label=r'80-150 M$_{\rm Jup}$')#,alpha=0.3)





ax1.set_xlabel(r'Host Star [Fe/H]',fontsize=fsize)
ax1.set_ylabel(r'Companion Mass [M$_{\rm Jup}$]',fontsize=fsize)
ax1.tick_params(labelsize=fsize)

ax1.errorbar(feh_148,M2_148,xerr=efeh_148,yerr=M2err_148,fmt='r.',ms=10,label='This work')
ax1.legend(fontsize=18)

ax1.text(feh_148-0.1,M2_148-5,'TOI-148',color='red',fontsize=fsize2)
ax1.errorbar(feh_587,M2_587,xerr=efeh_587,yerr=M2err_587,fmt='r.',ms=10)
ax1.text(feh_587+0.02,M2_587-5,'TOI-587',color='red',fontsize=fsize2)
ax1.errorbar(feh_681,M2_681,xerr=efeh_681,yerr=M2err_681,fmt='r.',ms=10)
ax1.text(feh_681-0.1,M2_681+2,'TOI-681',color='red',fontsize=fsize2)
ax1.errorbar(feh_746,M2_746,xerr=efeh_746,yerr=M2err_746,fmt='r.',ms=10)
ax1.text(feh_746,M2_746+2,'TOI-746',color='red',fontsize=fsize2)
ax1.errorbar(feh_1213,M2_1213,xerr=efeh_1213,yerr=M2err_1213,fmt='r.',ms=10)
ax1.text(feh_1213+0.01,M2_1213+2,'TOI-1213',color='red',fontsize=fsize2)
#ax1.xaxis.tick_top()
ax1.set_xlim(-0.7,0.55)
hist1.set_xlim(-0.7,0.55)

#x.tick_params(axis="x", direction="in", length=16, width=2, color="turquoise")
#ax1.tick_params(axis="x", length=16, width=2, color="turquoise")
ax1.tick_params(bottom=True, top=True, left=True, right=False)
ax1.tick_params(axis="x", direction="in", length=8, width=2)
      

#planets

binwidth = 0.1
hmin = -0.7
hmax = 0.7
#hist,bin_edges = np.histogram(metal_gp,bins=np.arange(hmin,hmax,binwidth))
#hist = hist/np.sum(hist)
#hist1.bar((bin_edges[:-1]+binwidth/2), hist,width=binwidth,color='blue',alpha=0.1,edgecolor='blue')



hist,bin_edges = np.histogram(lowmass['FeH'][lowmass['M2'] < cut1],bins=np.arange(hmin,hmax,binwidth))
#hist = hist/np.sum(hist)
hist1.bar((bin_edges[:-1]+binwidth/2),hist,width=binwidth,color='green',alpha=0.3,edgecolor='black',hatch='/',label=r'13-42.5 M$_{\rm Jup}$')

hist,bin_edges = np.histogram(lowmass['FeH'][(lowmass['M2'] > cut1) & (lowmass['M2'] < cut2)],bins=np.arange(hmin,hmax,binwidth))
#hist = hist/np.sum(hist)
hist1.bar((bin_edges[:-1]+binwidth/2),hist,width=binwidth,color='blue',alpha=0.3,edgecolor='black',label=r'42.5-80 M$_{\rm Jup}$')


#BDs
hist,bin_edges = np.histogram(lowmass['FeH'][lowmass['M2'] > cut2],bins=np.arange(hmin,hmax,binwidth))
#hist = hist/np.sum(hist)
hist1.bar((bin_edges[:-1]+binwidth/2),hist,width=binwidth,color='none',alpha=0.3,edgecolor='black',hatch='*',label=r'80-150 M$_{\rm Jup}$')


hist1.legend(fontsize=12)
#hist,bin_edges = np.histogram(lowmass['FeH'][lowmass['M2'] > 80],bins=np.arange(hmin,hmax,binwidth))
#hist = hist/np.sum(hist)
#hist1.bar((bin_edges[:-1]+binwidth/2),hist,width=binwidth,color='black',alpha=0.3,edgecolor='black',label=r'13-80 M$_{\rm Jup}$')

plt.tight_layout()
plt.savefig('plots/feh_mass.pdf')