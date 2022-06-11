# Spikeinterface
## Installation of Spikeinterface

Create a new environment, Python need to be >=3.7

```
conda create --name environmnent
```
Activate your environment  
If you want to use spyder
```
conda install spyder=5
```
for spikeinterface installation
```
pip install spikeinterface[full]==0.93
```
for phy
```
pip install phy==2.0b1
```
For Mountainsor4 in spikeinterface
```
pip install mountainsort4
```

## Usage
To export the data from Trodes (added from Caitlin): 
navigate to the Trodes folder and then type 
`trodesexport -mountainsort -rec <full path to rec file ending in .rec> -sortingmode 1`

  (this will create 1 file per tetrode, which is what Mountainsort expects)
  
Input the directory of the file you want to spikesort

Input the name of the file you want to spikesort; it needs to be to the .mda format (can be exported from trode)

It will use the inbuilt function of spikeinterface to run mountainsort and export to phy the result.

Warning to run the script you need to use crtl+A and F9
