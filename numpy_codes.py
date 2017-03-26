import numpy as np
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



