#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :main.py
@Date         :2022/03/03 15:24:42
@Author       :Xinqi Chen 
@Software     :VScode
@Description  :main function 
'''

import numpy as np
from utils import read_data, divide_files_by_name
from plot import plot_mag, stand_plot
from config import data_folder, save_folder, different_char

if __name__ == '__main__':
    
    read_data(save_folder)
    data_name = '对应'
    data = np.load(data_folder + data_name + '.npy')
    plot_mag(data, data_name, data_start=2, data_end=10)  # start time and end time of data (s)
    # stand_plot(data, data_name)