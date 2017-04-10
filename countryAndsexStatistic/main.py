# -*- coding: utf-8 -*-
import csv
import pandas as pd
import json
datapath = "/home/zengxiaosen/Downloads/theFirstLeacture/codes/lect01_proj/survey.csv"

def run_main():
    male_set = {'male', 'm'}
    female_set = {'female', 'f'}
    result_dict = {}

    with open(datapath, 'r') as csvfile:
        rows = csv.reader(csvfile)
        for i, row in enumerate(rows):
            if i == 0:
                continue
            if i % 50 == 0:
                print ('now process the{}row data...'.format(i))
            gender_val = row[2]
            country_val = row[3]
            gender_val = gender_val.replace(' ', '')
            gender_val = gender_val.lower()
            if country_val not in result_dict:
                result_dict[country_val] = [0, 0]
            if gender_val in female_set:
                result_dict[country_val][0] += 1
            elif gender_val in male_set:
                result_dict[country_val][1] += 1
            else:
                pass
    with open("/home/zengxiaosen/Downloads/theFirstLeacture/codes/"
              "lect01_proj/Mycountry_gender.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['country', 'male', 'female'])

        for k, v in list(result_dict.items()):
            csvwriter.writerow([k, v[0], v[1]])

    filename = '/home/zengxiaosen/Downloads/theFirstLeacture/codes/lect01_proj/Mycountry_gender.csv'
    df = pd.read_csv(filename)
    print (type(df))
    print (df.head())

    country_se = df[u'country']
    print (type(country_se))
    print (country_se.head())
    df.to_csv('/home/zengxiaosen/c.txt', index=None, encoding='utf-8')
    filename = '/home/zengxiaosen/Downloads/mySecondLecture/codes/examples/files/global_temperature.json'
    with open(filename, 'r') as f_obj:
        json_data = json.load(f_obj)
    print (type(json_data))

    print (json_data.keys())
    year_str_lst = json_data['data'].keys()
    year_lst = [int(year_str) for year_str in year_str_lst]
    print (year_lst)

    temp_str_lst = json_data['data'].values()
    temp_lst = [float(temp_str) for temp_str in temp_str_lst]
    print (temp_lst)

    # build dataframe
    year_se = pd.Series(year_lst, name='year')
    temp_se = pd.Series(temp_lst, name='temperature')
    result_df = pd.concat([year_se, temp_se], axis=1)
    print (result_df.head())

if __name__ == '__main__':
    run_main()