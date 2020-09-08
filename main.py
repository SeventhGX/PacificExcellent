import os
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from math import log

rawdata_filepath = './PacificExcellent_CCS/PacificExcellent_CCS'
rawdata_filelist = os.listdir(rawdata_filepath)
