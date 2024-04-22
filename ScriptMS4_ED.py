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
# This needs a more recent version of si but we need it to process bad channels
#import spikeinterface.preprocessing as spre

from mountainlab_pytools import mdaio

import tempfile
from tkinter import filedialog
import tkinter as tk

import readTrodesExtractedDataFile3 as trodesReader

os.environ['TEMPDIR'] = tempfile.gettempdir()
import matplotlib.pyplot as plt
import numpy as np
 
from spikeinterface.exporters import export_to_phy
import json
from extract_trodes_conf_v2 import extract_conf



def creatparam(mda_extract_params, direc): ##Function that will create the parameters and geometry file needed for mountainsort
    '''
    example of sort params:
    sort_params = {"samplerate": 30000, "spike_sign": -1}
    '''

    #mda_extract_params = {"samplerate": 30000, "spike_sign": -1}
    #geom = np.array([[1, 0],[2, 0],[3, 0],[4, 0]])
    # Trying something new
    geom = np.array([[0, 0],[-25, 25],[25, 25],[0, 50]])
    #ED mod file name handling
    np.savetxt(os.path.join(direc,'geom.csv'), geom, delimiter=',')
    # ED mod file name handling
    this_file_path = os.path.join(direc,'params.json')
    with open(this_file_path, 'w') as mon_fichier:
        json.dump(mda_extract_params, mon_fichier)           
        # print('Saved param file to:',this_file_path )

def save_ms_params(ms_sorting_params, folder):
    '''
    save the parameters used to run mountainsort
    sort_params = {'num_workers': 12, 'detect_threshold': 3, 'filter': False}
    '''

    this_file_path = os.path.join(folder,'ms_params.json')
    with open(this_file_path, 'w') as my_file:
        json.dump(ms_sorting_params, my_file)           
        # print('Saved ms param file to:', this_file_path )
        
def save_ses_lims(tosave_info, folder):
    '''
    Saves info about the start and end times and the sample number in each
    session of a concatenated recording
    ts_lims: dictionary with limits for each session
    sample_limes: same, for sample number
    ses_names: same, for session names
    '''

    this_fn = 'concat_limits.json'
    this_file_path = os.path.join(folder, this_fn)
    with open(this_file_path, 'w') as this_file:
        json.dump(tosave_info, this_file)
        print('Saved session(s) sample number info to:',this_file_path )


def run_Mountainsort(recording, directory_output, ms_sort_params = {}):
    verbose = 0;
    ##Function that will run mountainsort, extract the information from mountainsort and export to phy
    ss.installed_sorters()
    ms_params = ss.Mountainsort4Sorter.default_params()
    for param, value in ms_sort_params.items():
        ms_params[param] = value


    if 0:
        params = ss.get_default_sorter_params(sorter_name_or_class='mountainsort4')
        print("Parameters:\n", params)
        desc = ss.get_sorter_params_description(sorter_name_or_class='mountainsort4')
        print("Descriptions:\n", desc)

        # Note: this only works in more recent versions of spike interface.
        # For now we can get the parameters description from:
        # https://github.com/SpikeInterface/spikeinterface/blob/264c2b6b2915eed40327e93e9edd11acee551974/src/spikeinterface/sorters/external/mountainsort4.py#L37-L52

    desc = {
        "detect_sign": "Use -1 (negative) or 1 (positive) depending " "on the sign of the spikes in the recording",
        "adjacency_radius": "Radius in um to build channel neighborhood "
        "(Use -1 to include all channels in every neighborhood)",
        "freq_min": "High-pass filter cutoff frequency",
        "freq_max": "Low-pass filter cutoff frequency",
        "filter": "Enable or disable filter",
        "whiten": "Enable or disable whitening",
        "num_workers": "Number of workers (if None, half of the cpu number is used)",
        "clip_size": "Number of samples per waveform",
        "detect_threshold": "Threshold for spike detection",
        "detect_interval": "Minimum number of timepoints between events detected on the same channel",
        "tempdir": "Temporary directory for mountainsort (available for ms4 >= 1.0.2)s",
    }
    if verbose:
        print(ms_params) # we will send this to MS later       
        print("Descriptions:\n", desc)
    
        
    
    this_output_folder = os.path.join(directory_output, 'results_MS')
    
    sorting_MS = ss.run_mountainsort4(recording,
                                      output_folder = this_output_folder,
                                      verbose = True, **ms_params,)
        
    this_output_folder = os.path.join(directory_output,'wf_MS')

    # NOTE: this gives an error, if we only filter using MS:
    # from 'waveform_extractor'
    # "raise Exception('The recording is not filtered, you must filter it using `bandpass_filter()`."
    # so instead we pre-filter the recording and only do whitening in ms

    we_all = si.extract_waveforms(recording, sorting_MS, folder = this_output_folder, 
                                      max_spikes_per_unit = None, progress_bar = True)
    # What is this total_memory parameter?
    this_output_folder = os.path.join(directory_output,'phy_MS')
    export_to_phy(we_all, output_folder = this_output_folder,
                      progress_bar = True, total_memory = '500M')
    
    
