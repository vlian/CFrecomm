# -*- coding:utf-8 -*-
"""
recommend according to customers' subscription
2014-8-23
//////////////////////////////////////////////
readdata:input file.
commend_result:output file.
"""

__author__ = '(Yuan Lu-Feng)yuanlufeng@xwtech.com, (Wang Xing)wangxing@xwtech.com'
import reco
from reco import Recommend


def readdata(filename):
    l = []
    with open(filename, 'r') as f:
        for line in f:
            c, u, i = line.split("|")[0:3]
            if int(c) == 1:    # 城市。1：南京
                #print c,',', u, ',' , i,'\n'
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

matr = readdata('det_082324_nanjing.dat')
recommend('commend_result2.txt', matr)


