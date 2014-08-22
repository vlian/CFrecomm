# -*- coding:utf-8 -*-

import reco
from reco import Recommend

l = []
with open('det.dat') as f:
    for line in f:
        i, u = line.split("|")[6:8]
        l.append((u, i))
r = Recommend(l)
commend_result = open('commend_result.txt', 'w')
for u in r.users:
    rec_lis = r.recommend(u)
    s= str(u)
    rs=''
    for m in rec_lis:
        rs+=' '+m[0].decode('gbk').encode('utf-8')+':'+str(m[1])+';'
    commend_result.write(str(s)+rs+'\n')
commend_result.close()
