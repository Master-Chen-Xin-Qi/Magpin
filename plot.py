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
from config import sample_rate, fig_size, pic_save

def plot_mag(data, label, data_start=0, data_end=-1):
    '''
        plot mag data according to its label, and show part of the data
        data_start : begin time of the data (s)
        data_end   : end time of the data (s)
    '''

    plt.xlabel('time(s)')
    plt.ylabel('magnitude')
    if data_end == -1:
        data_end = len(data)/50 - data_start
    x_range = np.arange(data_start, data_end, 1/sample_rate)
    plt.plot(x_range, data[int(data_start*sample_rate):int(data_end*sample_rate), 0], label='x', color='b')
    x_ticks = np.linspace(data_start, data_end, int((data_end - data_start)))
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
    
    
def plot_action_cf(df_cm, title_, figure_saved, target_names, rotation,use_notation,font_size):
    '''
        plot the confusion matrix with heat bar
    '''
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=fig_size)
    fig.set_tight_layout({'pad': 1})
    ax = sn.heatmap(ax=ax, data=df_cm, annot=use_notation, cmap=plt.cm.Reds, vmin=0, vmax=1,
                    fmt=".2f", annot_kws={"size": font_size - 15})
    cbar = ax.collections[0].colorbar
    # here set the labelsize by 20
    cbar.ax.tick_params(labelsize=font_size - 15)  # colorbar
    ax.tick_params(labelsize=font_size - 15, width=1)
    ax.set_aspect(1)
    if target_names is not None:
        tick_marks = np.arange(0, len(target_names)) + 0.5 
        plt.xticks(tick_marks, target_names,fontsize=font_size-10, rotation=rotation) # [1,2,3,4,5,6,7,8,9,10,11]
        plt.yticks(tick_marks, target_names, rotation=0, fontsize=font_size-10)
    plt.title(title_)
    plt.savefig(pic_save + figure_saved + '.eps', format='eps')    
    plt.savefig(pic_save + figure_saved + '.pdf', format='pdf')
    plt.show()
    return