# -*- coding:utf-8 -*-
__author__ = 'Yuan, Wang'
import reco
from reco import Recommend
"""
readdata:读取数据。
commend_result:输出结果文件。
只计算有相同点播历史的用户
"""


def readdata(filename):
    l = []
    with open(filename, 'r') as f:
        for line in f:
            i, u = line.split("|")[6:8]
            if i != 'null' and i != '' and u != 'null' and u != '':
                l.append((u, i))
    return l


def recommend(writefile, tup=None):
    r = Recommend(tup)
    commend_result = open(writefile, 'w')
    for u in r.users:
        rec_lis = r.recommend(u)
        rs = ''
        for m in rec_lis:
            rs += ' ' + m[0].decode('gbk').encode('utf-8') + ':' + str(m[1]) + ';'
        commend_result.write(str(u) + rs + '\n')
    commend_result.close()

matr = readdata('userdet_20140713.dat')
recommend('commend_result.txt', matr)


