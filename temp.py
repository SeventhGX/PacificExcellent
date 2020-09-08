import os
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from math import log

path = './PacificExcellent_CCS/PacificExcellent_CCS'
filelist = os.listdir(path)

# 删除解压之后留下的zip文件
# for filename in filelist:
#     if 'zip' in filename:
#         os.remove(f'{path}/{filename}')


# 整合数据生成csv文件
# name = []
# for filename in filelist:
#     name.append(filename.split('.')[0])
# csv_data = np.empty((len(name), 0))
# csv_data = pd.DataFrame(data=csv_data, index=name)
#
# for filename in tqdm(filelist):
#     with open(f'{path}/{filename}', 'r') as datafile:
#         data = json.load(datafile)
#         for x in data:
#             if x not in csv_data.columns.tolist():
#                 csv_data[x] = np.nan
#             csv_data.loc[filename.split('.')[0], x] = data[x]
#
# csv_data.to_csv('PacificExcellent.csv')
# csv_data.to_excel('PacificExcellent.xlsx')


# 简单统计
csv_data = pd.read_csv('./PacificExcellent.csv', low_memory=False)
# cols = []
# for col in tqdm(csv_data.columns.tolist()):
#     nums = []
#     col_data = csv_data[col].values
#     for x in col_data:
#         if x == x and x not in nums:
#             nums.append(x)
#     if len(nums) == 4:
#         print(col)
#         cols.append(nums)
#         plt.plot(col_data)
#         plt.show()
# 92017 92020
mean1 = csv_data['92018'].mean()
csv_data['92018'].fillna(mean1, inplace=True)
col1 = csv_data['92018'].values
mean2 = csv_data['92020'].mean()
csv_data['92020'].fillna(mean2, inplace=True)
col2 = csv_data['92020'].values
# print(pearsonr(col1, col2))
numEntries = len(col1)  # 样本数
labelCounts = {}  # 该数据集每个类别的频数
for featVec in col1:  # 对每一行样本
    currentLabel = featVec  # 该样本的标签
    if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
    labelCounts[currentLabel] += 1
shannonEnt = 0.0
for key in labelCounts:
    prob = float(labelCounts[key]) / numEntries  # 计算p(xi)
    shannonEnt -= prob * log(prob, 2)  # log base 2
print(shannonEnt)

# col_data = csv_data['12216'].dropna().values
# a = 0
# for x in col_data:
#     x = str(x)
#     if ('.' in x and len(x) == 5) or ('.' not in x and len(x) == 4):
#         a += 1
# print(a)
# print(len(col_data))
# print(a / len(col_data))
