#!/usr/bin/env python
# -*- coding:utf-8 -*-

import reco
from reco import Recommend

l = []
with open('det.dat') as f:
	for line in f:
		i, u = line.split("|")[6:8]
		l.append((u, i))
r = Recommend(l)

for u in r.users:
    print u, r.recommend(u)
