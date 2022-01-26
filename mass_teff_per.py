#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:25:39 2021

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
print('# 13-150 Mjup transiting companions: ',len(lowmass['Name']))

msj = 0.000954588
rsj = 0.102763
######### Grieves 2021 #########

M2_148 = lowmass['M2'][lowmass['Name'] == 'TOI-148b'].values[0]
M2err_148 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['M2_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)
R2_148 = lowmass['R2'][lowmass['Name'] == 'TOI-148b'].values[0]
R2err_148 = np.array([lowmass['R2_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['R2_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)
teff_148 = lowmass['Teff'][lowmass['Name'] == 'TOI-148b'].values[0]
eteff_148 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)
feh_148 = lowmass['FeH'][lowmass['Name'] == 'TOI-148b'].values[0]
efeh_148 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)
ecc_148 = lowmass['ecc'][lowmass['Name'] == 'TOI-148b'].values[0]
ecce_148 = np.array([lowmass['ecc_err_low'][lowmass['Name'] == 'TOI-148b'].values[0],
                      lowmass['ecc_err_high'][lowmass['Name'] == 'TOI-148b'].values[0]]).reshape(2,1)

M2_587 = lowmass['M2'][lowmass['Name'] == 'TOI-587b'].values[0]
M2err_587 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
R2_587 = lowmass['R2'][lowmass['Name'] == 'TOI-587b'].values[0]
R2err_587 = np.array([lowmass['R2_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                   lowmass['R2_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
teff_587 = lowmass['Teff'][lowmass['Name'] == 'TOI-587b'].values[0]
eteff_587 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
feh_587 = lowmass['FeH'][lowmass['Name'] == 'TOI-587b'].values[0]
efeh_587 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)
ecc_587 = lowmass['ecc'][lowmass['Name'] == 'TOI-587b'].values[0]
ecce_587 = np.array([lowmass['ecc_err_low'][lowmass['Name'] == 'TOI-587b'].values[0],
                      lowmass['ecc_err_high'][lowmass['Name'] == 'TOI-587b'].values[0]]).reshape(2,1)

M2_681 = lowmass['M2'][lowmass['Name'] == 'TOI-681b'].values[0]
M2err_681= np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
R2_681 = lowmass['R2'][lowmass['Name'] == 'TOI-681b'].values[0]
R2err_681= np.array([lowmass['R2_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                   lowmass['R2_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
teff_681 = lowmass['Teff'][lowmass['Name'] == 'TOI-681b'].values[0]
eteff_681 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
feh_681 = lowmass['FeH'][lowmass['Name'] == 'TOI-681b'].values[0]
efeh_681 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)
ecc_681 = lowmass['ecc'][lowmass['Name'] == 'TOI-681b'].values[0]
ecce_681 = np.array([lowmass['ecc_err_low'][lowmass['Name'] == 'TOI-681b'].values[0],
                      lowmass['ecc_err_high'][lowmass['Name'] == 'TOI-681b'].values[0]]).reshape(2,1)


M2_746 = lowmass['M2'][lowmass['Name'] == 'TOI-746b'].values[0]
M2err_746 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
R2_746 = lowmass['R2'][lowmass['Name'] == 'TOI-746b'].values[0]
R2err_746 = np.array([lowmass['R2_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                   lowmass['R2_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
teff_746 = lowmass['Teff'][lowmass['Name'] == 'TOI-746b'].values[0]
eteff_746 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
feh_746 = lowmass['FeH'][lowmass['Name'] == 'TOI-746b'].values[0]
efeh_746 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)
ecc_746 = lowmass['ecc'][lowmass['Name'] == 'TOI-746b'].values[0]
ecce_746 = np.array([lowmass['ecc_err_low'][lowmass['Name'] == 'TOI-746b'].values[0],
                      lowmass['ecc_err_high'][lowmass['Name'] == 'TOI-746b'].values[0]]).reshape(2,1)

M2_1213 = lowmass['M2'][lowmass['Name'] == 'TOI-1213b'].values[0]
M2err_1213 = np.array([lowmass['M2_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                   lowmass['M2_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
R2_1213 = lowmass['R2'][lowmass['Name'] == 'TOI-1213b'].values[0]
R2err_1213 = np.array([lowmass['R2_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                   lowmass['R2_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
teff_1213 = lowmass['Teff'][lowmass['Name'] == 'TOI-1213b'].values[0]
eteff_1213 = np.array([lowmass['Teff_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                   lowmass['Teff_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
feh_1213 = lowmass['FeH'][lowmass['Name'] == 'TOI-1213b'].values[0]
efeh_1213 = np.array([lowmass['FeH_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                      lowmass['FeH_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)
ecc_1213 = lowmass['ecc'][lowmass['Name'] == 'TOI-1213b'].values[0]
ecce_1213 = np.array([lowmass['ecc_err_low'][lowmass['Name'] == 'TOI-1213b'].values[0],
                      lowmass['ecc_err_high'][lowmass['Name'] == 'TOI-1213b'].values[0]]).reshape(2,1)


##bds = pd.read_csv('substellar_pop_Carmichael_25sep2020.txt',sep=r"\s+",header=0)
#bds = pd.read_csv('transiting_BDs_1april2021.txt',sep=r"\s+",header=0)
#print(bds.columns)
#print('# Bds: ',len(bds['Name']))
##print(bds['Name'])
#
#comps = pd.read_csv('lowmassobject_ngedit_v2.csv',skiprows=[0,2],sep=',',header=0)
#print(comps.columns)
#
#M2 = comps['M2']
#M2el = comps['eM2']
#M2eh = comps['eM2_2']
#
#R2 = comps['R2']
#R2el = comps['eR2']
#R2eh = comps['eR2_2']
#
#teff = comps['Teff']
#teffel = comps['eTeff']
#teffeh = comps['eTeff_2']
#
#feh = comps['feh']
#fehel = comps['efeh_low']
#feheh = comps['efeh_hi']
#
#pers = comps['P']
#pers = np.array(pers).astype(np.float)
#
#ecc = comps['e'].copy()
#eccel = comps['ee'].copy()
#ecceh = comps['ee_2'].copy()
#
#ecc[comps['eflag'] == 'x'] = np.nan
#eccel[comps['eflag'] == 'x'] = np.nan
#ecceh[comps['eflag'] == 'x'] = np.nan
#
#ecc = np.array(ecc).astype(np.float)
#eccel = np.array(eccel).astype(np.float)
#ecceh = np.array(ecceh).astype(np.float)
#
#mcutl = 80
#mcuth = 150
#thecut = ((M2 > mcutl) & (M2 < mcuth))
#print('# low-mass stars initial: ',len(M2))
#print('# low-mass stars aftercut: ',len(M2[thecut]))
##print(comps['Name'][thecut])
#
#M2 = M2[thecut]
#M2el = M2el[thecut]
#M2eh = M2eh[thecut]
#R2 = R2[thecut]
#R2el = R2el[thecut]
#R2eh = R2eh[thecut]
#ecc = ecc[thecut]
#eccel = eccel[thecut]
#ecceh = ecceh[thecut]
#pers = pers[thecut]
#teff = teff[thecut]
#teffel = teffel[thecut]
#teffeh = teffeh[thecut]
#feh = feh[thecut]
#fehel = fehel[thecut]
#feheh = feheh[thecut]
#
#msj = 0.000954588
#rsj = 0.102763
#M2_sun = M2*msj
#R2_sun = R2*rsj
#M2el_sun = M2el*msj
#M2eh_sun = M2eh*msj
#R2el_sun = R2el*rsj
#R2eh_sun = R2eh*rsj
#
#
#
#
############## Indvidual stars ############
##TOI-148
#M2_148 = 77.1
#M2el_148 = 4.6
#M2eh_148 = 5.8
#M2err_148 = np.array([M2el_148,M2eh_148]).reshape(2,1)
#R2_148 = np.array(0.81)
#R2el_148 = 0.06
#R2eh_148 = 0.05
#R2err_148 = np.array([R2el_148,R2eh_148]).reshape(2,1)
#ecc_148 = 0.0052
#ecce_148 = np.array([0.0052,0.006]).reshape(2,1)
#per_148 = 4.867103
#teff_148 = 5990
#eteff_148 = np.array([140,140]).reshape(2,1)
#feh_148 = -0.24
#efeh_148 = np.array([0.25,0.25]).reshape(2,1)
#
##TOI-587
#M2_587 = 81.1
#M2err_587 = np.array([7.0,7.1]).reshape(2,1) #lower boundary first!
#R2_587 = 1.32
#R2err_587 = np.array([0.06,0.07]).reshape(2,1)
#ecc_587 = 0.051
#ecce_587 = np.array([0.036,0.049]).reshape(2,1)
#per_587 = 8.043450
#teff_587 = 9800
#eteff_587 = np.array([200,200]).reshape(2,1)
#feh_587 = 0.08
#efeh_587 = np.array([0.11,0.12]).reshape(2,1)
#
##TOI-681
#M2_681 = 88.7
#M2err_681 = np.array([2.3,2.5]).reshape(2,1)
#R2_681 = 1.52
#R2err_681 = np.array([0.15,0.25]).reshape(2,1)
#ecc_681 = 0.093
#ecce_681 = np.array([0.019,0.022]).reshape(2,1)
#per_681 = 15.778482
#teff_681 = 7440
#eteff_681 = np.array([140,150]).reshape(2,1)
#feh_681 = -0.08
#efeh_681 = np.array([0.05,0.05]).reshape(2,1)
#
##TOI-746
#M2_746 = 82.2
#M2err_746 = np.array([4.4,4.9]).reshape(2,1)
#R2_746 = 0.95
#R2err_746 = np.array([0.06,0.09]).reshape(2,1)
#ecc_746 = 0.1985
#ecce_746 = np.array([0.0031,0.0029]).reshape(2,1)
#per_746 = 10.980303
#teff_746 = 5690
#eteff_746 = np.array([140,140]).reshape(2,1)
#feh_746 = -0.02
#efeh_746 = np.array([0.23,0.23]).reshape(2,1)
#
#
##TOI-1213
#M2_1213 = 96.1
#M2err_1213 = np.array([3.7,4.6]).reshape(2,1)
#R2_1213 = 1.54
#R2err_1213 = np.array([0.59,0.99]).reshape(2,1)
#ecc_1213 = 0.4994
#ecce_1213 = np.array([0.0027,0.0030]).reshape(2,1)
#per_1213 = 27.214070
#teff_1213 = 5550
#eteff_1213 = np.array([150,150]).reshape(2,1)
#feh_1213  = 0.25
#efeh_1213  = np.array([0.15,0.14]).reshape(2,1)


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


#### plots ####
fsize = 28
fsize2 = 14
fsize3 = 20

####### Mass vs ecc

#m_combo = np.append(M2,bds['Mj'])
#m_combo = np.append(m_combo,[M2_148,M2_587,M2_681,M2_746,M2_1213])
#e_combo = np.append(ecc,bds['e'])
#e_combo = np.append(e_combo,[ecc_148,ecc_587,ecc_681,ecc_746,ecc_1213])
#p_combo = np.append(pers,bds['P'])
#p_combo = np.append(p_combo,[per_148,per_587,per_681,per_746,per_1213])
#p_combolog = np.log10(p_combo)
#teff_combo = np.append(teff,bds['Teff'])
#teff_combo = np.append(teff_combo,[teff_148,teff_587,teff_681,teff_746,teff_1213])
#

################ TEFF vs Mass ################

fig = plt.figure(figsize=(14,10))
grid = gridspec.GridSpec(20, 20)
grid.update(wspace=0.0, hspace=0.0) # set the spacing between axes. 
ax1 = fig.add_subplot(grid[3:,:17])
hist1 = fig.add_subplot(grid[:3,:17])

#fig,ax1 = plt.subplots(figsize=(14,10))


hist1.spines["top"].set_visible(False)  
hist1.spines["right"].set_visible(False)
hist1.spines["left"].set_visible(False)
hist1.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
hist1.xaxis.set_minor_formatter(ticker.NullFormatter())
hist1.set_xticks([])
hist1.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
hist1.yaxis.set_minor_formatter(ticker.NullFormatter())
hist1.set_yticks([])

#ax1.errorbar(bds['Teff'],bds['Mj'], 
#            xerr=np.array([bds['T_err'],bds['T_err']]),
#            yerr=np.array([bds['Mj_err_low'],bds['Mj_err_high']]),
#            fmt='b.',elinewidth=1.5,ms=10,label=r'13-80 M$_{\rm Jup}$')#,alpha=0.3)
#
#ax1.errorbar(teff,M2,xerr=np.array([teffel,teffeh]),
#             yerr=np.array([M2el,M2eh]),fmt='.',color='orange',
#             elinewidth=1.5,ms=10,label=r'80-150 M$_{\rm Jup}$')#,alpha=0.3)



## doubling the width of markers
#x = [0,2,4,6,8,10]
#y = [0]*len(x)
#s = [20*4**n for n in range(len(x))]
#plt.scatter(x,y,s=s)
#plt.show()

ax1.set_xlabel(r'Host Star T$_{\mathrm{eff}}$ [K]',fontsize=fsize)
ax1.set_ylabel(r'Companion Mass [M$_{\rm Jup}$]',fontsize=fsize)
ax1.tick_params(labelsize=fsize)

ax1.errorbar(teff_148,M2_148,xerr=eteff_148,yerr=M2err_148,fmt='r.',ms=1,label='This work',alpha=0.6)
ax1.scatter([],[], s=300/1, edgecolors='black',color='none',label='P = 1 day')
ax1.scatter([],[], s=300/10, edgecolors='black',color='none',label='P = 10 days')
ax1.scatter([],[], s=300/100, edgecolors='black',color='none',label='P = 100 days')

ax1.plot([],[],'b.',label=r'0.5-13 M$_{\rm Jup}$')
ax1.plot([],[],'k.',label=r'13-150 M$_{\rm Jup}$')

ax1.legend(fontsize=18)
ax1.text(teff_148,M2_148-4,'TOI-148',color='red',fontsize=fsize2)
ax1.errorbar(teff_587,M2_587,xerr=eteff_587,yerr=M2err_587,fmt='r.',ms=1,alpha=0.6)
ax1.text(teff_587,M2_587+2,'TOI-587',color='red',fontsize=fsize2)
ax1.errorbar(teff_681,M2_681,xerr=eteff_681,yerr=M2err_681,fmt='r.',ms=1,alpha=0.6)
ax1.text(teff_681,M2_681+1,'TOI-681',color='red',fontsize=fsize2)
ax1.errorbar(teff_746,M2_746,xerr=eteff_746,yerr=M2err_746,fmt='r.',ms=1,alpha=0.6)
ax1.text(teff_746,M2_746+2,'TOI-746',color='red',fontsize=fsize2)
ax1.errorbar(teff_1213,M2_1213,xerr=eteff_1213,yerr=M2err_1213,fmt='r.',ms=1,alpha=0.6)
ax1.text(teff_1213,M2_1213+1,'TOI-1213',color='red',fontsize=fsize2)

ax1.scatter(lowmass['Teff'],lowmass['M2'],s=300/lowmass['Period'],color='black',alpha=0.6)
ax1.scatter(teff_gp,mass_gp,s=300/period_gp,color='blue',alpha=0.3)


#Teff limits of spectral types:
#http://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt

ax1.axvline(10050,color='green',linestyle='--',alpha=0.6)
ax1.axvline(7310,color='green',linestyle='--',alpha=0.6)
ax1.axvline(5960,color='green',linestyle='--',alpha=0.6)
ax1.axvline(5325,color='green',linestyle='--',alpha=0.6)
ax1.axvline(3890,color='green',linestyle='--',alpha=0.6)
ax1.axvline(2310,color='green',linestyle='--',alpha=0.6)

ax1.text(3000,10,'M',color='green',fontsize=fsize)
ax1.text(4500,10,'K',color='green',fontsize=fsize)
ax1.text(5450,10,'G',color='green',fontsize=fsize)
ax1.text(6600,10,'F',color='green',fontsize=fsize)
ax1.text(8600,10,'A',color='green',fontsize=fsize)
ax1.text(10300,10,'B',color='green',fontsize=fsize)

ax1.tick_params(bottom=True, top=True, left=True, right=False)
ax1.tick_params(axis="x", direction="in", length=8, width=2)

ax1.set_xlim(1900,10800)
hist1.set_xlim(1900,10800)

binwidth = 500
hmin = 2000
hmax = 12000

hist,bin_edges = np.histogram(lowmass['Teff'],bins=np.arange(hmin,hmax,binwidth))
hist = hist/np.sum(hist)
hist1.bar((bin_edges[:-1]+binwidth/2.0), hist,width=binwidth,color='black',alpha=0.3,edgecolor='black')#,label=r'80-150 M$_{\rm Jup}$')
#maxlowmass=np.max(hist)

hist,bin_edges = np.histogram(teff_gp,bins=np.arange(hmin,hmax,binwidth))
hist = hist/np.sum(hist)#*maxlowmass
#hist1.bar((bin_edges[:-1]+binwidth/2.0), hist,width=binwidth,color='blue',alpha=0.3,edgecolor='black',hatch='*',label=r'0.5-13 M$_{\rm Jup}$')
#hist1.legend()
hist1.bar((bin_edges[:-1]+binwidth/2.0), hist,width=binwidth,color='blue',alpha=0.3,edgecolor='black',label=r'0.5-13 M$_{\rm Jup}$')

plt.tight_layout()

plt.savefig('plots/BDsLMS_Teff_mass_per_withexo.pdf')
