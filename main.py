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

if __name__ == '__main__':
    
    input_folder = "C:/Users/ASUS/Desktop/科研/magpin/PINs数据/"
    read_data(input_folder)
    data_name = './npy_data/Big.npy'
    data = np.load(data_name)
    label = data_name.strip('./data/').strip('.npy')
    # plot_mag(data, label, 2, 10)
    stand_plot(data[2*50:10*50, :], label)