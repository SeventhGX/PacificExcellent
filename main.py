import os
import argparse
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

global args


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='数据质量评估系统运行参数')
    parser.add_argument('--start_status', type=int, choices=[0, 1],
                        default=1, help='0表示原始数据未被整理，1表示已经得到整合的csv文件')
    parser.add_argument('--csv_path', type=str,
                        default='./PacificExcellent.csv', help='整理好的csv文件路径')
    parser.add_argument('--rawdata_filepath', type=str,
                        default=None,
                        help='原始数据路径')

    global args
    args = parser.parse_args(argv)


if __name__ == '__main__':
    parse_args()

    if args.start_status == 0:
        if args.rawdata_filepath is None:
            print('原始数据保存路径为空')
            exit()
        else:
            rawdata_filelist = os.listdir(args.rawdata_filepath)

        name = []
        for filename in rawdata_filelist:
            name.append(filename.split('.')[0])
        csv_data = np.empty((len(name), 0))
        csv_data = pd.DataFrame(data=csv_data, index=name)

        for filename in tqdm(rawdata_filelist):
            with open(f'{rawdata_filelist}/{filename}', 'r') as datafile:
                data = json.load(datafile)
                for x in data:
                    if x not in csv_data.columns.tolist():
                        csv_data[x] = np.nan
                    csv_data.loc[filename.split('.')[0], x] = data[x]

        csv_data.to_csv('PacificExcellent.csv')
