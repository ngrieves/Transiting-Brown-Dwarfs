#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:40:27 2021

@author: nolangrieves
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
from matplotlib.ticker import FormatStrFormatter

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



fig,ax = plt.subplots(figsize=(11,8))

ax.errorbar(lowmass['M2'],lowmass['ecc'],
            xerr=np.array([lowmass['M2_err_low'],lowmass['M2_err_high']]),
            yerr=np.array([lowmass['ecc_err_low'],lowmass['ecc_err_high']]),
            fmt='k.',elinewidth=1.5,ms=10)#,label='BDs')#,alpha=0.3)
#plt.legend(fontsize=20)

ax.errorbar(M2_148,ecc_148,xerr=M2err_148,yerr=ecce_148,fmt='go',ms=10)
ax.text(M2_148-14,ecc_148+0.018,'TOI-148',color='green',fontsize=fsize2,**{"zorder":100})

ax.errorbar(M2_587,ecc_587,xerr=M2err_587,yerr=ecce_587,fmt='go',ms=10)
ax.text(M2_587+1,ecc_587-0.03,'TOI-587',color='green',fontsize=fsize2,**{"zorder":100})

ax.errorbar(M2_681,ecc_681,xerr=M2err_681,yerr=ecce_681,fmt='go',ms=10)
ax.text(M2_681-6,ecc_681+0.02,'TOI-681',color='green',fontsize=fsize2,**{"zorder":100})

ax.errorbar(M2_746,ecc_746,xerr=M2err_746,yerr=ecce_746,fmt='go',ms=10)
ax.text(M2_746-7,ecc_746+0.02,'TOI-746',color='green',fontsize=fsize2,**{"zorder":100})

ax.errorbar(M2_1213,ecc_1213,xerr=M2err_1213,yerr=ecce_1213,fmt='go',ms=10)
ax.text(M2_1213-8,ecc_1213-0.04,'TOI-1213',color='green',fontsize=fsize2,**{"zorder":100})

#ax.errorbar(lowmass['M2']*msj,lowmass['ecc'], 
#            xerr=np.array([lowmass['M2_err_low']*msj,lowmass['M2_err_high']]),
#            yerr=np.array([lowmass['ecc_err_low']*msj,lowmass['ecc_err_high']]),
#            fmt='k.',elinewidth=1.5,ms=10)#,alpha=0.3)


import matplotlib.colors as mcol
#cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b","g","y","orange","red"])
#cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b","g","y","red"])
#cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["red","blue"])
#cm1 = mcol.ListedColormap(["indigo","blue","green","yellow","orange","red"])
#cm1 = mcol.ListedColormap(["indigo","blue","orange","red"])
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["red","orange","blue"])
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["red","yellow","blue","purple"])
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["red","pink","orange","yellow","blue","purple"])
import matplotlib
#cm1 = matplotlib.cm.get_cmap('seismic')

img1 = ax.scatter(lowmass['M2'],lowmass['ecc'],s=200,edgecolors='black',
            c=lowmass['Period'],cmap=cm1,**{"zorder":50},norm=matplotlib.colors.LogNorm())
#ax.legend(fontsize=24,loc='upper right',framealpha=0.9)
cb1 = fig.colorbar(img1,ax=ax)
cb1.set_label(r'Period [days]',fontsize=fsize)
cb1.ax.tick_params(labelsize=20)
cb1.ax.set_yticklabels(['1','10','100'])

ax.scatter(M2_148,ecc_148,s=190,facecolors='none',edgecolors='green',linewidth=2.5,**{"zorder":100})
ax.scatter(M2_587,ecc_587,s=190,facecolors='none',edgecolors='green',linewidth=2.5,**{"zorder":100})
ax.scatter(M2_681,ecc_681,s=190,facecolors='none',edgecolors='green',linewidth=2.5,**{"zorder":100})
ax.scatter(M2_746,ecc_746,s=190,facecolors='none',edgecolors='green',linewidth=2.5,**{"zorder":100})
ax.scatter(M2_1213,ecc_1213,s=190,facecolors='none',edgecolors='green',linewidth=2.5,**{"zorder":100})

#ax.set_xscale('log')
ax.set_ylabel('eccentricity',fontsize=fsize)
ax.set_xlabel(r'Mass [M$_{\rm Jup}$]',fontsize=fsize)
ax.tick_params(labelsize=fsize)
ax.axvline(13,color='black',linestyle='--',alpha=0.6)
ax.axvline(42.5,color='black',linestyle='--',alpha=0.6)
ax.axvline(80,color='black',linestyle='--',alpha=0.6)
plt.ylim(-0.025,1)
plt.xlim(0,155)
plt.tight_layout()

plt.savefig('plots/mass_ecc_per.pdf')