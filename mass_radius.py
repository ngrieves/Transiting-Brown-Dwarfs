#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:23:02 2021

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
      
############## BHAC15 Isochrones ################
#http://perso.ens-lyon.fr/isabelle.baraffe/
#http://perso.ens-lyon.fr/isabelle.baraffe/COND03_models
#http://perso.ens-lyon.fr/isabelle.baraffe/BHAC15dir/
###### 0.1 Gyr #######
bhac_01 = pd.read_csv('model_isochrones/BHAC15_01Gyr.txt',skiprows=4,sep=r"\s+",header=None)
#print(bhac_01.columns)
m_bhac_01 = bhac_01[0]
r_bhac_01 = bhac_01[4]
cond_01 = pd.read_csv('model_isochrones/COND03_01Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_cond_01 = cond_01[0]
r_cond_01 = cond_01[4]
#r_cond_01 = r_cond_01[m_cond_01 < min(m_bhac_01)]
#m_cond_01 = m_cond_01[m_cond_01 < min(m_bhac_01)]
r_bhac_01 = r_bhac_01[m_bhac_01 > max(m_cond_01)]
m_bhac_01 = m_bhac_01[m_bhac_01 > max(m_cond_01)]
m_01 = np.append(m_cond_01,m_bhac_01,)
r_01 = np.append(r_cond_01,r_bhac_01,)

###### 0.5 Gyr #######
bhac_05 = pd.read_csv('model_isochrones/BHAC15_05Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_bhac_05 = bhac_05[0]
r_bhac_05 = bhac_05[4]
cond_05 = pd.read_csv('model_isochrones/COND03_05Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_cond_05 = cond_05[0]
r_cond_05 = cond_05[4]
r_bhac_05 = r_bhac_05[m_bhac_05 > max(m_cond_05)]
m_bhac_05 = m_bhac_05[m_bhac_05 > max(m_cond_05)]
m_05 = np.append(m_cond_05,m_bhac_05,)
r_05 = np.append(r_cond_05,r_bhac_05,)


###### 1 Gyr #######
bhac_1 = pd.read_csv('model_isochrones/BHAC15_1Gyr.txt',skiprows=4,sep=r"\s+",header=None)
#print(bhac_01.columns)
m_bhac_1 = bhac_1[0]
r_bhac_1 = bhac_1[4]
cond_1 = pd.read_csv('model_isochrones/COND03_1Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_cond_1 = cond_1[0]
r_cond_1 = cond_1[4]
#r_cond_1 = r_cond_1[m_cond_1 < min(m_bhac_1)]
#m_cond_1 = m_cond_1[m_cond_1 < min(m_bhac_1)]
r_bhac_1 = r_bhac_1[m_bhac_1 > max(m_cond_1)]
m_bhac_1 = m_bhac_1[m_bhac_1 > max(m_cond_1)]
m_1 = np.append(m_cond_1,m_bhac_1)
r_1 = np.append(r_cond_1,r_bhac_1)
#f_1 = interpolate.interp1d(m_1,r_1)
#x_1 = np.arange(min(m_1),max(m_1),0.01)
#y_1 = f_1(x_1)

###### 5 Gyr #######
bhac_5 = pd.read_csv('model_isochrones/BHAC15_5Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_bhac_5 = bhac_5[0]
r_bhac_5 = bhac_5[4]
cond_5 = pd.read_csv('model_isochrones/COND03_5Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_cond_5 = cond_5[0]
r_cond_5 = cond_5[4]
#r_cond_5 = r_cond_5[m_cond_5 < min(m_bhac_5)]
#m_cond_5 = m_cond_5[m_cond_5 < min(m_bhac_5)]
r_bhac_5 = r_bhac_5[m_bhac_5 > max(m_cond_5)]
m_bhac_5 = m_bhac_5[m_bhac_5 > max(m_cond_5)]
m_5 = np.append(m_cond_5,m_bhac_5)
r_5 = np.append(r_cond_5,r_bhac_5)

###### 10 Gyr #######
bhac_10 = pd.read_csv('model_isochrones/BHAC15_10Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_bhac_10 = bhac_10[0]
r_bhac_10 = bhac_10[4]
cond_10 = pd.read_csv('model_isochrones/COND03_10Gyr.txt',skiprows=4,sep=r"\s+",header=None)
m_cond_10 = cond_10[0]
r_cond_10 = cond_10[4]
#r_cond_10 = r_cond_10[m_cond_10 < min(m_bhac_10)]
#m_cond_10 = m_cond_10[m_cond_10 < min(m_bhac_10)]
r_bhac_10 = r_bhac_10[m_bhac_10 > max(m_cond_10)]
m_bhac_10 = m_bhac_10[m_bhac_10 > max(m_cond_10)]

m_10 = np.append(m_cond_10,m_bhac_10)
r_10 = np.append(r_cond_10,r_bhac_10)


####### plots #######

xlolim = 0.0
xuplim = 155*0.000954588 #0.22#0.30

ylolim = 0.05
yuplim = 0.28#0.3

fsize = 28
fsize2 = 14
fsize3 = 20

fig = plt.figure(figsize=(11,8))
#ax1 = fig.add_subplot(111)

##### addd top histogram
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

#hist1.set_ylim([ylolim,yuplim])
hist1.set_xlim([xlolim/msj,xuplim/msj])

#ax1.set_xlim(-0.7,0.55)
#hist1.set_xlim(-0.7,0.55)


#M2_new = np.array([M2_148,M2_587,M2_681,M2_746,M2_1213])
#masscombo1 = np.concatenate((np.array(bds['Mj']),np.array(M2)))
#masscombo = np.concatenate((masscombo1,M2_new))

binwidth = 10
hmin = 0
hmax = 200

#hist,bin_edges = np.histogram(masscombo,bins=np.arange(hmin,hmax,binwidth))
hist,bin_edges = np.histogram(lowmass['M2'],bins=np.arange(hmin,hmax,binwidth))
#binwidth = (bin_edges[1]-bin_edges[0])
#hist = hist/np.sum(hist)
hist1.bar((bin_edges[:-1]+binwidth/2.0), hist,width=binwidth,color='black',alpha=0.3,edgecolor='black')#,label=r'80-150 M$_{\rm Jup}$')





ax1.plot(m_01,r_01,linestyle='-',color='orange',label='0.1 Gyr')
ax1.plot(m_05,r_05,linestyle=':',color='g',label='0.5 Gyr')
ax1.plot(m_1,r_1,linestyle='-.',color='c',label='1 Gyr')
ax1.plot(m_5,r_5,linestyle='--',color='m',label='5 Gyr')
ax1.plot(m_10,r_10,linestyle='-',color='b',label='10 Gyr')
ax1.legend(loc='lower right')
#ax1.plot(M2_sun, R2_sun,'k.')
#ax1.errorbar(M2_sun,R2_sun, xerr=np.array([M2el_sun,M2eh_sun]),
#             yerr=np.array([R2el_sun,R2eh_sun]),fmt='k.',elinewidth=1.5,ms=5,alpha=0.6)

nogrieves = ((lowmass['Name'] != 'TOI-148b') & 
             (lowmass['Name'] != 'TOI-587b') &
             (lowmass['Name'] != 'TOI-681b') &
             (lowmass['Name'] != 'TOI-746b') &
             (lowmass['Name'] != 'TOI-1213b'))

m2_nogrieves = (lowmass['M2']*msj)[nogrieves]
m2_err_low_nogrieves = (lowmass['M2_err_low']*msj)[nogrieves]
m2_err_high_nogrieves = (lowmass['M2_err_high']*msj)[nogrieves]

r2_nogrieves = (lowmass['R2']*rsj)[nogrieves]
r2_err_low_nogrieves = (lowmass['R2_err_low']*rsj)[nogrieves]
r2_err_high_nogrieves = (lowmass['R2_err_high']*rsj)[nogrieves]

ax1.errorbar(m2_nogrieves,r2_nogrieves, 
            xerr=np.array([m2_err_low_nogrieves,m2_err_high_nogrieves]),
            yerr=np.array([r2_err_low_nogrieves,r2_err_high_nogrieves]),
            fmt='k.',elinewidth=1.5,ms=8,label=r'13-42.5 M$_{\rm Jup}$',alpha=0.8)

#ax1.errorbar(lowmass['M2']*msj,lowmass['R2']*rsj, 
#            xerr=np.array([lowmass['M2_err_low']*msj,lowmass['M2_err_high']*msj]),
#            yerr=np.array([lowmass['R2_err_low']*rsj,lowmass['R2_err_high']*rsj]),
#            fmt='k.',elinewidth=1.5,ms=10,label=r'13-42.5 M$_{\rm Jup}$',alpha=0.8)


ax1.tick_params(labelsize=fsize3)
ax1.tick_params(labelsize=fsize3)
ax1.set_xlabel(r'Mass [M$_{\odot}$]',fontsize=fsize)
ax1.set_ylabel(r'Radius [R$_{\odot}$]',fontsize=fsize)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
ax1.set_ylim([ylolim,yuplim])
ax1.set_xlim([xlolim,xuplim])
ax1.set_ylim([ylolim,yuplim])
ax1.set_xlim([xlolim,xuplim])


ax2 = ax1.twinx()
ax3 = ax2.twiny()

#ax3.errorbar(bds['Mj'],bds['Rj'], xerr=np.array([bds['Mj_err_low'],bds['Mj_err_high']]),
#             yerr=np.array([bds['Rj_err_low'],bds['Rj_err_high']]),fmt='k.',elinewidth=1.5,ms=5,alpha=0.6)
#ax1.errorbar(lowmass['M2'],lowmass['R2'], 
#            xerr=np.array([lowmass['FeH_err_low'],lowmass['FeH_err_high']]),
#            yerr=np.array([lowmass['M2_err_low'],lowmass['M2_err_high']]),
#            fmt='g.',elinewidth=1.5,ms=10,label=r'13-42.5 M$_{\rm Jup}$')#,alpha=0.3)

ax3.axvline(80,color='black',linestyle='--',alpha=0.3)
ax3.text(25,2.5,'brown dwarfs',color='black',fontsize=fsize3,alpha=0.8)
ax3.text(100,2.5,'low-mass stars',color='black',fontsize=fsize3,alpha=0.8)
ax3.axvline(13,color='black',linestyle='--',alpha=0.3)

ax3.set_ylim([ylolim/rsj,yuplim/rsj])
ax3.set_xlim([xlolim/msj,xuplim/msj])
ax3.set_xlabel(r'Mass [M$_{\rm Jup}$]',fontsize=fsize)
ax3.tick_params(labelsize=fsize3)
ax2.set_ylabel(r'Radius [R$_{\rm Jup}$]',fontsize=fsize)
ax2.tick_params(labelsize=fsize3)
ax2.yaxis.set_major_locator(plt.MaxNLocator(5))

ptsize = 12
ptsize2 = 14
ax3.errorbar(M2_148,R2_148, xerr=M2err_148,yerr=R2err_148,
             fmt='.',color='red',elinewidth=1.5,ms=10,alpha=0.6)
ax3.text(M2_148,R2_148-0.1,'TOI-148',color='red',fontsize=ptsize2)

ax3.errorbar(M2_587,R2_587, xerr=M2err_587,yerr=R2err_587,
             fmt='.',color='red',elinewidth=1.5,ms=10,alpha=0.6)
ax3.text(M2_587-17,R2_587+0.02,'TOI-587',color='red',fontsize=ptsize2)

ax3.errorbar(M2_681,R2_681, xerr=M2err_681,yerr=R2err_681,
             fmt='.',color='red',elinewidth=1.5,ms=10,alpha=0.6)
ax3.text(M2_681-17,R2_681,'TOI-681',color='red',fontsize=ptsize2)

ax3.errorbar(M2_746,R2_746, xerr=M2err_746,yerr=R2err_746,
             fmt='.',color='red',elinewidth=1.5,ms=10,alpha=0.6)
ax3.text(M2_746-17,R2_746+0.01,'TOI-746',color='red',fontsize=ptsize2)

ax3.errorbar(M2_1213,R2_1213, xerr=M2err_1213,yerr=R2err_1213,
             fmt='.',color='red',elinewidth=1.5,ms=10,alpha=0.6)
ax3.text(M2_1213,R2_1213+0.015,'TOI-1213',color='red',fontsize=ptsize2)

plt.tight_layout()

plt.savefig('plots/mass_radius.pdf')