# coding:utf-8
from datetime import datetime
import copy
import random
import math
'''
@author : zengxiaosen
'''
def run_main():
    chinese_str = 'python data analysis'
    print chinese_str

    other_str = 'naive'
    print other_str

def divide(x, y):
    """
    do division
    :param x:
    :param y:
    :return:
    """
    try:
        return x/y
    except:
        return 'error happens'

def fun2(lst):
    lst[0] = 5
    print lst

def return_multiple():
    t = (1, 2, 3)
    return t

def remove_space(str):
    """
    remove space
    :param str:
    :return:
    """
    str_no_space = str.replace(' ', '')
    return str_no_space

def remove_dollar(str):
    """
    remove $
    :param str:
    :return:
    """
    if '$' in str:
        return str.replace('$', '')
    else:
        return str

def clean_str_lst(str_lst, operations):
    """
    clean string list
    :param str_lst:
    :param operation:
    :return:
    """
    result = []
    for item in str_lst:
        for op in operations:
            item = op(item)
        result.append(item)
    return result

def gen_test():
    for i in range(3):
        yield i

def func_add(x, y, f):
    """
    functional addition
    :param x:
    :param y:
    :param f:
    :return:
    """
    return f(x) + f(y)

def make_num(str1, str2):
    return int(str1) * 10 + int(str2)

def is_negative(x):
    return x < 0
