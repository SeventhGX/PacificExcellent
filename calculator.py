import pandas as pd
from tqdm import tqdm
from scipy.stats import pearsonr
from math import log


def info_entropys(csv_data: pd.DataFrame):
    """
    每一列的信息熵

    :param csv_data: 要计算的表格
    :return: pd.Series，传感器数据的信息熵
    """
    sensors = csv_data.columns.tolist()  # 传感器列表
    entropy = pd.Series(index=sensors)
    for sensor in tqdm(sensors):
        col = csv_data[sensor].values
        numentries = len(col)  # 样本数
        labelcounts = {}  # 该数据集每个类别的频数
        for featVec in col:  # 对每一行样本
            currentlabel = featVec  # 该样本的标签
            if currentlabel not in labelcounts.keys():
                labelcounts[currentlabel] = 0
            labelcounts[currentlabel] += 1
        shannonent = 0.0
        for key in labelcounts:
            prob = float(labelcounts[key]) / numentries  # 计算p(xi)
            shannonent -= prob * log(prob, 2)
        entropy[sensor] = shannonent

    return entropy


def info_pearsonrs(csv_data: pd.DataFrame):
    """
    任意两列之间的皮尔逊相关系数

    :param csv_data: 要计算的表格
    :return: pd.DataFrame，任意两传感器数据的相关系数
    """
    sensors = csv_data.columns.tolist()  # 传感器列表
    pearsonrs = pd.DataFrame(index=sensors, columns=sensors)
    for sensor1 in tqdm(sensors):
        for sensor2 in sensors:
            mean1 = csv_data[sensor1].mean()
            csv_data[sensor1].fillna(mean1, inplace=True)
            col1 = csv_data[sensor1].values
            mean2 = csv_data[sensor2].mean()
            csv_data[sensor2].fillna(mean2, inplace=True)
            col2 = csv_data[sensor2].values
            pearsonrs.loc[sensor1, sensor2] = pearsonr(col1, col2)

    return pearsonrs
