# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:40:11 2022

@author: kayva
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
    np.savetxt(direc+'geom.csv', geom, delimiter=',')

    with open(direc+'params.json', 'w') as mon_fichier:
    	json.dump(parameter, mon_fichier)

def run_Mountainsort(recording,directory_output): ##Function that will run mountainsort, extract the information from mountainsort and export to phy
    ss.installed_sorters()
    default_MS = ss.Mountainsort4Sorter.default_params()
    print(default_MS)
    sorting_MS = ss.run_mountainsort4(recording, output_folder=directory_output+'/results_MS', verbose=True, **default_MS,)
        
    we_all = si.extract_waveforms(recording, sorting_MS, folder=directory_output+"/wf_MS", 
                                      max_spikes_per_unit=None, progress_bar=True)
    
    export_to_phy(we_all, output_folder=directory_output+'/phy_MS',
                      progress_bar=True, total_memory='100M')


directory = input("Enter the directory: ")
name = input("Enter the name of the file to spikesort: ")
print(directory)
output = directory+'/output'
creatparam(directory) #Create the parameter and geom file
rec = se.MdaRecordingExtractor(directory,raw_fname=name,params_fname='params.json',geom_fname='geom.csv')
w = sw.plot_timeseries(rec) #plot the first second of the recording
recording_f = st.bandpass_filter(rec, freq_min=300, freq_max=6000) #Band pass filtering
w = sw.plot_timeseries(recording_f)
rec.annotate(is_filtered=True)
run_Mountainsort(recording_f,output) ## Run mountainsort and export to phy
