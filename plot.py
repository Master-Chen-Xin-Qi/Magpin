#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :plot.py
@Date         :2022/03/03 15:34:42
@Author       :Xinqi Chen 
@Software     :VScode
@Description  :plot mag data
'''
import matplotlib.pyplot as plt
import numpy as np

def plot_mag(data, label):
    '''
        plot mag data according to its label
    '''
    plt.figure()
    data_l = len(data)
    x_range = np.arange(0, data_l/50, 0.02)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.title(f'{label}')
    plt.plot(x_range, data[:, 0], label='x')
    plt.plot(x_range, data[:, 1], label='y')
    plt.plot(x_range, data[:, 2], label='z')
    plt.legend()
    plt.savefig(f'./pics/{label}.png')
    plt.show()