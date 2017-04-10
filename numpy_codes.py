import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
data = np.random.rand(2, 3)
print data

print 'dimension number: ', data.ndim
print 'each dimension size: ', data.shape
print 'data kind: ', data.dtype

# create ndarray
#list transform to ndarray
l = range(10)
data = np.array(l)
print data
print data.shape

# nested sequence transform to ndarray
l2 = [range(10), range(10)]
data = np.array(l2)
print data
print data.shape

zeros_arr = np.zeros((3, 4))
print zeros_arr

ones_arr = np.ones((2, 3))
print ones_arr

empty_arr = np.empty((3, 3))
empty_int_arr = np.empty((3, 3), int)
print zeros_arr
print '-----------------'
print ones_arr
print '-----------------'
print empty_arr
print '-----------------'
print empty_int_arr

print np.arange(10)
zeros_float_arr = np.zeros((3, 4), dtype=np.float64)
print zeros_float_arr
print zeros_float_arr.dtype

# use astype to transform data kind
zeros_int_arr = zeros_float_arr.astype(np.int32)
print zeros_int_arr
print zeros_int_arr.dtype

arr = np.array([[1, 2, 3],[4, 5, 6]])
print "matrix multiple: "
print arr * arr
print "matrix add: "
print arr + arr
print 2 * arr

arr2 = np.arange(12).reshape(3, 4)
print arr2
print arr2[1]
print arr2[0:2, 2:]
print arr2[:, 1:3]

data_arr = np.random.rand(3, 3)
print data_arr

year_arr = np.array([[2000,2001,2000],
                     [2005,2002,2009],
                     [2001,2003,2010]])

is_year_after_2005 = year_arr >= 2005
print is_year_after_2005
filtered_arr = data_arr[is_year_after_2005]
print filtered_arr

arr = np.random.rand(2, 3)
print arr
print arr.transpose()

arr3d = np.random.rand(2, 3, 4)
print arr3d
print '------------------------'
print arr3d.transpose((1, 0, 2))

arr = np.random.randn(2, 3)
print arr
print np.any(arr > 0)
print np.all(arr > 0)

arr = np.array([[1, 2, 1], [2, 3, 4]])
print arr
print np.unique(arr)

filename = '/home/zengxiaosen/zengxiaosen/kaggle/lecture02/codes/presidential_polls.csv'
data_array = np.loadtxt(filename,delimiter=',',
                        skiprows=1,
                        dtype={'names':('cycle', 'type', 'matchup'),'formats':('i4', 'S15', 'S50')},
                        usecols=(0, 2, 3))
print '---------------------'
print data_array
print '---------------------'
print data_array.shape

# random_arr = np.random.randn(100)
# plt.plot(random_arr)
# plt.show()

x = np.linspace(-5, 15, 50)
print x.shape
# draw guassian distribution
# plt.plot(x, sp.stats.norm.pdf(x=x, loc=5, scale=2))
# # cumulative sum
# plt.hist(sp.stats.norm.rvs(loc=5, scale=2, size=200), bins=50, normed=True, color='red', alpha=0.5)
# plt.show()
# plt.hist(np.random.randn(100), bins=10, color='b', alpha=0.3)
# plt.show()

# x = np.arange(50)
# y = x + 5 * np.random.rand(50)
# plt.scatter(x, y)
# plt.show()

# x = np.arange(5)
# y1, y2 = np.random.randint(1, 25, size=(2, 5))
# width = 0.25
# ax = plt.subplot(1, 1, 1)
# ax.bar(x, y1, width, color='r')
# ax.bar(x+width, y2, width, color='g')
# ax.set_xticks(x+width)
# ax.set_xticklabels(['a', 'b', 'c', 'd', 'e'])
# plt.show()

# m = np.random.rand(10, 10)
# plt.imshow(m, interpolation='nearest', cmap=plt.cm.ocean)
# plt.colorbar()
# plt.show()