if __name__ == '__main__':
    run_main()
    print '%d %s cost me $%.2f.' %(2,'books', 21.227)
    s_val = '3.1415926'
    print 'string value: %s' %s_val
    f_val = float(s_val)
    print 'float value: %f' %f_val
    i_val = int(f_val)
    print 'int value : %i' %i_val
    dt = datetime(2016, 12, 3, 15, 0, 0)
    print dt.month
    print dt.day
    dt.strftime('%Y%m%d %H:%M')
    dt.strftime('%d%m%Y %H:%M')
    datetime.strptime('20161203', '%Y%m%d')

    l = range(20)
    for i in l:
        if i%2 == 0:
            continue
        if i == 15:
            break
        print i
    print divide(8, 2)
    # print divide('8', 2)

    l_1 = [1, 2, 3]
    l_2 = l_1
    l_1.append(4)
    print l_1
    print l_2

    lst1 = range(5)
    print lst1

    fun2(lst1)
    print lst1

    a = [[1, 2, 3], [4, 5, 6]]
    b = a
    # c = copy(a)
    d = copy.deepcopy(a)

    a.append(15)
    a[1][2] = 10
    print 'processing......'
    print a
    print b
    # print c
    print d

    tup1 = 1, 2, 3
    print tup1

    tup2 = (1, 2, 3), (4, 5)
    print tup2

    l = [1, 2, 3]
    print tuple(l)

    str = 'Hello China'
    print tuple(str)

    tup3 = tuple(str)
    print tup3[4]

    print tup1 + tup2
    a, b, c = tup1
    print b

    a, _, c = return_multiple()
    print c

    tuple_lst = [(1, 2), (3, 4), (5, 6)]
    for x, y in tuple_lst:
        print x+y

    print tup3.count('o')

    lst_1 = [1, 2, 3, 'a', 'b', (4, 5)]
    print lst_1

    lst_2 = range(1, 9)
    print lst_2

    lst_3 = list(tup3)
    print lst_3

    lst_4 = range(10)
    lst_4.append(11)
    print lst_4

    lst_4.insert(5, 12)
    print lst_4

    item = lst_4.pop(6)
    print item
    print lst_4

    lst_4.remove(12)
    print lst_4

    lst_3 = lst_1 + lst_2
    print lst_3

    lst_1.extend(lst_2)
    print lst_1

    lst_5 = range(10)
    random.shuffle(lst_5)
    print lst_5

    lst_5.sort()
    print lst_5

    lst_6 = ['welcome', 'to', 'python', 'data', 'analysis', 'course']
    lst_6.sort()
    print lst_6

    lst_6.sort(key=len, reverse=True)
    print lst_6

    print lst_5
    print lst_5[1: 5]
    print lst_5[5:]
    print lst_5[:5]
    print lst_5[-5:]
    print lst_5[-5:-2]
    print lst_5[::2]
    print lst_5[::-1]

    lst_6 = ['welcome', 'to', 'python', 'data', 'analysis', 'course']
    for i, item in enumerate(lst_6):
        print '%i-%s' %(i, item)

    str_dict = dict((i, item) for i, item in enumerate(lst_6))
    print str_dict

    lst_5 = range(10)
    random.shuffle(lst_5)
    print lst_5

    lst_5_sorted = sorted(lst_5)
    print lst_5
    print lst_5_sorted

    lst_6 = ['welcome', 'to', 'python', 'data', 'analysis', 'course']
    lst_7 = range(5)
    lst_8 = ['a', 'b', 'c']
    zip_lst = zip(lst_6, lst_8, lst_7)
    print zip_lst

    print zip(*zip_lst)
    print list(reversed(lst_6))

    empty_dict = {}
    dict1 = {'a': 1, 2: 'b', '3': [1, 2, 3]}
    print empty_dict
    print dict1

    dict1[4] = (4, 5)
    print dict1

    del dict1[2]
    print dict1

    a_value = dict1.pop('a')
    print a_value
    print dict1

    print dict1.keys()
    print dict1.values()
    print dict1
    dict2 = {4: 'new1', 5: 'news'}
    dict1.update(dict2)
    print dict1

    dict_3 = {}
    l1 = range(10)
    l2 = list(reversed(range(10)))
    for i1, i2 in zip(l1, l2):
        dict_3[i1] = i2
    print dict_3

    dict_4 = dict(zip(l1, l2))
    print dict_4


    a = set(range(10))
    print a

    b = set(range(5, 15))
    print b

    print a | b
    print a.issubset(b)

    result1 = []
    for i in range(10000):
        if i%2 == 0:
            result1.append(i)

    print result1

    result2 = [i for i in range(10000) if i%2 == 0]
    print result2

    str_lst = ['welcome', 'to', 'python', 'data', 'analysis', 'course']
    result3 = [x.upper() for x in str_lst if len(x) > 4]
    print result3

    dict1 = {key : value for key, value in enumerate(reversed(range(10)))}
    print dict1

    set1 = {i for i in range(10)}
    print set1

    lists = [range(10), range(10, 20)]
    print lists

    events = [item for lst in lists for item in lst if item % 2 == 0]
    print events

    str_lst = ['$1.123', ' $1123.454', '$899.12312']
    clean_operations = [remove_space, remove_dollar]
    result = clean_str_lst(str_lst, clean_operations)
    print result

    f = lambda x:x**2
    print f(2)

    str_lst = ['welcome', 'to', 'python', 'data', 'analysis', 'course']
    str_lst.sort(key=lambda x:len(x))
    print str_lst

    str_lst.sort(key=lambda x:x[-1]) # sort by the last letter
    print str_lst

    gen = gen_test()
    print type(gen)

    for i in gen:
        print i

    fun = math.sqrt
    print fun(10)

    print func_add(4, 25, math.sqrt)
    print func_add(-4, 25, abs)

    x_2_lst = [x**2 for x in range(10)]
    print x_2_lst

    x_sqrt_lst = map(math.sqrt, x_2_lst)
    print x_sqrt_lst

    x_2_float_lst = map(float, x_2_lst)
    print x_2_float_lst

    # x_2_str_list = map(str, x_2_lst)
    # print x_2_str_list

    # str_lst = map(str, range(5))
    # print str_lst
    #
    # result = reduce(make_num, str_lst)
    # print result

    number_lst = range(-10, 10)
    filtered_lst = filter(is_negative, number_lst)
    print number_lst
    print filtered_lst
