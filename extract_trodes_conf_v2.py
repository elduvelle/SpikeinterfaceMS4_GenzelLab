# Joshua Chu 
# downloaded from Trodes slack on 2024-04-21
import pathlib
import argparse

from typing import List

def _write_output(filename:str, output:List):
    '''Writes the configuration section to the output file'''
 
    with open(filename, 'wb') as f:
        f.writelines(output)

def _extract(filepath:str, maxlines:int):
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
                # change output filename suffix to .extracted_trodes_header and write the result
                _write_output(filepath.with_suffix('.extracted_trodes_header.xml'), output_lines)
                break

            if linecount > maxlines:
                raise Exception(
                    f"Maximum lines {maxlines} exceeded but no valid "
                    "configuration section found")

def extract_conf(filename:str, maxlines:int):
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

    _extract(filepath, maxlines)


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
        '-m', '--maxlines', type=int, default=10000,
        help='maximum number of lines to read from the input file'
    )
    
    args = parser.parse_args()

    extract_conf(args.filename, args.maxlines)
