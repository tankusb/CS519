#!/usr/bin/env python

import os
import math
import numpy as np
from random import random, randint
from matplotlib import pyplot
from sklearn import svm

from perc import sign, perc

dim = 2
N = 500

def gen():
    a, b, c = (random()-0.5)*10, (random()-0.5)*10, (random()+1)*5  # 0 for no bias
    norm = math.sqrt(a*a+b*b)

    w = np.array([a/norm, b/norm, c/norm])

    prec=1e-2
    data = [[], []]
    datas = []
    X = []
    Y = []
    # generate random data points that are separable
    while not all(len(d)>=20 for d in data):
        xy = np.array([(random()-0.5) * 20, (random()-0.5) * 20, 1])
        c = w.dot(xy)
        if c >= 1:
            i = 0 
        elif c <= -1:
            i = 1 
        else:
            i = 2
        if i < 2 and len(data[i]) <= 20:
            data[i].append((xy[0], xy[1]))
            datas.append(((xy[0], xy[1]), sign(c)))
            X.append(xy[:-1])
            Y.append(sign(c))

    # draw data points
    markers = ["ro", "bs"]
    for i, d in enumerate(data):
        ps = np.array(d).transpose()
        pyplot.plot(ps[0], ps[1], markers[i], ms=5)

    x = np.linspace(-10, 10, 21)

    # run perceptron and mira
    e1, percw, avgw, errp, marginp = perc(datas, MIRA=False)
    e2, miraw, _, erra, margina = perc(datas, MIRA=True, aggressive=False)
    e3, miraw2, _, erra2, margina2 = perc(datas, MIRA=True, aggressive=True, margin=0.9)
    print e1, e2, e3
    print percw, avgw
    print np.linalg.norm(percw), np.linalg.norm(avgw)
    print marginp, margina
    print errp, erra

    # draw perc/mira separation boundaries
    pyplot.plot(x, (percw[0]*x + percw[2])/-percw[1], "--", linewidth=0.5, label='perc') # PERC
    pyplot.plot(x, (miraw[0]*x + miraw[2])/-miraw[1], "-.", label='MIRA') # MIRA
    pyplot.plot(x, (miraw2[0]*x + miraw2[2])/-miraw2[1], "-.", label='0.9-aggress. MIRA') # agg. MIRA

    pyplot.legend(loc=2)
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    pyplot.xticks(x)
    pyplot.yticks(x)
    pyplot.show()

pyplot.ion()

while True:
    gen()
    pyplot.show()
    try:
        a = raw_input()
    except:
        break
    pyplot.clf()
