
import numpy as np
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import datetime
def concact():
    year_list=[i for i in range(2001,2011)]
    month_list=[i for i in range(1,13)]
    year_data=[]
    for year in year_list:
        tmp_list=[]
        for month in month_list:
            zero=str(0) if month<10 else ''
            file_name='WFDEI/Tair_WFDEI_'+str(year)+zero+str(month)+'.nc'
            tmp_data=xr.open_dataset(file_name,decode_times=False)
            months=tmp_data.mean(dim='tstep')
            times=[datetime.datetime(year,month,1)]
            months = months.expand_dims(time=times)
            tmp_list.append(months)
            print(file_name)
        years=xr.concat(tmp_list,dim='time')
        a=years['lon']
        b=years['lat']
        years.drop_vars('timestp')
        year_data.append(years)
        
        print(year)
    xr.concat(year_data,dim='time').drop_vars('timestp').to_netcdf('observational_datasets/Tair_WFDEI_ann.nc')  
concact()
