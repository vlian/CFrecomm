__author__ = 'yuan'

import os

file_list = ('userdet_20140823.dat', 'userdet_20140824.dat')
f = open('userdet_20140823-24.dat', 'w')
os.chdir('userdet_data')
for det_file in file_list:
    with open(det_file) as df:
        for line in df:
            f.write(line)
f.close()