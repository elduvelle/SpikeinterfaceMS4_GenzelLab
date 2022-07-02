# Spikeinterface
## Installation of Spikeinterface

Create a new environment, Python needs to be >=3.7

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
~`pip install phy==2.0b1`~

Actually, this doesn't work, what we want to do instead is:
`pip install phy --pre --upgrade` as indicated on [this page](https://github.com/cortex-lab/phy)

For Mountainsor4 in spikeinterface
```
pip install mountainsort4
```
- if this step fails, it means you need to do the following
`pip install git+https://github.com/magland/isosplit5_python.git`
(you might have to do `pip install git` separately first, if git is not already installed)

## Usage
To export the data from Trodes (added from Caitlin): 
navigate to the Trodes folder and then type 
`trodesexport -mountainsort -rec <full path to rec file ending in .rec> -sortingmode 1`

(this will create 1 '.mda' file per tetrode, which is what Mountainsort expects)

Open the script 'ScriptMS4.py' and change the `directory` and `tetrodes_list` variables to correspond to the data directory and the number of the tetrodes you want to sort.
Note, this will create 1 subfolder (output_Tx) per tetrode where X is the tetrode number.
It will use the inbuilt function of spikeinterface to run mountainsort and export to phy the result.

Once the main code has run: you can change the 'run_phy' variable to 1 and run that part of the code (will improve later)
(specifically: 
```
from phy.apps.template import template_gui
this_params_file = path_to_data\output\phy_MS\params.py
template_gui(this_params_file)
```

or run, from a command line:
`phy template-gui path_to_data\output_Tx\phy_MS\params.py` (change the X to be the tetrode number of your choice)


_Credits: Adrian Aleman & Kayvan Combadiere from the Genzel lab_
