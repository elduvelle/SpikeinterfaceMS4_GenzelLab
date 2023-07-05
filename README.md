## Disclaimer: code is not guaranteed to work! Use it at your own risk ##

# Spikeinterface
## Installation of Spikeinterface

Create a new environment, Python needs to be >=3.7

```
conda create --name name_of_your_environment
```
Activate your environment  
```
conda activate name_of_your_environment
```
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

For Mountainsort4 in spikeinterface
```
pip install mountainsort4
```
- if this step fails, it means you need to do the following:  

`pip install git+https://github.com/magland/isosplit5_python.git`  
(you might have to do `pip install git` separately first, if git is not already installed; OR `conda install -c anaconda git` if pip install git doesn't work)

## Usage
To export the data from Trodes (added from Caitlin): 
navigate to the Trodes folder and then type
```
`trodesexport -mountainsort -rec <full path to rec file ending in .rec> -sortingmode 1`
```

(this will create 1 '.mda' file per tetrode, which is what Mountainsort expects)

2 options to run the code:

- Option 1. Open the script 'ScriptMS4.py', update `tetrodes_list` and optionally `path_to_file` to indicate the '.rec' raw data file. Run the code by pressing F5.
- Option 2. Run:
`run_MS_on_folder(tetrodes_list, path_to_file)` with appropriate contents given to those variables, note, `path_to_file` can be set to empty (`''`) and it will propt you to manually choose a folder.

Note 1: you'll have to be in the right conda environment!

Note 2: this will create 1 subfolder (output_Tx) per tetrode where X is the tetrode number.
It will use the inbuilt function of spikeinterface to run mountainsort and export to phy the result.

Once the main code has run: 3 options for the manual refinement with Phy:
- Option 1. Change 'run_MS' to 0 and 'run_phy' to 1 in 'ScriptMS4.py' and re-run the script. It will launch an instance of Phy for each tetrode in `tetrodes_list` (one after the other). Don't forget to save in Phy once you're finished with the sorting!
- Option 2. Run, from python: 
```
from phy.apps.template import template_gui
this_params_file = path_to_data\output_TX\phy_MS\params.py (where X = the tetrode to be sorted)
template_gui(this_params_file)
```
- Option 3: Run, from a command line:
```
phy template-gui path_to_data\output_Tx\phy_MS\params.py 
(change the X to be the tetrode number of your choice)
```

## Additional resources:
- [Phy clustering guide](https://phy.readthedocs.io/en/latest/sorting_user_guide/)
- [Next steps: extracting Phy data](https://phy.readthedocs.io/en/latest/sorting_user_guide/#analysis)
- [Phy video tutorial](https://www.youtube.com/watch?v=czdwIr-v5Yc)

_Credits: Adrian Aleman & Kayvan Combadiere from the Genzel lab_
## Disclaimer: code is not guaranteed to work! Use it at your own risk ##

