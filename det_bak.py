#!/usr/bin/env python
# -*- coding:utf-8 -*-

import reco
from reco import Recommend

l = []
with open('userdet_20140713.dat') as f:
	for line in f:
		i, u = line[6:8]
		l.append((u, i))
r = Recommend(l)
print l
