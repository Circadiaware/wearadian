# Fix iButtons incorrect csv formatting in the last column (value), where floating point numbers are represented with a comma, hence  messing up with the csv since it's comma separated. We replace with a dot.
# v0.2
# Created on 2020-06-26 by Stephen Karl Larroque

import codecs
import re
import sys

# Precompile regex to be faster
RE_comma = re.compile(r'(\d+),(\d+)')

def fix_ibuttons_csv(infile):
    outfilename = infile[:-4]+'_fixed.csv'
    with codecs.open(infile, 'r') as f, codecs.open(outfilename, 'w') as o:
        # Use a flag to detect when the values table begins, before there is a short table describing the parameters
        headerfound = False
        for line in f:
            if not headerfound:
                # Header not found, just copy line as-is
                o.write(line)
                # Check if we find the header of the values table
                if 'value' in line.lower():
                    headerfound = True
            else:
                # Else the header was found before, we need to fix this line
                if RE_comma.search(line):
                    # If we match the regex (ie, a number with a comma), we replace with a dot
                    o.write(RE_comma.sub(r'\1.\2', line))
                else:
                    # Otherwise, write the line as-is
                    o.write(line)
    # Return new filename
    return outfilename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please specify the path to the csv file as input.')
        sys.exit(1)

    infile = sys.argv[1]
    fix_ibuttons_csv(infile)
    print('All done! Fixed csv saved in %s. Exiting.' % outfilename)
