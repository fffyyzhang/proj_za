#老丁给的代码

# -*- coding: utf-8 -*-
import logging
import os
import sys
import json
import collections
from datetime import timedelta
from datetime import datetime
import time
import numpy as np

# from extratools.disjointsets import DisjointSets

class DisjointSets():
    def __init__(self, *objs):
        self.weights = {}
        self.parents = {}
        self.numofsets = 0

        for obj in objs:
            self.add(obj)


    def __iter__(self):
        return iter(self.parents)


    def __contains__(self, obj):
        return obj in self.parents


    def __len__(self):
        return len(self.parents)


    def add(self, obj):
        if obj in self.parents:
            return False

        self.parents[obj] = obj
        self.weights[obj] = 1
        self.numofsets += 1

        return True

    #find 函数，找根节点同时路径压缩
    def __getitem__(self, obj):
        if obj not in self:
            raise KeyError

        # Find path of objects up to the root
        path = []

        root = obj

        while len(path) == 0 or root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # Compress the path
        for obj in path:
            self.parents[obj] = root

        return root


    def cc(self):
        ret = collections.defaultdict(set)
        for obj in self:
            root = self[obj]
            ret[root].add(obj)

        return ret

    def union(self, *objs):
        roots = [self[obj] for obj in objs] #[] 操作就是找根节点

        heaviest = max(roots, key=lambda r: self.weights[r]) #weight都是一样的时候随意

        for r in roots:
            # liy : or self.parents[r] is heaviest 只有在多个节点被合并的时候回出现这个情况
            if r is heaviest or self.parents[r] is heaviest:
                continue

            self.weights[heaviest] += self.weights[r]
            self.parents[r] = heaviest
            self.numofsets -= 1 #统计非联通子图的个数

        return heaviest


def task_cc(iter_input):
    ts_begin = time.time()

    ds = DisjointSets()

    for index, row in enumerate(iter_input):
        if index % 100000 == 0:
            elapsed = time.time()-ts_begin + 0.0001 #liy aded +0.0001， avoid divide by 0
            logging.info('----{}----'.format(index))
            logging.info(str(timedelta(seconds=elapsed)))
            logging.info(int(index/elapsed))  #到目前为止每10w条耗费的时间

        docID, jd_id_prev, jd_id_cur = row

        ds.add(jd_id_prev)
        ds.add(jd_id_cur)
        ds.union(jd_id_prev, jd_id_cur )
        d=1

    return index, ds

def fn_iter_input():
    MAX = 40000000
    for i in range(MAX):
        x, y = np.random.randint(1, MAX, 2)
        if MAX< 100:
            logging.info(['doc-%05d' %i , x, y])
        yield ['doc-%05d' %i , x, y]  #docID,  jd_id_prev, jd_id



if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s][%(module)s][%(funcName)s][%(lineno)s] %(message)s', level=logging.INFO)

    iter_input = fn_iter_input()
    ts_begin = time.time()

    index, ds = task_cc(iter_input)

    elapsed = time.time()-ts_begin
    ret = {
        'elapsed': str(timedelta(seconds=elapsed)),
        'lines per second': int(index/elapsed),
        'total line': index,
        'total cc': len(ds.cc()),
    }
    if index< 100:
        logging.info(ds.cc())
    logging.info(json.dumps(ret, indent=4, sort_keys=True))

'''
    pip install extratools
    python etl/etl_cc.py

'''
