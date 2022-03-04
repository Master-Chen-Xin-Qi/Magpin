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

def plot_mag(data, label, start_time=0, end_time=-1):
    '''
        plot mag data according to its label, and show part of the data
    '''
    data_l = len(data)
    if start_time == 0 and end_time == -1:
        x_range = np.arange(0, data_l/50, 0.02)
        data_start = 0
        data_end = len(data) + 1
    else:
        x_range = np.arange(start_time, end_time, 0.02)
        data_start = int(start_time * 50)
        data_end = int(end_time * 50)
    f, ax = plt.subplots(1, 3)
    plt.subplot(131)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[data_start:data_end, 0], label='x', color='b')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(132)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[data_start:data_end, 1], label='y', color='r')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(133)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[data_start:data_end, 2], label='z', color='g')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    f.suptitle(f'{label}')
    plt.savefig(f'./pics/{label}.png')
    plt.show()
    
    
def stand_plot(data, label):
    '''
        plot the mag data after standardization
    '''
    mu_x = np.mean(data[:, 0], axis=0)
    sigma_x = np.std(data[:, 0], axis=0)
    data[:, 0] = (data[:, 0] - mu_x) /sigma_x
    
    mu_y = np.mean(data[:, 1], axis=0)
    sigma_y = np.std(data[:, 1], axis=0)
    data[:, 1] = (data[:, 1] - mu_y) /sigma_y
    
    mu_z = np.mean(data[:, 2], axis=0)
    sigma_z = np.std(data[:, 2], axis=0)
    data[:, 2] = (data[:, 2] - mu_z) /sigma_z
    x_range = np.arange(0, len(data)/50, 0.02)
    f, ax = plt.subplots(1, 3)
    plt.subplot(131)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[:, 0], label='x')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(132)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[:, 1], label='y')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(133)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[:, 2], label='z')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    f.suptitle(f'{label}')
    plt.savefig(f'./pics/standard_{label}.png')
    plt.show()