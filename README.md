# Calibration and validation code for Ice Floe Tracker (Spring 2025)
The notebooks, scripts, and data in this repository is targeted toward calibration and validation tasks for the Ice Floe Tracker algorithm.

## Setting up the environment
Download miniconda, a minimal installation of the conda package manager. Then, navigate in the terminal to the project folder, and run
```
conda env create --file calval.yml
```
This will create an environment with the right versions of Python packages for working on the project. You can load the environment with
```
conda activate calval
```

# Finding data in the MIZ
The International Arctic Buoy Program (IABP) routinely places buoys on sea ice to monitor sea ice motion. Usually these buoys are placed in pack ice, so that the buoy stays in the Arctic long enough to make the expense of deployment worthwhile. Eventually, many buoys end up adrift in the marginal ice zone -- the region of the pack ice where ocean waves affect the ice dynamics, and where we often are able to see individual floes in satellite imagery. The Ice Floe Tracker (IFT) algorithm aims to identify and track such ice floes. To validate the IFT, we need to identify portions of IABP buoy trajectories occuring in times and locations where it is possible that the buoy lies upon a visible, distinct ice floe.

The folder `data/iabp/raw` contains some of the raw Level 1 IABP buoy data, while `data/iabp/clean` contains some trajectories that have undergone quality control. More trajectories will be added as they are processed. 

Monthly average sea ice concentration data from the National Snow and Ice Data Center (NSIDC) has been concatenated into yearly files and stored in `data/nsidc_agg`. These files can be used to identify whether the buoy is in a region with sea ice -- some buoys continue to drift into the open ocean after the ice that carries them melts away. 

# Determining search window size
The notebook `distance_threshold` uses the IABP data to determine the distance that an ice floe may travel in between images. 