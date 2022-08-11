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

def run_Mountainsort(recording, directory_output): ##Function that will run mountainsort, extract the information from mountainsort and export to phy
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
    
    if not path_to_file or not os.path.isfile(path_to_file):
        # wasn't given proper file as input so we will ask the user for it
    
        # Note ED: the 'input' command makes Spyder crash (at least the version that's
        # compatible with Anaconda). So we can either input the files with tk or
        # directly as variables in the code
        # TODO would probably be better to input the actual mountainsort file
        print('Please select main data file (.rec) ')
        path_to_file = select_file()

    if not tetrodes:
        tetrodes = [1] # Can give '' as tetrode input and then use this instead
        
    print('Will run on tetrodes:' + str(tetrodes))
    print(path_to_file)
    
    path_to_file = Path(path_to_file)
    [data_folder, data_fn] = os.path.split(path_to_file)
    # get no-extension filename
    [data_fn_noext, fn_ext] = os.path.splitext(data_fn)
        
    print('Chosen folder path: ' + data_folder)   
    print('Chosen filename: ' + data_fn)
    
    ms_folder = os.path.join(data_folder, data_fn_noext +'.mountainsort')
    print('Mountainsort path:' + ms_folder)

    # Extract all tetrodes mentioned in tetrode list
    for tt_num in tetrodes:
        # this_name = 'r204_screening_' + ele_file_ID +'.nt' + str(tt_num) + '.mda'   
        this_name = data_fn_noext +'.nt' + str(tt_num) + '.mda'   

        output_dir = os.path.join(ms_folder, 'output_T' + str(tt_num))

        creatparam(ms_folder) # Create the parameter and geom file
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Running Mountainsort on file:' + this_name + '...')
        rec = se.MdaRecordingExtractor(ms_folder, raw_fname = this_name, 
                                       params_fname = 'params.json',
                                       geom_fname = 'geom.csv')
        w = sw.plot_timeseries(rec) #plot the first second of the recording
        recording_f = st.bandpass_filter(rec, freq_min=300, freq_max=6000) #Band pass filtering
        # Note it looks like we don't need to do this with our ED data?
        w = sw.plot_timeseries(recording_f)
        rec.annotate(is_filtered = True)
        run_Mountainsort(recording_f, output_dir) ## Run mountainsort and export to phy
        
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
        
    export_to_MS = 0; #First step before being able to run Mountainsort. 
    # Can also be done from the command line.
    # TODO!
    
    run_MS = 1 # 1 to run Mountainsort on all selected tetrodes. This will take
    # a while: make sure to run it only once! Need to have extracted the data first.
    
    run_phy = 0 # if 1 will run phy on each tetrode one after the other
    # Note: you might also want to start running it once it's finished with 
    # one tetrode, in that case, run the code printed once mountainsort ends 
    # for one tetrode 
    
    extract_LFP = 0 # TODO (or do we want to do this in Matlab?)
    
    # list here the tetrodes that you want to be sorted by Mountainsort.
    tetrodes_list = [30, 31, 32, 1, 2, 3, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24,
                      25, 26, 11, 12, 13, 14, 15, 17, 18, 19, 27, 28, 29, 20]


    # tetrodes_list = [30, 1, 2, 3, 5, 9, 22, 23, 24,
    #                   25, 26, 11, 12, 14, 27, 28, 29]
    
    # MAIN tetrode list
    tetrodes_list = [2, 3, 5, 9, 22, 23, 24,
                      25, 26, 11, 12, 14, 27, 28, 29]
    
    tetrodes_list = [13]
    
    path_to_file = '' # Change this to an actual path to the raw data file, 
    # otherwise, the code will prompt you to choose it using the explorer
    
    
    ### 0: extract SpikeGadgets raw data into mountainsort format ###   
    
    ### 1: run mountainsort ###
    if run_MS:
        ms_folder = run_MS_on_folder(tetrodes_list, path_to_file)
    else:
        ms_folder = r'C:\xxx\this_data_folder\this_mountainsort_file.mountainsort'
        ms_folder = Path(ms_folder)
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
            template_gui(this_params_file)