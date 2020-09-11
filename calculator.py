import pandas as pd
from tqdm import tqdm
from scipy.stats import pearsonr
from math import log
import time
import numpy as np
import re


def contain_alpha(array: np.ndarray):
    """
    检测数组是否含有字母

    :param array: 待检测的数组
    :return: True or False
    """
    for i in array:
        if bool(re.search('[a-zA-Z]', str(i))) and i == i:
            return True
    return False


def info_entropys(csv_data: pd.DataFrame):
    """
    每一列的信息熵

    :param csv_data: 要计算的表格
    :return: pd.Series，每一列数据的信息熵
    """
    print('entropy')
    time.sleep(0.1)
    sensors = csv_data.columns.tolist()
    entropy = pd.Series(index=sensors)
    for sensor in tqdm(sensors):
        col = csv_data[sensor].values
        numentries = len(col)
        labelcounts = {}
        for featVec in col:
            currentlabel = featVec
            if currentlabel not in labelcounts.keys():
                labelcounts[currentlabel] = 0
            labelcounts[currentlabel] += 1
        shannonent = 0.0
        for key in labelcounts:
            prob = float(labelcounts[key]) / numentries
            shannonent -= prob * log(prob, 2)
        entropy[sensor] = shannonent

    return entropy


def info_pearsonrs(csv_data: pd.DataFrame):
    """
    任意两列之间的皮尔逊相关系数

    :param csv_data: 要计算的表格
    :return: pd.DataFrame，任意两列数据的相关系数
    """
    print('pearsonr')
    time.sleep(0.1)
    sensors = csv_data.columns.tolist()
    pearsonrs = pd.DataFrame(index=sensors, columns=sensors)
    containalpha = pd.Series(index=sensors)
    for sensor in sensors:
        if contain_alpha(csv_data[sensor].values):
            containalpha[sensor] = 1
        else:
            containalpha[sensor] = 0
    for sensor1 in tqdm(sensors):
        if containalpha[sensor1] == 1:
            continue
        for sensor2 in sensors:
            if containalpha[sensor2] == 1:
                continue
            mean1 = csv_data[sensor1].mean()
            csv_data[sensor1].fillna(mean1, inplace=True)
            col1 = csv_data[sensor1].values
            mean2 = csv_data[sensor2].mean()
            csv_data[sensor2].fillna(mean2, inplace=True)
            col2 = csv_data[sensor2].values
            pearsonrs.loc[sensor1, sensor2] = pearsonr(col1, col2)

    return pearsonrs


def info_integralitys(csv_data: pd.DataFrame):
    """
    每一列的完整性

    :param csv_data: 要计算的表格
    :return: pd.Series，每一列数据的完整性
    """
    print('integrality')
    time.sleep(0.1)
    sensors = csv_data.columns.tolist()
    integrality = pd.Series(index=sensors)
    for sensor in tqdm(sensors):
        col = csv_data[sensor]
        integrality[sensor] = len(col.dropna().values) / len(col.values)

    return integrality