def run_MS_on_folder(tetrodes = range(1,33), path_to_file = '', 
                     mda_params = {"samplerate": 30000, "spike_sign": -1},
                     ms_sort_params = {}, multisession = 0, extract_config = 1):
    
    do_filter_before_ms = 1 # 1: filter in the spike-band before sending the recording to mountainsort
    # note, mountainsort also has the possibility to whiten and filter
    
    if not path_to_file or not os.path.isfile(path_to_file):
        # wasn't given proper file as input so we will ask the user for it
    
        # Note ED: the 'input' command makes Spyder crash (at least the version that's
        # compatible with Anaconda). So we can either input the files with tk or
        # directly as variables in the code
        # TODO would probably be better to input the actual mountainsort file
        
        ms_suf = '.mountainsort'
        timestamps_suf = '.timestamps.mda'
        if multisession:

            print('Please select the parent folder to the sessions to concatenate (alphabetically) and spike-sort')
            path_to_folders = select_folder()
            # convert to os-independent path
            path_to_folders = os.path.abspath(path_to_folders)
            all_dirs = os.walk(path_to_folders)
            all_f = next(os.walk(path_to_folders))[1]
            # Only keep .rec ones
            all_f = [os.path.join(path_to_folders, folder) for folder in all_f if '.rec' in folder]
            # Find the .mountainsort folder in each folder
            all_ms_fold = []
            all_rec_fns = []
            for folder in all_f:
                in_folders = next(os.walk(folder))[1]
                # add the full path
                ms_folder = [os.path.join(folder, in_folder) for in_folder in in_folders if
                             ms_suf in in_folder]
                all_ms_fold += ms_folder

                in_files = next(os.walk(folder))[2]
                this_rec_fn = [os.path.join(folder, this_file) for this_file in in_files if '.rec' in this_file]
                if len(this_rec_fn) ==1:
                    all_rec_fns+= this_rec_fn
                elif len(this_rec_fn)==0:
                    print('Warning! No .rec file found in ' + folder)
                else:
                    print('Warning! More than one .rec file found in ' + folder)

            if len(all_ms_fold) <1:
                print('No Mountainsort folder found! Please extract the recording(s) to Mountainsort format with Trodes')
                return -1
                
            # Organize alphabetically, using this tuple to get the sorting index
            all_fns_with_ind = [(i, os.path.split(folder)[1][0:-len(ms_suf)]) for i, folder in enumerate(all_ms_fold)]
            # Sort this alphabetically
            all_fns_with_ind.sort( key=lambda fn: fn[1])
            sort_inds = [pair[0] for pair in all_fns_with_ind]
            all_fns = [pair[1] for pair in all_fns_with_ind]
            # apply sorting to the other lists
            # no wait that is too simple and doesn't work in python
            # all_ms_fold = all_ms_fold[sort_inds]
            # instead we have to do:
            all_ms_fold = [all_ms_fold[ind] for ind in sort_inds]

            num_to_merge = len(all_fns)
            print('Will concatenate ' + str(num_to_merge) + ' session(s) for spike-sorting:')
            for ind, filename in enumerate(all_fns):
                print (str(ind) + ': ' + filename)

            # get each session name in order    
            all_fns = [os.path.split(folder)[1][0:-len(ms_suf)] for folder in all_ms_fold]
            all_fns_paths = [os.path.split(folder)[0] for folder in all_ms_fold]

            # Get the timestamp info for each file  
            all_timestamps_fns = [fn + timestamps_suf for fn in all_fns]

            # Read the "timestamps" file to get the start and end sample numbers of this session

            all_fns_ts_senum = []
            print('Reading .mda timestamps files...')
            for [fni, fn] in enumerate(all_timestamps_fns):
                these_ts = mdaio.readmda(os.path.join(all_ms_fold[fni], fn))
                # This is an array of what appears to be timestamps that
                # possibly start either when the recording file was open
                # or when trodes started streaming.

                all_fns_ts_senum.append([int(these_ts[0]), int(these_ts[-1]), len(these_ts)])
                
            print('Done!')

            if extract_config:
                print('Extracting configuration header from all .rec files...')
                for rec_fn in all_rec_fns:
                    # Also extract and ideally read the header from the .rec file
                    # maxlines might need to be updated (increased) for larger channel counts?
                    extract_conf(rec_fn, maxlines = 1000)
                    
                    # TODO read this and add the relevant info into tosavedict

                    # TODO ALSO maybe use the systemtime at creation to order the merge???
            print('Done')
            
            concat_fname = all_fns[0] + '_concat_' + str(num_to_merge)
            # from the first session name create the concatenated folder name
            # IN the parent folder
            concat_fold = os.path.join(path_to_folders, concat_fname)
            sample_figs_fold = os.path.join(concat_fold, 'sample_figures')

            # Check if exist first
            if os.path.isdir(concat_fold):
                print('Warning! Folder for concatenated files already exists at: ')
                print(concat_fold)
                print('Please delete it and re-run this code, or press "c" then enter to continue')
                #return # comment this if you don't care, but it will erase all the sorting results if sorting the
                # same tetrodes
                breakpoint()
            
            else:
                print('creating folder for merged sessions at :')
                print(concat_fold)
                os.mkdir(concat_fold)
                # Also create a folder for sample figures
                os.mkdir(sample_figs_fold)

            
        else:
            # Only doing 1 session so selecting a rec file instead of a folder
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


            # Get the timestamp info for this file  
            timestamps_fn = data_fn_noext + timestamps_suf

            # Read the "timestamps" file to get the start, end and sample numbers of this session
            ts_senum = []
            print('Reading .mda timestamp file...')
            these_ts = mdaio.readmda(os.path.join(ms_folder, timestamps_fn))
            # This is an array of what appears to be timestamps that
            # possibly start either when the recording file was open
            # or when trodes started streaming.
            print('done')

            # Also extract and ideally read the header from the .rec file
            # maxlines might need to be updated (increased) for larger channel counts?
            extract_conf(path_to_file, maxlines = 1000)
            # TODO read this and add the relevant info into tosavedict

            # save it
            tosave_info_dict = {};
            tosave_info_dict['ts_s'] = [int(these_ts[0])]
            tosave_info_dict['ts_e'] = [int(these_ts[-1])]
            tosave_info_dict['ts_num'] = [len(these_ts)]                                
            tosave_info_dict['all_fns']= [data_fn_noext]
            tosave_info_dict['all_ms_fold'] = [ms_folder]
            tosave_info_dict['all_fns_paths'] = [data_folder]
            # This will be saved with the first tetrode sorted

            prev_figs_fold = os.path.join(ms_folder, 'sample_figures')
            # Create a folder for sample figures
            os.mkdir(prev_figs_fold)

    if not tetrodes:
        # default
        tetrodes = [1] # Can give '' as tetrode input and then use this instead
        
    print('Will run on tetrodes:' + str(tetrodes))
    
    saved_info = 0
   
    # Extract & sort all tetrodes mentioned in tetrode list
    
    for tt_num in tetrodes:
        if multisession:
            # load each recording in 'rec' format with mda recording extractor & concatenate them
            output_dir = os.path.join(concat_fold, 'output_T' + str(tt_num))
            recordings_list = []
            sample_nums = []
            ts_s = []
            ts_e = []
            ts_num = []
            recordings_dur = []
            for [rec_i, rec_n] in enumerate(all_fns):
                # Create the parameters, seems that they have to be saved in the same folder where mda data is

                creatparam(mda_params, all_ms_fold[rec_i])

                # Also create the parameters used by mountainsort
                save_ms_params( ms_sort_params, all_ms_fold[rec_i])
                
                # try to create the object and see if we can get sample number
                mda_name = rec_n +'.nt' + str(tt_num) + '.mda'

                # NOTE IMPORTANT the times here are by default starting at 0 with spikeinterface
                # We can get them to start at the actual time by computing the new times (add
                # the start time to the current time) and then use rec.set_times(new_time)
                # default_times = rec.get_times()
                # new_times = default_times + 5
                # rec.set_times(new_times)

                # looks like we can find the start time using timestamps.mda file extracted by Trodes!
                # note however that these are separate sessions so the start time of a later recording
                # might be smaller than that of an earlier recording, just because they have no link
                # across sessions
                this_rec = se.MdaRecordingExtractor(all_ms_fold[rec_i],\
                                                    raw_fname = mda_name, 
                               params_fname = 'params.json',
                               geom_fname = 'geom.csv')
                recordings_list.append(this_rec)
                sample_nums.append(this_rec.get_num_samples())
                #  fill this with start and end timestamps for each session, as well as number of samples
                ts_s.append(all_fns_ts_senum[rec_i][0])
                ts_e.append(all_fns_ts_senum[rec_i][1])
                ts_num.append(all_fns_ts_senum[rec_i][2])

                this_dur = this_rec.get_num_samples() / this_rec.get_sampling_frequency()
                recordings_dur.append(this_dur)
                
            #Save the sample num list and equivalent in times to file so that we can recover the original session limits
            if not saved_info:
                # Do this only once
                tosave_info_dict ={}
                # Need to convert these to int because int32 is not supported
                tosave_info_dict['ts_s'] = ts_s
                tosave_info_dict['ts_e'] = ts_e
                tosave_info_dict['ts_num'] = ts_num                                 
                tosave_info_dict['sample_nums']= sample_nums
                tosave_info_dict['all_fns']= all_fns
                tosave_info_dict['recordings_dur'] = recordings_dur
                tosave_info_dict['all_ms_fold'] = all_ms_fold
                tosave_info_dict['all_fns_paths'] = all_fns_paths
                save_ses_lims(tosave_info_dict, concat_fold)
                saved_info = 1

            # create a multirecording time extractor which concatenates the traces in time
            # The function MdaRecordingExtractor doesn't work in our spike interface version (0.93.0)
            # so we will try a different approach
            #multirecording = se.MultiRecordingTimeExtractor(recordings = recordings_list)

            # Use this concatenate_recordings function instead, but try to upgrade when we can
            multirecording = si.concatenate_recordings(recordings_list)

            # Do filtering
            w = sw.plot_timeseries(multirecording)
            #plot the first second of the recording
            # Make this save to file instead of showing
            prev_plot_title = 'data sample for ' + concat_fname + '-tt' + str(tt_num) +\
                              ' pre-filtering'

            prev_plot_path = sample_figs_fold
            plt.title(prev_plot_title)
            plt.savefig(os.path.join(prev_plot_path, prev_plot_title) + '.png',\
                        bbox_inches='tight')
            plt.close()
            
            if do_filter_before_ms:
                print('Pre-filtering in spike band')
                multirecording = st.bandpass_filter(multirecording, freq_min=300, freq_max=6000) #Band pass filtering
                # if we don't do this, ms gives an error, even though it also has filtering in its parameters
                w = sw.plot_timeseries(multirecording)
                # Make this save to file instead of showing
                prev_plot_title = 'data sample for' + concat_fname + '-tt' +\
                                  str(tt_num) + ', post-filtering'
                
                prev_plot_path = sample_figs_fold
                plt.title(prev_plot_title)
                plt.savefig(os.path.join(prev_plot_path, prev_plot_title) + '.png', bbox_inches='tight')
                plt.close()
                multirecording.annotate(is_filtered = True)
            else:
                print('Not pre-filtering the recording')

            # run mountainsort, give it the concat_fold as output dir

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Running Mountainsort on concatenated files...')
            print(*all_fns)
            ## Run mountainsort and export to phy
            run_Mountainsort(multirecording, output_dir, ms_sort_params)
            
            print('********************************')
            print('Finished tetrode:' + str(tt_num))
            print('********************************')
                        
        else:
            # Save the info about this session, just once for all tetrodes
            if not saved_info:
                save_ses_lims(tosave_info_dict, data_folder)
                saved_info = 1
            
            mda_name = data_fn_noext +'.nt' + str(tt_num) + '.mda'   

            output_dir = os.path.join(ms_folder, 'output_T' + str(tt_num))

            creatparam(mda_params, ms_folder) # Create the parameter and geom file, I think this can
            # be done only once           

            rec = se.MdaRecordingExtractor(ms_folder, raw_fname = mda_name, 
                                           params_fname = 'params.json',
                                           geom_fname = 'geom.csv')

            w = sw.plot_timeseries(rec) #plot the first second of the recording
            # Make this save to file instead of showing
            prev_plot_title = 'data sample for' + data_fn_noext + '-tt' + str(tt_num) + ' pre-filtering'
            prev_plot_path = prev_figs_fold
            plt.title(prev_plot_title)
            plt.savefig(os.path.join(prev_plot_path, prev_plot_title) + '.png', bbox_inches='tight')
            plt.close()
            
            
            if do_filter_before_ms:
                print('Pre-filtering in spike band')
                recording_f = st.bandpass_filter(rec, freq_min=300, freq_max=6000) #Band pass filtering
                # Note it looks like we don't need to do this with our ED data?
                w = sw.plot_timeseries(recording_f)
                prev_plot_title = 'data sample for' + data_fn_noext + '-tt' + str(tt_num) + ' post-filtering'
                plt.title(prev_plot_title)
                plt.savefig(os.pathc.join(prev_plot_path, prev_plot_title) + '.png', bbox_inches='tight')
                plt.close()
                rec.annotate(is_filtered = True)
            else:
                print('Not pre-filtering the recording')
                recording_f = rec
                
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Running Mountainsort on file:' + mda_name + '...')
            run_Mountainsort(recording_f, output_dir, ms_sort_params) ## Run mountainsort and export to phy
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

    # plt.ion() # will only show plot content at the end apparently
    

    # Note: data needs to have been extracted in mountainsort format first!
    # check https://github.com/elduvelle/SpikeinterfaceMS4_GenzelLab if unsure how

    # Options:
    export_to_MS = 0 #First step before being able to run Mountainsort. 
    # Can also be done from the command line.
    # trodesexport -mountainsort -rec C:\shared\DATA\Screening_DM\r206\2023-03-09_r206_test_rec6_wireless.rec\2023-03-09_r206_test_rec6_wireless_merged.rec -sortingmode 1

    run_MS = 1 # 1 to run Mountainsort on  selected tetrodes. This will take
    # a while: make sure to run it only once! Need to have extracted the data first.
     
    run_phy = 0 # if 1 will run phy on each tetrode one after the other
    # Warning, this mode seems to have a memory leak at the moment.
    # Note: you might also want to start running it once it's finished with 
    # one tetrode, in that case, run the code printed once mountainsort ends 
    # for one tetrode in the console (same python environment)
    
    
    # list here the tetrodes that you want to be sorted by Mountainsort.
    tetrodes_list = [24, 25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     23, 22, 21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]
    
    
    # rat 8
    tetrodes_list = [25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]
    
    tetrodes_list = [25, 26, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]
    tetrodes_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29,
                     21, 10, 9, 8, 7, 6, 5, 4, 3 ,2 , 1, 32, 31, 30]
    # 1: combine multiple sessions together (select the parent folder).
    # 0: only sort 1 session, select the .rec file.
    multisession = 1
    extract_config = 1 # Will create a readable version of the recording with the
    # extension .extracted_trodes_header.xml


    mda_params = {"samplerate": 30000, "spike_sign": -1}
    # None in num workers mean half of the cpu workers will be used
    # Detect threshold is to detect spikes on the 'normalized' signal
    # where std has been set to 1. 3 is the default.
    # We set the filter to false here because we pre-filter the recording
    ms_sort_params = {"num_workers": None, 'detect_threshold':3, \
                      'filter': False, 'whiten':True} 
   
    
    path_to_file = '' # Change this to an actual path to the raw data file, 
    # otherwise, the code will prompt you to choose it using the explorer
    
    
    ### 0: extract SpikeGadgets raw data into mountainsort format ###
    # Note, I am currently using matlab for this
    if export_to_MS:
        # TODO finish this, currently not working

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
        ms_folder = run_MS_on_folder(tetrodes_list, path_to_file, 
                                     mda_params, ms_sort_params, multisession,\
                                     extract_config)
    else:
        ms_folder = '' # can comment this to use the written path instead of choosing manually

    # print(ms_folder)   
    
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
