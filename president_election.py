#coding:utf-8
import numpy as np
import datetime
import matplotlib.pyplot as plt

def is_convert_float(s):
    """
    judge a string can transform to float kind or not
    :param s:
    :return:
    """
    try:
        float(s)
    except:
        return False

def get_sum(str_array):
    cleaned_data = filter(is_convert_float, str_array)
    float_array = np.array(cleaned_data, np.float)
    return np.sum(float_array)

def run_main():
    """
    main function
    :return:
    """
    filename = '/home/zengxiaosen/zengxiaosen/kaggle/lecture02/codes/presidential_polls.csv'

    with open(filename, 'r') as f:
        col_names_str = f.readline()[:-1] # -1 means without the end '\n'

    col_name_lst = col_names_str.split(',')
    # use it's col name
    use_col_name_lst = ['enddate', 'rawpoll_clinton', 'rawpoll_trump', 'adjpoll_clinton', 'adjpoll_trump']

    use_col_index_lst = [col_name_lst.index(use_col_name) for use_col_name in use_col_name_lst]

    ## read data
    data_array = np.loadtxt(filename,
                            delimiter=',',
                            skiprows=1,
                            dtype=str,
                            usecols=use_col_index_lst)

    # data procession
    enddate_idx = use_col_name_lst.index('enddate')
    enddate_lst = data_array[:, enddate_idx].tolist()

    enddate_lst = [enddate.replace('-','/') for enddate in enddate_lst]
    date_lst = [datetime.datetime.strptime(enddate, '%m%d%Y') for enddate in enddate_lst]
    # year_month
    month_lst = ['%d-%02d' %(date_obj.year, date_obj.month) for date_obj in date_lst]
    month_array = np.array(month_lst)
    months = np.unique(month_array)

    # data analysis
    # statistic the canvass of cliton
    # raw data
    rawpoll_clinton_idx = use_col_name_lst.index('rawpoll_clinton')
    rawpoll_clinton_data = data_array[:, rawpoll_clinton_idx]
    # the data after weighting
    adjpoll_clinton_idx = use_col_name_lst.index('adjpoll_clinton')
    adjpoll_clinton_data = data_array[:, adjpoll_clinton_idx]
    # trump
    # raw data
    rawpoll_trump_idx = use_col_name_lst.index('rawpoll_trump')
    rawpoll_trump_data = data_array[:,rawpoll_trump_idx]

    # the trump data after weighting
    adjpoll_trump_idx = use_col_name_lst.index('adjpoll_trump')
    adjpoll_trump_data = data_array[:, adjpoll_trump_idx]

    results = []
    print '-------'
    print '-------'
    for month in months:
        # clinton
        # raw data
        print '---'
        rawpoll_clinto_month_data = rawpoll_clinton_data[month_array == month]
        print rawpoll_clinto_month_data
        rawpoll_clinton_month_sum = get_sum(rawpoll_clinto_month_data)
        adjpoll_clinton_month_data = adjpoll_clinton_data[month_array == month]
        adjpoll_clinton_month_sum = get_sum(adjpoll_clinton_month_data)

        # trump
        # raw data of trump
        rawpoll_trump_month_data = rawpoll_trump_data[month_array == month]
        # sum
        rawpoll_trump_month_sum = get_sum(rawpoll_trump_month_data)

        # adjusted data of adjpoll
        adjpoll_trump_month_data = adjpoll_trump_data[month_array == month]
        adjpoll_trump_month_sum = get_sum(adjpoll_trump_month_data)

        results.append((month, rawpoll_clinton_month_sum, adjpoll_clinton_month_sum, rawpoll_trump_month_sum, adjpoll_trump_month_sum))

    print results

    months, raw_cliton_sum, adj_cliton_sum, raw_trump_sum, adj_trump_sum = zip(*results)

    # visualization
    fig, subplot_arr = plt.subplot(2, 2, figsize=(15, 10))
    # raw data tendency showing
    subplot_arr[0, 0].plot(raw_cliton_sum, color='r')
    subplot_arr[0, 0].plot(raw_trump_sum, color='g')

    width=0.25
    x = np.arange(len(months))
    subplot_arr[0, 1].bar(x, raw_cliton_sum, width, color='r')
    subplot_arr[0, 1].bar(x + width, raw_trump_sum, width, color='g')
    subplot_arr[0, 1].set_xticks(x + width)
    subplot_arr[0, 1].set_xticklabels(months, rotation='vertical')




if __name__ == "__main__":
    run_main()