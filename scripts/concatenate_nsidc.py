"""Simple script to read the monthly average SIC files
and merge them into single files per year."""

import xarray as xr
import os

files = [f for f in os.listdir('../data/nsidc_sic/') if '.nc' in f]
files.sort()
for year in range(2002, 2023):
    ds_year = []
    fyear = [f for f in files if '_' + str(year) in f]
    for f in fyear:
        with xr.open_dataset('../data/nsidc_sic/' + f) as ds:
            ds_year.append(ds.load())
    xr.concat(ds_year, dim='time').to_netcdf('../data/nsidc_agg/nsidc_cdr_sic_' + str(year) + '.nc',
                                         encoding = {var:
                                {"zlib": True, "complevel": 9} for var in
                                                     ['cdr_seaice_conc_monthly',
                                                      'cdr_seaice_conc_monthly_stdev',
                                                      'cdr_seaice_conc_monthly_qa_flag']})