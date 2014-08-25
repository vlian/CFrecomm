__author__ = 'yuan'

import os

file_list = ('tmp0823.dat', 'tmp0824.dat')
f = open('det_082324_nanjing.dat', 'w')
os.chdir('userdet_data')
for det_file in file_list:
    with open(det_file) as df:
        for line in df:
            f.write(line)
f.close()