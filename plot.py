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
from config import sample_rate

def plot_mag(data, label, data_start=0, data_end=-1):
    '''
        plot mag data according to its label, and show part of the data
    '''

    plt.xlabel('time(s)')
    plt.ylabel('magnitude')
    if data_end == -1:
        data_end = len(data)/50 - data_start
    x_range = np.arange(data_start, data_end, 1/sample_rate)
    plt.plot(x_range, -data[int(data_start*sample_rate):int(data_end*sample_rate), 1], label='x', color='b')
    x_ticks = np.linspace(data_start, data_end, int((data_end - data_start)//5))
    plt.xticks(x_ticks)
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    plt.xlim(data_start, data_end)
    
    # plt.subplot(132)
    # plt.xlabel('time(s)')
    # plt.ylabel('magnitude')
    # plt.plot(x_range, data[data_start:data_end, 1], label='y', color='r')
    # x_ticks = np.arange(0, len(data)/50, 5)
    # plt.xticks(x_ticks)
    # plt.legend()
    # bottom, top = plt.ylim()
    # plt.ylim((bottom, top))
    
    # plt.subplot(133)
    # plt.xlabel('time(s)')
    # plt.ylabel('magnitude')
    # plt.plot(x_range, data[data_start:data_end, 2], label='z', color='g')
    # x_ticks = np.arange(0, len(data)/50, 5)
    # plt.xticks(x_ticks)
    # plt.legend()
    # bottom, top = plt.ylim()
    # plt.ylim((bottom, top))
    # f.suptitle(f'{label}')
    plt.title(f'{label}')
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
    plt.plot(x_range, data[:, 0], label='x', color='b')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(132)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[:, 1], label='y', color='b')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    plt.subplot(133)
    plt.xlabel('time')
    plt.ylabel('magnitude')
    plt.plot(x_range, data[:, 2], label='z', color='b')
    plt.legend()
    bottom, top = plt.ylim()
    plt.ylim((bottom, top))
    
    f.suptitle(f'{label}')
    plt.savefig(f'./pics/standard_{label}.png')
    plt.show()