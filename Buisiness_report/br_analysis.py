import os
import csv
import numpy as np
import math
file_path_W = 'csv/W.csv'
file_path_M = 'csv/M.csv'
file_path_3M = 'csv/3M.csv'
raw_result = 'report_result/raw_result.csv'

days = 7

with open(file_path_W, 'r') as csv_W:
    new_item = {}
    for i, csv_W_items in enumerate(csv_W):
        if i > 0:
            #print(items)
            item_splitted_by_comma_W = csv_W_items.split('","')
            key = item_splitted_by_comma_W[0][1:] + item_splitted_by_comma_W[1]
            num = int(item_splitted_by_comma_W[8])
            new_item[key] = [item_splitted_by_comma_W[0][1:], item_splitted_by_comma_W[1], item_splitted_by_comma_W[2], num, 0, 0, round(num/days, 3), 0, 0]

days = 30


with open(file_path_M, 'r') as csv_M:
    for i, csv_M_items in enumerate(csv_M):
        if i > 0:
            item_splitted_by_comma_M = csv_M_items.split('","')
            num = int(item_splitted_by_comma_M[8])
            key = item_splitted_by_comma_M[0][1:] + item_splitted_by_comma_M[1]
            print(key)
            if key not in new_item.keys():
                new_item[key] = [item_splitted_by_comma_M[0][1:], item_splitted_by_comma_M[1], item_splitted_by_comma_M[2], 0, num, 0, 0 , round(num/days, 3), 0]
            else:
                new_item[key][4] = num
                new_item[key][7] = round(num/days,3)


days = 90

with open(file_path_3M, 'r') as csv_3M:
    for i, csv_3M_items in enumerate(csv_3M):
        if i > 0:
            item_splitted_by_comma_3M = csv_3M_items.split('","')
            num = int(item_splitted_by_comma_3M[8])
            key = item_splitted_by_comma_3M[0][1:] + item_splitted_by_comma_3M[1]
            if key not in new_item.keys():
                new_item[key] = [item_splitted_by_comma_3M[0][1:], item_splitted_by_comma_3M[1], item_splitted_by_comma_3M[2], 0, 0, num, 0 , 0, round(num/days, 3)]
            else:
                new_item[key][5] = num
                new_item[key][8] = round(num/days,3)

pre_days = 60
with open(raw_result, 'w') as csv_result:
    writer = csv.writer(csv_result)
    writer.writerow(['父Asin号','Asin号','名字','近7日销量','近30日销量','近90日销量','近7日平均销量','近30日平均销量','近90日平均销量','总日平均销量','未来60日预测销量'])
    for key, value in new_item.items():
        nonzerolist = [e for e in value[-3:] if e != 0]
        if len(nonzerolist) > 0:
            num = round(float(np.mean(nonzerolist)),2)
            new_item[key].append(num)
            new_item[key].append(math.ceil(num * pre_days))

        else:
            new_item[key].append(0)
            new_item[key].append(0)

        writer.writerow(new_item[key])