# soiltau-ec modified
An implementation for [A spatial emergent constraint on the sensitivity of soil carbon turnover to global warming](https://www.nature.com/articles/s41467-020-19208-8).
<img src="imgs/show.png" width="900px"/>

This project is based on the author's [original project](https://github.com/rebeccamayvarney/soiltau_ec). 
+ Several bugs have been modified.
+ Adapted it to the latest version of the iris package.

## Setup

### Prerequisites
+ Windows (Linux may also work).
+ python=3.10.8

### Download data
+ Download [CMIP5 model output](https://esgf-node.llnl.gov/search/CMIP5/) to directory `cmip5_data`.
+ Download [CMIP6 model output](https://esgf-node.llnl.gov/search/cmip6/) to directory `cmip6_data`.
+ Download [The WFDEI Meteorological Forcing Data](https://rda.ucar.edu/datasets/ds314.2/) to directory `WFDEI`.
+ Download [CARDAMOM Heterotrophic Respiration](https://datashare.is.ed.ac.uk/handle/10283/875) to directory `observational_datasets`.
+ Download [Raich et al. 2002 Soil Respiration](https://cdiac.ess-dive.lbl.gov/epubs/ndp/ndp081/ndp081.html) to directory `observational_datasets`.
+ Download [Hashimoto et al. 2015 Heterotrophic Respiration ](http://cse.ffpri.affrc.go.jp/shojih/data/index.html) to directory `observational_datasets`.
+ Download [the datasets for observational Soil Carbon](https://github.com/rebeccamayvarney/soiltau_ec) to directory `observational_datasets`.
+ [MODIS NPP](https://lpdaac.usgs.gov/products/mod17a3v055/) product isn't available now, so the code that needs this data cannot be run temporarily. But they are not the main part of the paper.

**Note**: 
+ The above data are uploaded with the code except CMIP5 model output and CMIP6 model output because they are too large. 
    + An example of ACCESS-ESM1-5 in ssp126 and ssp585 is given to show in Figure1, run Figure1_single.py to show it. 
    + To get To get a complete chart, you need to download all the data.
+ The initial WFDEI data is monthly data rather than the annual average temperature of 2001-2010 used in the paper. 
    + The processed data has been placed under the directory `observational_datasets`
    + If you choose to download it yourself, run get_WFDEI_ann.py after downloading to obtain the annual average temperature data of WFDEI in the paper.
    ```bash
    python get_WFDEI_ann.py.
    ```

### Getting Started
+ Install iris at dependencies from https://scitools-iris.readthedocs.io/en/latest/installing.html
```bash
conda install -c conda-forge iris
```
+ Install netCDF4 
```bash
conda install netCDF4
```
## Run
+ Run the code in the order described in [README.pdf](README.pdf)
+ All codes can be run with CMIP5 and CMIP6 data.
+ According to some uploaded data, the following code can be run:
    + [Figure1_single.py](Figure1_single.py)
    + [Figure2.py](Figure2.py)
    + [pofp_cmip5_plotting.py](pofp_cmip5_plotting.py)
    + [pofp_cmip6_plotting.py](pofp_cmip6_plotting.py)
    + [Figure3.py](Figure2.py)
    + [Figure4.py](Figure2.py)
    + [parisagreement_cmip5cmip6_plotting.py](parisagreement_cmip5cmip6_plotting.py)
+ [emergentconstraint_cmip5_plotting.py](emergentconstraint_cmip5_plotting.py) and [emergentconstraint_cmip6_plotting.py](emergentconstraint_cmip6_plotting.py) are useless.
