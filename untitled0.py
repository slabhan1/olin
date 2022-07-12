#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 19:03:01 2022

@author: sakshilabhane



enter month unmers
3 month average (jja) indices accross yars for 50 years 
correlation plots and maps for precipitation and oni 
"""
import pandas as pd
import numpy as np
import os
import xarray as xr
#from netCDF4 import Dataset
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

path='/Users/sakshilabhane/Desktop/BenZ/Data/PPT'
os.chdir(path)



#df = pd.read_csv('1951_1960.nc.gz', compression='gzip', header=0, sep=',', quotechar='"')
#ds1 = ("1961_1970.nc")


#ncfile = Dataset('1961_1970.nc',mode='w',format='NETCDF4_CLASSIC') 

DS1 = xr.open_dataset('1951_1960.nc')
df1 = DS1.to_dataframe() #empty


DS2 = xr.open_dataset('1961_1970.nc')
df2 = DS2.to_dataframe() #empty

DS3 = xr.open_dataset('1971_1980.nc')
df3 = DS3.to_dataframe()

DS4 = xr.open_dataset('1981_1990.nc')
df4 = DS4.to_dataframe()

DS5 = xr.open_dataset('1991_2000.nc')
df5 = DS5.to_dataframe()

DS6 = xr.open_dataset('2001_2010.nc')
df6 = DS6.to_dataframe()

DS7 = xr.open_dataset('2011_2019.nc')
df7 = DS7.to_dataframe()


fulldf=pd.concat([df3, df4, df5, df6, df7])
fulldf1=np.nan_to_num(fulldf)

DS=xr.merge([DS3,DS4,DS5,DS6,DS7])
fulldf2=DS.to_dataframe()


precip = fulldf['precip']
np.isnan(precip).sum()   #3957240 (65% NaN values)


da = DS.precip
mi=6 
mf=8
i=0

year_avg = [0] * 48
   
    
'''
year = 1971 

timei = str(year) + "-0" + str(mi) + "-01"
timef = str(year)+ "-0" + str(mf) + "-01"
    
temp_da = da.sel(time=slice(timei,timef))
temp_df = temp_da.to_dataframe()
temp_df = temp_df.mean()

year_avg= temp_df.mean()
'''
#for lat in range():
#for lon in range():
for year in range(1971,2019):
    i= year-1971
    timei = str(year) + "-0" + str(mi) + "-01"
    timef = str(year)+ "-0" + str(mf) + "-01"
    
    temp_da = da.sel(time=slice(timei,timef))
    temp_df = temp_da.to_dataframe()
    temp_df = temp_df.mean()

    year_avg[i] = temp_df.mean()


    
    
    
da1=da.to_dataframe()

clim = fulldf['precip'].mean() #what




'''
fig = plt.figure(figsize=[12,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=180))
clim.plot.contourf(ax=ax,
                   levels=np.arange(0, 13.5, 1.5),
                   extend='max',
                   transform=ccrs.PlateCarree(),
                   cbar_kwargs={'label': clim.units},
                   cmap='viridis_r')