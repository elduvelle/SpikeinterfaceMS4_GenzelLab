# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import spikeinterface.extractors as se
import os
from tkinter import filedialog
import tkinter as tk

def select_file():
    root = tk.Tk()
    path_to_file = filedialog.askopenfilename()
    root.attributes("-topmost", True)
    root.withdraw()   
    return path_to_file


if __name__ == '__main__':
    
    var_exists = 'path_to_file' in locals() or 'path_to_file' in globals()
    
    if not var_exists or not os.path.isfile(path_to_file):
        # wasn't given proper file as input so we will ask the user for it
    
        # Note ED: the 'input' command makes Spyder crash (at least the version that's
        # compatible with Anaconda). So we can either input the files with tk or
        # directly as variables in the code
        # TODO would probably be better to input the actual mountainsort file
        print('Please select main data file (.rec) ')
        path_to_file = select_file()
    
    sg_rec = se.SpikeGadgetsRecordingExtractor(file_path=path_to_file, stream_id='trodes')
    
    tvec = sg_rec.get_times()
    
    channels = sg_rec.get_channel_ids()
    duration_s = sg_rec.get_total_duration()
    
    channel_num = '97';
    ch_data = sg_rec.get_traces(channel_ids=[channel_num])
    
    ## Plotting
    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(tvec, ch_data)
    
    
