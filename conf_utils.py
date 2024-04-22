# Joshua Chu 
# downloaded from Trodes slack on 2024-04-21
import pathlib
import argparse
import os

from typing import List


import xml.etree.ElementTree as ET


def _write_output(filename:str, output:List):
    '''Writes the configuration section to the output file'''

    if os.path.isfile(filename):
        print('Warning! Config file already exists at :' + str(filename)+ ' - skipping extraction')
    else:     
        with open(filename, 'wb') as f:
            f.writelines(output)

def _extract(filepath:str, maxlines:int, conf_ext:str):
    '''Does the actual extraction of configuration section'''

    with open(filepath, 'rb') as infile:
        output_lines = []
        fileline = b''
        linecount = 0 # to prevent endless reading of the input file

        while True:
            # note: reading line-by-line may introduce a vulnerability. what happens
            # if there are NO newline characters in the file?
            fileline = infile.readline()
            output_lines.append(fileline)
            linecount += 1

            # we only look for the ending </Configuration> tag as a way for determining
            # that the file has a valid configuration section. but of course it's
            # possible that the file might be corrupted in some other way...
            if b"</Configuration>" in fileline:
                conf_fn = filepath.with_suffix(conf_ext)
                # change output filename suffix to .extracted_trodes_header and write the result
                _write_output(conf_fn, output_lines)
                return conf_fn

            if linecount > maxlines:
                raise Exception(
                    f"Maximum lines {maxlines} exceeded but no valid "
                    "configuration section found")

def extract_config(filename:str, maxlines:int, conf_ext:str):
    '''
    Extract configuration section from Trodes rec file

    Parameters
    ----------
    filename: Path to .rec file, str
    maxlines: Maximum number of lines to read from .rec file, int
    '''

    # handle filename
    filepath = pathlib.Path(filename)
    if not filepath.is_file():
        raise FileNotFoundError(f"File {str(filepath)} not valid!")

    conf_fn = _extract(filepath, maxlines, conf_ext)
    return conf_fn

def read_trodes_config(path_to_file):
    '''
    Reads and returns as a dictionary specific elements of a Trodes configuration header
    '''

    ## Initialization
    trodes_config = {};

    ## Collect relevant info from the header file

    # Open the file
    tree = ET.parse(path_to_file)
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

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='extract_trodes_conf',
        description='Extract configuration section from Trodes rec file '
            'and write the output to the same directory as the input file'
    )
    parser.add_argument('filename', type=str,
        help='Path to the .rec file from which to extract configuration info'
    )
    parser.add_argument(
        'conf_ext', type=str, default='.extracted_trodes_header.xml',
        help='extension of the extracted configuration file'
    )
    parser.add_argument(
        '-m', '--maxlines', type=int, default=10000,
        help='maximum number of lines to read from the input file'
    )    
    args = parser.parse_args()

    extract_conf(args.filename, args.maxlines, '.extracted_trodes_header.xml')
