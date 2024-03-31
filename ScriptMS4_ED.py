# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:40:11 2022

@author: kayva
modified by ED on 2022-06-11
"""
import subprocess
import os
import sys 
from pathlib import Path
import spikeinterface as si
import spikeinterface.extractors as se 
import spikeinterface.toolkit as st
import spikeinterface.sorters as ss
import spikeinterface.comparison as sc
import spikeinterface.widgets as sw
import tempfile
from tkinter import filedialog
import tkinter as tk

os.environ['TEMPDIR'] = tempfile.gettempdir()
import matplotlib.pyplot as plt
import numpy as np
 
from spikeinterface.exporters import export_to_phy




def creatparam(direc): ##Function that will create the parameters and geometry file needed for mountainsort
    import json

    parameter = {"samplerate": 30000, "spike_sign": -1}
    geom = np.array([[1, 0],[2, 0],[3, 0],[4, 0]])
    #ED mod file name handling
    np.savetxt(os.path.join(direc,'geom.csv'), geom, delimiter=',')
    # ED mod file name handling
    this_file_path = os.path.join(direc,'params.json')
    with open(this_file_path, 'w') as mon_fichier:
    	json.dump(parameter, mon_fichier)
        
    print('Should have saved param file to:',this_file_path )

def run_Mountainsort(recording, directory_output): 
    ##Function that will run mountainsort, extract the information from mountainsort and export to phy
    ss.installed_sorters()
    default_MS = ss.Mountainsort4Sorter.default_params()
    print(default_MS)
    this_output_folder = os.path.join(directory_output, 'results_MS')
    sorting_MS = ss.run_mountainsort4(recording,
                                      output_folder = this_output_folder,
                                      verbose = True, **default_MS,)
        
    #ED added use of os.path.join
    this_output_folder = os.path.join(directory_output,'wf_MS')
    we_all = si.extract_waveforms(recording, sorting_MS, folder = this_output_folder, 
                                      max_spikes_per_unit = None, progress_bar = True)
    #ED added use of os.path.join
    this_output_folder = os.path.join(directory_output,'phy_MS')
    export_to_phy(we_all, output_folder = this_output_folder,
                      progress_bar = True, total_memory = '100M')
    
    
def run_MS_on_folder(tetrodes = range(1,33), path_to_file = ''):
    do_filter = 1 # 1: filter in the spike-band
    
    if not path_to_file or not os.path.isfile(path_to_file):
        # wasn't given proper file as input so we will ask the user for it
    
        # Note ED: the 'input' command makes Spyder crash (at least the version that's
        # compatible with Anaconda). So we can either input the files with tk or
        # directly as variables in the code
        # TODO would probably be better to input the actual mountainsort file
        if multisession:
            ms_suf = '.mountainsort'
            # TODO turn this into a session
            print('Please select the parent folder to the session to concatenate and sort')
            path_to_folders = select_folder()
            # convert to os-independent path
            path_to_folders = os.path.abspath(path_to_folders)
            
            all_dirs = os.walk(path_to_folders)
            all_f = next(os.walk(path_to_folders))[1]
            # Only keep .rec ones
            all_f = [os.path.join(path_to_folders, folder) for folder in all_f if '.rec' in folder]
            # Find the .mountainsort folder in each folder
            all_ms_fold = []
            for folder in all_f:
                in_folders = next(os.walk(folder))[1]
                # add the full path
                ms_folder = [os.path.join(folder, in_folder) for in_folder in in_folders if
                             ms_suf in in_folder]
                all_ms_fold += ms_folder

            # Organize alphabetically
            all_ms_fold.sort()
            num_to_merge = len(all_ms_fold)
            print('Will concatenate ' + str(num_to_merge) + ' session(s) for spike-sorting:')
            for ind, folder in enumerate(all_ms_fold):
                print (str(ind) + ': ' + folder)

            # get each session name in order    
            all_fns = [os.path.split(folder)[1][0:-len(ms_suf)] for folder in all_ms_fold]
            all_fns_paths = [os.path.split(folder)[0] for folder in all_ms_fold]

            concat_fname = all_fns[0] + '_concat_' + str(num_to_merge)
            # from the first session name create the concatenated folder name
            # IN the parent folder
            concat_fold = os.path.join(path_to_folders, concat_fname)

            # Check if exist first
            if os.path.isdir(concat_fold):
                print('Warning! Folder for concatenated files already exists at: ')
                print(concat_fold)
            else:
                print('creating folder for merged sessions at :')
                print(concat_fold)
                os.mkdir(concat_fold)
            # Find and store start and end times of each session for sp and lfp and pos
            breakpoint()
            
        else:
            print('Please select main data file (.rec) to be sorted')
            path_to_file = select_file()
            print(path_to_file)
    
            path_to_file = Path(path_to_file)
            [data_folder, data_fn] = os.path.split(path_to_file)
            # get no-extension filename
            [data_fn_noext, fn_ext] = os.path.splitext(data_fn)
                
            print('Chosen folder path: ' + data_folder)   
            print('Chosen filename: ' + data_fn)
            
            ms_folder = os.path.join(data_folder, data_fn_noext +'.mountainsort')
            print('Mountainsort path:' + ms_folder)

    if not tetrodes:
        tetrodes = [1] # Can give '' as tetrode input and then use this instead
        
    print('Will run on tetrodes:' + str(tetrodes))


    # Extract all tetrodes mentioned in tetrode list
    for tt_num in tetrodes:
        # this_name = 'r204_screening_' + ele_file_ID +'.nt' + str(tt_num) + '.mda'   
        this_name = data_fn_noext +'.nt' + str(tt_num) + '.mda'   

        output_dir = os.path.join(ms_folder, 'output_T' + str(tt_num))

        creatparam(ms_folder) # Create the parameter and geom file
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Running Mountainsort on file:' + this_name + '...')
        rec = se.MdaRecordingExtractor(ms_folder, raw_fname = this_name, 
                                       params_fname = 'params.json',
                                       geom_fname = 'geom.csv')
        w = sw.plot_timeseries(rec) #plot the first second of the recording
        if do_filter:
            recording_f = st.bandpass_filter(rec, freq_min=300, freq_max=6000) #Band pass filtering
            # Note it looks like we don't need to do this with our ED data?
            w = sw.plot_timeseries(recording_f)
            rec.annotate(is_filtered = True)
        else:
            recording_f = rec
        run_Mountainsort(recording_f, output_dir) ## Run mountainsort and export to phy
        print('********************************')
        print('Finished tetrode:' + str(tt_num))
        print('********************************')

    return ms_folder

def select_file():
    root = tk.Tk()
    path_to_file = filedialog.askopenfilename()
    root.attributes("-topmost", True)
    root.withdraw()   
    return path_to_file
   
def select_folder():
    root = tk.Tk()
    path_to_folder = filedialog.askdirectory()
    root.attributes("-topmost", True)
    root.withdraw() 
    return path_to_folder      
    
    

if __name__ == '__main__':
    

    # Note: data needs to have been extracted in mountainsort format first!
    # check https://github.com/elduvelle/SpikeinterfaceMS4_GenzelLab if unsure how

    # Options:
    
    multisession = 1 # Will ask to select a directory instead of a folder,
    # and will concatenate all sessions in there, for now, in a new folder
    # if not, will ask to select a single .rec file and will 
        
    export_to_MS = 0 #First step before being able to run Mountainsort. 
    # Can also be done from the command line.
    # trodesexport -mountainsort -rec C:\shared\DATA\Screening_DM\r206\2023-03-09_r206_test_rec6_wireless.rec\2023-03-09_r206_test_rec6_wireless_merged.rec -sortingmode 1
    
    run_MS = 1 # 1 to run Mountainsort on all selected tetrodes. This will take
    # a while: make sure to run it only once! Need to have extracted the data first.
     
    run_phy = 0 # if 1 will run phy on each tetrode one after the other
    # Note: you might also want to start running it once it's finished with 
    # one tetrode, in that case, run the code printed once mountainsort ends 
    # for one tetrode 
    
    extract_LFP = 0 # TODO (or do we want to do this in Matlab?)
    
    # list here the tetrodes that you want to be sorted by Mountainsort.
    tetrodes_list = [24, 25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     23, 22, 21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]
    
    
    # rat 8
    tetrodes_list = [25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]

    # RAt 6
#    tetrodes_list = [19, 3]
    
    # tetrodes_list = [1]
    #tetrodes_list = [20, 31, 2, 3, 4, 6, 10, 21, 22, 23]
    
    #17 didn't work for sq13

    # tetrodes_list = [12, 30, 3, 4];
    # tetrodes_list = [24, 25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29]
    
    # tetrodes_list = [9]

    # tetrodes_list =  [11, 12, 14, 20,27, 28, 22,21, 4, 3, 2]
    # tetrodes_list = [5]
    
    # # MAIN tetrode list
 
    #tetrodes_list = [12,14,15, 27,28,2,3,4,5,7, 21,23]
    
    #tetrodes_list = [13, 28,2,3,4,5,23]
    #tetrodes_list = [22, 27]
    #tetrodes_list = [29, 12, 13, 14, 15]
    
# Error for tetrodes 11 and 14: 
#     assert geom.shape[0] == self._diskreadmda.N1(), f'Incompatible dimensions between geom.csv and timeseries ' \

# AssertionError: Incompatible dimensions between geom.csv and timeseries file: 4 <> 3
# #could it be because we removed some bad channels?

# another error :
    # ResourceWarning: unclosed file <_io.TextIOWrapper name=5 encoding='cp1252'>
    # later:
  #   File C:\ProgramData\Anaconda3\envs\MoutainSort_Phy_test\lib\site-packages\sklearn\decomposition\_incremental_pca.py:283 in partial_fit
  #     raise ValueError(

  # ValueError: n_components=5 must be less or equal to the batch number of samples 4.
# Warning! The recording is already filtered, but mountainsort4 filter is enabled

    
    path_to_file = '' # Change this to an actual path to the raw data file, 
    # otherwise, the code will prompt you to choose it using the explorer
    
    
    ### 0: extract SpikeGadgets raw data into mountainsort format ###
    if export_to_MS:
        # TODO finish this

        print('Please select main data file (.rec) ')
        path_to_file = select_file()
        local_trodes_path = r"C:\Users\Eleonore\Desktop\Trodes_2-3-4_Windows64"
        
        # Store the current working directory to come back to it later
        cur_dir = os.getcwd()
        # Move to Trodes directory
        os.chdir(local_trodes_path)
        # os.chdir(cur_dir)
        # subprocess.run(["ls", "-l"])
        # cd the trodes path
        # then
        # Run the trodes export command to export the data into mountainsort format
        # Hopefully we can bypass this in future
        #note: maybe we need to move to the dict in the same process; try to do that instead
        res_sb = subprocess.run(["trodesexport", "-mountainsort -rec "+ path_to_file +" -sortingmode 1"],capture_output=True, shell = True)
        print(res_sb)
        # return to the original working directory
        os.chdir(cur_dir)
    
    
    ### 1: run mountainsort ###
    if run_MS:
        ms_folder = run_MS_on_folder(tetrodes_list, path_to_file)
    else:
        # ms_folder = r'\\dartfs.dartmouth.edu\rc\lab\D\DuvelleE\ED_Postdoc_2021_data\r206\screening\2023-02-15_r206_sq3\2023-02-15_r206_sq3.mountainsort'
        # ms_folder = Path(ms_folder)
        ms_folder = '' # can comment this to use the written path instead of choosing manually

    print(ms_folder)   
    
    ### 2: run phy ###
    if run_phy:
        from phy.apps.template import template_gui
        if not ms_folder or not os.path.isdir(ms_folder):
            #  ask the user for folder imput (to mountainsort folder)
            print('Please select mountainsort folder (ends with .mountainsort) ')
            ms_folder = select_folder()
           
            
        for this_tt in tetrodes_list:
            this_params_file = os.path.join(ms_folder, 'output_T' + str(this_tt), 'phy_MS', 'params.py')
            if not os.path.isfile(this_params_file):
                print('File not found!')
            else:
                print('Loading tetrode ' + str(this_tt) +' with Phy')
            template_gui(this_params_file)
