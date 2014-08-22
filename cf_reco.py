#-*- coding:utf-8 -*-
__author__ = 'yuan & wang'
#__推荐算法的实践，订购节目排名__#
import math


class UserBasedCF:
    def __init__(self, userdet=None, outcfcomm=None):
        self.count = dict()   #
        self.bestusersim = dict()
        self.userdet = userdet
        self.outcfcomm = outcfcomm
        self.userDict = {}
        self.itemDict = {}
        self.user_item_matrix = dict()
        self.UserItemDic()
        self.bestsim()

    def UserItemDic(self, userdet=None, outcfcomm=None):
        """
        读用户
        """
        self.userdet = userdet or self.userdet
        self.outcfcomm = outcfcomm or self.outcfcomm
        f = open(self.userdet, 'r')
        for var in f:
            arr = var.split('|')
            itemF = arr[6]
            userF = arr[7]
            if itemF != 'null' and itemF != '':
                if itemF in self.itemDict:
                    self.itemDict[itemF] += 1
                else:
                    self.itemDict[itemF] = 1
                if userF in self.userDict:
                    self.userDict[userF] += 1
                    if itemF in self.user_item_matrix[userF]:
                        self.user_item_matrix[userF][itemF] += 1
                else:
                    self.userDict[userF] = 1
                    self.user_item_matrix.setdefault(userF, {})
                    self.user_item_matrix[userF][itemF] = 1
        f.close()
        #补齐矩阵
        ('\n'
         '        for i in self.userDict:\n'
         '            for j in self.itemDict:\n'
         '                if j not in self.user_item_matrix[i]:\n'
         '                    self.user_item_matrix[i][j] = 0\n'
         '\n'
         '        '
        )

    def similarity(self):

        """
        计算用户相似度的一种简单方法。
        """
        self.userSim = dict()
        for u in user_item_matrix.keys():
            for v in user_item_matrix.keys():
                if u == v:
                    continue
                self.userSim[u][v] = len(set(user_item_matrix[u].keys()) & set(user_item_matrix[v].keys()))
                self.userSim[u][v] /= math.sqrt(len(user_item_matrix[u]) * len(user_item_matrix[v]) * 1.0)

    '''
    物品到用户的反查表。
    '''
    def bestsim(self, usermatr=None):
        usermatr = usermatr or self.user_item_matrix
        item_users = dict()  #item对应所有user的字典。
        for i, item in usermatr.items():
            '''
            i为用户，item为节目字典如{‘\xd5\xbd\xb3\xa4\xc9\xb3’,2}
            '''
            for j in item.keys():
                item_users.setdefault(j, set())
                item_users[j].add(i)
        user_item_count = dict()   #
        for item, users in item_users.items():
            #print users:点播某一个节目的用户集。
            for u in users:
                user_item_count.setdefault(u, 0)
                user_item_count[u] += 1  #用户1的点播数量。
                for v in users:
                    if u == v:
                        continue
                    self.count.setdefault(u, {})
                    self.count[u].setdefault(v, 0)
                    self.count[u][v] += 1  #用户订购关系矩阵。
        for u, related_users in self.count.items():
            self.bestusersim.setdefault(u, dict())
            for v, cuv in related_users.items():
                """
                cuv:related_users[][]:用户相同节目的个数。
                """
                self.bestusersim[u][v] = cuv / math.sqrt(user_item_count[u] * user_item_count[v] * 1.0)#用户相似度。

    def recommend(self, user, usermatr=None, k=4, nitem=4):
        """
        推荐。
        """
        usermatr = usermatr or self.user_item_matrix
        rank = dict()
        interacted_items = usermatr.get(user, {})#输入用户的订购矩阵。
        for v, wuv in sorted(self.bestusersim[user].items(), key=lambda x:x[1], reverse=True)[0:k]:
            """
            v:最近邻用户；wuv:最近邻用户的相似度。
            """
            for i, rvi in usermatr[v].items():
                '''
                i:最近邻用户v订购的节目。rvi:最近邻用户订购节目的打分（1）。
                '''
                if i in interacted_items:
                    continue
                rank.setdefault(i, 0)
                rank[i] += wuv
                '''
                rank：对于一个用户的某个节目，累加相似度。
                '''
        return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:nitem])
        """
        返回节目累加的相似度排名。
        """

u = UserBasedCF('userdet_20140713.dat', 'cf_comm.txt')
#print u.ReadUserDet().keys()
#useritem_dic = u.UserItemDic()
"""
for a in useritem_dic:
    if useritem_dic[a].values().count(1) > 0:
        pass
        #print a.ljust(50, '.'), useritem_dic[a], '*******************\n'
"""

for usr in u.count.keys():
    #print usr
    c= u.recommend(usr)
    if len(c) !=0:
        print c ,'**\n'
"""
a=('051589568804' in u.count.keys())
print a
"""
#u.userDict