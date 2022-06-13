# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:40:11 2022

@author: kayva
modified by ED on 2022-06-11
"""

import os
import spikeinterface as si
import spikeinterface.extractors as se 
import spikeinterface.toolkit as st
import spikeinterface.sorters as ss
import spikeinterface.comparison as sc
import spikeinterface.widgets as sw
import tempfile

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

if __name__ == '__main__':
    tetrodes_list = [2,4,7,8,22]
    #ED: the 'input' command makes Spyder crash. So we will input the files 
    # directly as variables here instead for now.
    # directory = input("Enter the data directory: ")
    # name = input("Enter the name of the file to spikesort: ")
    directory = r"\\dartfs.dartmouth.edu\rc\lab\D\DuvelleE\mvdmlab_ED_fs\Spike_sorting\Mallory_sample_data\tetrode_recording.mountainsort"
    if not os.path.isdir(directory):
        print('Directory not found!')
    print(directory)
    # name = 'tetrode_recording.nt1.mda'
    # From Caitlin: I think 2, 4, 6, 7, 8, 22 and 30 are the best.
    
    # Extract all tetrodes mentioned in tetrode list
    for tt_num in tetrodes_list:
        this_name = 'tetrode_recording.nt' + str(tt_num) + '.mda'   

        output = os.path.join(directory, 'output_T' + str(tt_num))
        # output = directory+'\output' # Note the backslash will change between linux and win
        # ED
        creatparam(directory) #Create the parameter and geom file
        print('Running Mountainsort on file:' + this_name + '...')
        rec = se.MdaRecordingExtractor(directory,raw_fname=this_name,params_fname='params.json',geom_fname='geom.csv')
        w = sw.plot_timeseries(rec) #plot the first second of the recording
        recording_f = st.bandpass_filter(rec, freq_min=300, freq_max=6000) #Band pass filtering
        w = sw.plot_timeseries(recording_f)
        rec.annotate(is_filtered=True)
        run_Mountainsort(recording_f,output) ## Run mountainsort and export to phy
        
        run_phy = 0
    
        if run_phy:
            from phy.apps.template import template_gui
            this_data_folder = r'\\dartfs.dartmouth.edu\rc\lab\D\DuvelleE\mvdmlab_ED_fs\Spike_sorting\Mallory_sample_data\tetrode_recording.mountainsort'
            this_tt = '6'
            this_params_file = os.path.join(this_data_folder, 'output_T' + this_tt, 'phy_MS' 'params.py')
            if not os.path.isfile(this_params_file):
                print('File not found!')
            template_gui(this_params_file)