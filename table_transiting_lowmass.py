#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create latex table for transiting 13-150 mjup companions
Created on Wed Jun 23 17:05:05 2021
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
print('----------------------------')
      
      
for itr in range(len(lowmass['Name'])):
    name = str(lowmass['Name'][itr])
    m2 = str(format(lowmass['M2'][itr],'.1f'))
    m2elow = str(format(lowmass['M2_err_low'][itr],'.1f'))
    m2ehigh = str(format(lowmass['M2_err_high'][itr],'.1f'))
    r2 = str(format(lowmass['R2'][itr],'.2f'))
    r2elow = str(format(lowmass['R2_err_low'][itr],'.2f'))
    r2ehigh = str(format(lowmass['R2_err_high'][itr],'.2f'))
    period = str(format(lowmass['Period'][itr],'.2f'))
    ecc = str(format(lowmass['ecc'][itr],'.3f'))
    eccelow = str(format(lowmass['ecc_err_low'][itr],'.3f'))
    eccehigh = str(format(lowmass['ecc_err_high'][itr],'.3f'))
    m1 = str(format(lowmass['M1'][itr],'.2f'))
    m1elow = str(format(lowmass['M1_err_low'][itr],'.2f'))
    m1ehigh = str(format(lowmass['M1_err_high'][itr],'.2f'))
    r1 = str(format(lowmass['R1'][itr],'.2f'))
    r1elow = str(format(lowmass['R1_err_low'][itr],'.2f'))
    r1ehigh = str(format(lowmass['R1_err_high'][itr],'.2f'))
    if np.isnan(lowmass['Teff'][itr]) == False:
        teff = str(int(lowmass['Teff'][itr]))
        teffelow = str(int(lowmass['Teff_err_low'][itr]))
        teffehigh = str(int(lowmass['Teff_err_high'][itr]))
    else:
        teff = 'nan'
        teffelow = 'nan'
        teffehigh = 'nan'
    feh = str(format(lowmass['FeH'][itr],'.2f'))
    fehelow = str(format(lowmass['FeH_err_low'][itr],'.2f'))
    fehehigh = str(format(lowmass['FeH_err_high'][itr],'.2f'))
    ref = str(lowmass['Ref'][itr])
    refnum = str(lowmass['Refnum'][itr])
    ecctab = str(lowmass['table_ecc'][itr]).strip()
    
    if m2elow == m2ehigh:
        m2out = m2+'\,$\pm$\,'+m2elow
    else:
        m2out = m2+'$_{-'+m2elow+'}^{+'+m2ehigh+'}$'
        
    if r2elow == r2ehigh:
        r2out = r2+'\,$\pm$\,'+r2elow
    else:
        r2out = r2+'$_{-'+r2elow+'}^{+'+r2ehigh+'}$'
        
    if eccelow == eccehigh:
        eccout = ecc+'\,$\pm$\,'+eccelow
    else:
        eccout = ecc+'$_{-'+eccelow+'}^{+'+eccehigh+'}$'
    
    if ecctab != 'nan':
        eccout = ecctab
    
    if m1elow == m1ehigh:
        m1out = m1+'\,$\pm$\,'+m1elow
    else:
        m1out = m1+'$_{-'+m1elow+'}^{+'+m1ehigh+'}$'
        
    if r1elow == r1ehigh:
        r1out = r1+'\,$\pm$\,'+r1elow
    else:
        r1out = r1+'$_{-'+r1elow+'}^{+'+r1ehigh+'}$'
        
    if teffelow == teffehigh:
        teffout = teff+'\,$\pm$\,'+teffelow
    else:
        teffout = teff+'$_{-'+teffelow+'}^{+'+teffehigh+'}$'  
        
    if fehelow == fehehigh:
        fehout = feh+'\,$\pm$\,'+fehelow
    else:
        fehout = feh+'$_{-'+fehelow+'}^{+'+fehehigh+'}$'
        
    line = name+' & '+m2out+' & '+r2out+' & '+period+' & '+eccout+' & '+m1out+' & '+r1out+' & '+teffout+' & '+fehout+' & '+refnum+' \\\ '
    print(line)
print('----------------------------')
for itr in range(len(lowmass['Name'])):
    ref = str(lowmass['Ref'][itr])
    refnum = str(lowmass['Refnum'][itr])
    citeout = refnum+' \citealt{'+ref+'}; '
    print(citeout)
    #print(teff)
    #print(m2)
#for lowm in lowmass:
 #   c     
 
 #