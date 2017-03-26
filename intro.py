#!/usr/bin/python
# -*- coding:utf-8 -*-
# import function library
import numpy as np
import matplotlib
import time
# from scipy.optimize import leastsq
# import scipy.optimize as opt
# import scipy
import matplotlib.pyplot as plot
# from scipy.stats import norm, poisson
# from scipy.interpolate import BarycentricInterpolator
# from scipy.interpolate import CubicSpline
import math
import function_collection

if __name__ == "__main__":

    L = [1, 2, 3]
    print  L

    a = np.array(L)
    print a
    print type(a)

    b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print b

    print a.shape
    print b.shape

    b.shape = 4, 3
    print b

    b.shape = 2, -1
    print b

    # b and c share the mem
    c = b.reshape((4, -1))
    print c

    b[0][1] = 20

    print b
    print c

    print a.dtype
    print b.dtype

    d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float)
    print d

    f = np.array([[1 + 2j, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.complex)
    print f

    #a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print  a

    f = d.astype(np.int)
    print f

    d.dtype = np.int
    print d

    a = np.arange(1, 10, 0.5)
    print a

    # include terminate date
    b = np.linspace(1, 10, 15)
    print b

    c = np.linspace(1, 10, 10, endpoint=False)
    print c

    d = np.logspace(1, 2, 20, endpoint=False)
    print d

    f = np.logspace(0, 10, 11, endpoint=True, base=2)
    print f

    s = 'ABCDZ'
    g = np.fromstring(s, dtype=np.int8)
    print g

    a = np.arange(10)
    print a

    print a[3]
    print a[3:6]

    print a[:5]

    print a[3:]
    print a[1:9:2]

    print a[::-1]

    a[1:4] = 10, 20, 30
    print a

    print a
    b = a[2:5]
    print b
    b[0] = 200
    print b

    print a

    a = np.logspace(0, 9, 10, base=2)
    print a

    i = np.arange(0, 10, 2)
    print i

    b = a[i]

    print b

    b[2] = 1.6

    print b
    print a

    a = np.random.rand(10)
    print a

    print a > 0.5

    b = a[a > 0.5]
    print b

    a[a > 0.5] = 0.5
    print a
    print b

    a = np.arange(0, 60, 10)
    print a
    print a.shape
    b = a.reshape((-1, 1))
    print b
    print b.shape

    a = np.arange(0, 60, 10)
    print a

    b = a.reshape((-1, 1))
    print b

    c = np.arange(6)
    print c

    f = b + c
    print f

    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print a

    print a[(0, 1, 2, 3), (2, 3, 4, 5)]
    print a[3:, [0, 2, 5]]

    i = np.array([True, False, True, False, False, True])
    print a[i]

    print a[i, 3]

    # for j in np.logspace(0, 7, 10):
    #     x = np.linspace(0, 10, j)
    #     start = time.clock()
    #     y = np.sin(x)
    #     t1 = time.clock() - start
    #
    #     x = x.tolist()
    #     start = time.clock()
    #     for i, t in enumerate(x):
    #         x[i] = math.sin(t)
    #
    #     t2 = time.clock() - start
    #
    #     print j, ": " , t1, t2, t2/t1

    mu = 0
    sigma = 1

    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    y = np.exp( -(x - mu) ** 2 / (2 * sigma ** 2) / (math.sqrt(2 * math.pi) * sigma))

    #plot.plot(x, y, 'ro-', linewidth=2)
    # plot.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    # plot.grid(True)
    # plot.show()

    # loss function: logistic loss(-1,1)/SVM Hinge loss/ 0/1 loss
    x = np.linspace(-3, 3, 1000)
    y_logit = np.log(1 + np.exp(-x)) / math.log(2)
    y_01 = x < 0
    print y_01
    y_hinge = 1 - x
    y_hinge[y_hinge < 0] = 0
    # plot.plot(x, y_logit, 'r-', label='Logistic Loss', linewidth=2)
    # plot.plot(x, y_01, 'g-', label='0/1 Loss', linewidth=2)
    # plot.plot(x, y_hinge, 'b-', label='Hinge Loss', linewidth=2)
    # plot.grid()
    # plot.legend(loc = 'upper right')
    # plot.show()

    # x = np.linspace(1.3, 1.3, 101)
    # y = function_collection.ff(x)
    # print y
    # plot.plot(x, y, 'g-', label='x^x', linewidth=2)
    # plot.grid()
    # plot.legend(loc='upper left')
    # plot.show()


    # x = np.arange(1, 0, -0.001)
    # y = (-3 * x * np.log(x) + np.exp(-(40 * (x - 1 / np.e)) ** 4) / 25) / 2
    # plot.figure(figsize=(5, 7))
    # plot.plot(y, x, 'r-', linewidth=2)
    # plot.grid(True)
    # plot.show()
    #
    # t = np.linspace(0, 7, 100)
    # x = 16 * np.sin(t) ** 3
    # y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    # plot.plot(x, y, 'r-', linewidth=2)
    # plot.grid(True)
    # plot.show()

    # center limit
    # t = 10000
    # a = np.zeros(1000)
    # for i in range(t):
    #     a += np.random.uniform(-5, 5, 1000)
    # a /= t
    # plot.hist(a, bins=30, color='g')
    # plot.grid()
    # plot.show()
    #
    # # poisson distribution
    # x = np.random.poisson(lam=5, size=10000)
    # print x
    # pillar=15
    # a = plot.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
    # plot.grid()
    # plot.show()

    













