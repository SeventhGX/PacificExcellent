# 船舶数据质量评估系统
## 1、运行需求

系统：Windows / Linux
需求包：numpy，pandas

## 2、运行方法

### 2.1、整理原始数据

运行`main.py`，参数设定如下：

```
python main.py --start_status=0 --rawdata_filepath=your_path
```

使用时请将命令中的`your_path`用存放原始数据的文件夹路径替代。运行完成后，会在当前目录下生成`PacificExcellent.csv`文件保存经过初步整理后的数据。

### 2.2、获取相关指标

运行`main.py`，可以查看帮助获取系统支持的指标列表：

```
pyhton main.py -h
```

获取指标计算结果，命令格式如下：

```
python main.py --csv_path='./PacificExcellent.csv' 
```

其中`'./PacificExcellent.csv'`可使用自定义的csv文件路径替代。

## 3、后续开发与维护

系统计算指标的函数全部保存在`calculator.py`中，每一项指标都有一个对应的函数，如果需要进行修改，直接对函数体进行修改即可。

如果需要添加/删除某些指标，请在完成相关函数的编写之后，对`main.py`文件中的`parse_args()`函数进行相应的修改，添加/删除相应的参数项；同时在`command2function.json`文件中，按照`参数名: 函数名`的格式补全参数与函数的对应关系。

