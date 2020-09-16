import os
import argparse
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
from calculator import Calculator

global args


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='数据质量评估系统运行参数')
    parser.add_argument('--start_status', type=bool,
                        default=True, help='原始数据是否整合为csv文件')
    parser.add_argument('--csv_path', type=str,
                        default='./PacificExcellent.csv', help='整理好的csv文件路径')
    parser.add_argument('--rawdata_filepath', type=str,
                        default=None, help='原始数据路径')
    parser.add_argument('--visualization', type=bool,
                        default=False, help='是否可视化计算结果')
    parser.add_argument('--all', type=bool,
                        default=False, help='是否计算全部的指标')
    parser.add_argument('--integrality', type=bool,
                        default=False, help='是否计算完整性')
    parser.add_argument('--entropy', type=bool,
                        default=True, help='是否计算信息熵')
    parser.add_argument('--pearsonr', type=bool,
                        default=False, help='是否计算皮尔逊相关系数')

    global args
    args = vars(parser.parse_args(argv))  # 用字典的形式保存参数


def generate_csv(rawdata_filepath: str, csv_path: str):
    """
    根据原始数据，生成csv文件

    :param rawdata_filepath: 原始数据路径
    :param csv_path: csv文件路径
    """
    rawdata_filelist = []
    if rawdata_filepath is None:
        print('原始数据保存路径为空')
        exit()
    else:
        rawdata_filelist = os.listdir(rawdata_filepath)

    names = []
    for filename in rawdata_filelist:
        names.append(filename.split('.')[0])
    csv_data = np.empty((len(names), 0))
    csv_data = pd.DataFrame(data=csv_data, index=names)

    print('开始整理原始数据')
    for filename in tqdm(rawdata_filelist):
        with open(f'{rawdata_filelist}/{filename}', 'r') as datafile:
            data = json.load(datafile)
            for x in data:
                if x not in csv_data.columns.tolist():
                    csv_data[x] = np.nan
                csv_data.loc[filename.split('.')[0], x] = data[x]

    csv_data.to_csv(csv_path)
    print('原始数据整理完毕，已存入对应csv文件')


if __name__ == '__main__':
    parse_args()

    if not args['start_status']:
        generate_csv(args['rawdata_filepath'], args['csv_path'])

    sensors_data = pd.read_csv(args['csv_path'], low_memory=False, index_col=0)
    calculator = Calculator(sensors_data, args['visualization'])

    for command in args:
        if (args['all'] or args[command]) \
                and command not in ['all', 'start_status', 'csv_path', 'rawdata_filepath', 'visualization']:
            calculator.calculate(command)
