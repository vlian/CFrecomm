# -*- coding:utf-8 -*-

"""recommend according to customers' subscription"""

__author__ = 'Yuan, Wang'

import math


class Recommend:
    def __init__(self, records=None):
        self.records = records or []
        self.users = set()
        self.items = set()
        self.uimatrix = dict()
        self.iumatrix = dict()
        self.userSim = dict()
        self.setuser()
        self.setitem()
        self.setuimatrix()
        self.setiumatrix()
        self.setusersim()

        """
        user_set
        """
    def setuser(self):
        self.users = set(r[0] for r in self.records)

        """
        item_set
        """
    def setitem(self):
        self.items = set(r[1] for r in self.records)

        """
        user-item-ordered matrix
        """
    def setuimatrix(self):
        for u in self.users:
            self.uimatrix[u] = {}
        for u, i in self.records:
            try:
                self.uimatrix[u][i] += 1
            except KeyError:
                self.uimatrix[u][i] = 1

        """
        user-items matrix
        """
    def setiumatrix(self):
        for i in self.items:
            self.iumatrix[i] = {}
        for u, i in self.records:
            try:
                self.iumatrix[i][u] += 1
            except KeyError:
                self.iumatrix[i][u] = 1

    def similarity(self):
        pass
        """
        other methods of similarity computation。
        """

        """
        similarity computation
        """
    def setusersim(self):
        userRelated = {}
        for u in self.users:
            userRelated[u] = {}
            self.userSim[u] = {}

        """
        similarity matrix。
        """
        for us in self.iumatrix.values():
            for u in us:
                for v in us:
                    if u != v:
                        try:
                            userRelated[u][v] += 1
                        except KeyError:
                            userRelated[u][v] = 1

        """
        similarity matrix
        """
        for u, related in userRelated.items():
            for v, count in related.items():
                self.userSim[u][v] = count / math.sqrt(len(self.uimatrix[u]) * len(self.uimatrix[v]))

        """
        add scores
        """
    def recommend(self, user, k=4, nitem=4):
        rank = dict()
        for u, sim in sorted(self.userSim[user].items(), key=lambda x: x[1], reverse=True)[:k]:
            for i in self.uimatrix[u]:
                if i not in self.uimatrix[user]:
                    if sim != 0:
                        rank.setdefault(i, 0)
                        rank[i] += sim
        return sorted(rank.items(), key=lambda x: x[1], reverse=True)[:nitem]

