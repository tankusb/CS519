# primal (pegosos)
# both batch and online subgradient update

from __future__ import division
import random # shuffle
import numpy as np

def svm_batch(X, Y, C=0.1, it=100): 
    #X = np.array([np.concatenate((vecx,[1])) for vecx in X])
    X = np.array(X)
    dim = len(X[0]) # assume bias dimension is not included
    Y = np.array(Y)
    w = np.zeros(dim)
    datasize = len(Y)
    for t in xrange(1, it+1):
        grad = np.zeros(dim)
        for x, y in zip(X, Y):
            func_margin = y * w.dot(x)
            if func_margin < 1:
                grad += y * x
        w *= (1 - 1/t)
        w += grad * C / 2 / t
        #print "t=", t, "w=", w
    return w
        
def svm_sgd(X, Y, C=0.1, it=100): 
    #X = np.array([np.concatenate((vecx,[1])) for vecx in X])
    X = np.array(X)
    dim = len(X[0]) # assume bias dimension is not included
    Y = np.array(Y)
    w = np.zeros(dim)
    N = len(Y)
    t = 0
    trainset = zip(X,Y)
    const = N * C * 0.5 # * 1e-4
    for epoch in xrange(1, it+1):
        for x, y in trainset:
            t += 1
            w *= (1 - 1/t)        
            func_margin = y * w.dot(x)
            if func_margin < 1:
                w += (const / t) * y * x
        #print "t=", t, "w=", w
    return w


if __name__ == "__main__":
    X = [[1,1], [1,-1], [-1,1], [-1,-1]]
    Y = [ 1,     1,      -1,     -1]
    print svm_batch(X, Y, C=1)
    print svm_sgd(X, Y, C=1)

