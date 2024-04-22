import xml.etree.ElementTree as ET

def read_trodes_config(path_to_file):
    '''
    Reads and returns as a dictionary specific elements of a Trodes configuration header
    '''

    ## Initialization
    trodes_config = {};

    ## Collect relevant info from the header file

    # Open the file
    tree = ET.parse(this_fn)
    root = tree.getroot()

    # Parse it to get relevant data, adjust this to collect more or less fields
    for config in root.iter('Configuration'):
        for glob_config in config.iter('GlobalConfiguration'):
            trodes_config['ts_creat'] = int(glob_config.get('timestampAtCreation'))
            trodes_config['systime_creat'] = int(glob_config.get('systemTimeAtCreation'))
            trodes_config['trodes_ver'] = glob_config.get('trodesVersion')
        for hard_config in config.iter('HardwareConfiguration'):
            trodes_config['sampling_rate'] = int(hard_config.get('samplingRate'))

    return trodes_config


if __name__ == '__main__':

    # full path to the extracted configuration, note, I changed the extension
    # to avoid overwriting an actual trodes config
    this_fn = "D:\\DATA\\Screening\\r208\\2024-03-15\\r208_sc41.rec\\r208_sc41.extracted_trodes_header.xml"
    trodes_config = read_trodes_config(this_fn)
    # Print the outcome
    print (trodes_config)


