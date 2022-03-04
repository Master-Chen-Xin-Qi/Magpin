#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :utils.py
@Date         :2022/03/02 21:14:02
@Author       :Xinqi Chen
@Software     :VScode
@Description  :basic function for data process
'''
import os
import numpy as np
from config import different_char


def divide_files_by_name(input_folder, different_char):
    '''
        Read files of different categories and divide into several parts
    '''
    file_dict = dict()
    for char in different_char:
        file_dict[char] = []
        for (root, _, files) in os.walk(input_folder):
            for filename in files:
                if char in filename:
                    file_ = os.path.join(root, filename)
                    file_dict[char].append(file_)
    return file_dict

def read_single_file(single_file):
    '''
        Read data from a single file
    '''
    mag_data = []
    fid = open(single_file, 'r')
    for line in fid:
        if line.strip() == '':
            continue
        else:
            line = line.strip('\n')
            line = line.split(',')
            mag_data.append([float(line[-3]), float(line[-2]), float(line[-1])])
    return np.array(mag_data)

def read_data(input_folder):
    '''
        Read and merge all data of the same char
    '''
    file_dict = divide_files_by_name(input_folder, different_char)
    for char in different_char:
        total_data_per_char = np.array((0, 0, 0))
        for single_file in file_dict[char]:
            mag_data = read_single_file(single_file)
            total_data_per_char = np.vstack((total_data_per_char, mag_data))
        label = char[-1]
        if total_data_per_char.ndim < 2:
            continue
        total_data_per_char = total_data_per_char[1:]
        print(f"char:{label} data size:{total_data_per_char.shape}")
        np.save(f'./data/{char}.npy', total_data_per_char)
    

def fft_transform(vector):
    '''
        FFT transform, save the real part
    '''
    transformed = np.fft.fft(vector)
    return np.abs(transformed)

def gauss_filter(vector, sigma):
    '''
        Gaussian transform to filter some noise
    '''
    import scipy.ndimage
    gaussian_vector = scipy.ndimage.filters.gaussian_filter(vector, sigma)
    return gaussian_vector

def PCA(vector, dimension):
    '''
        Using PCA to reduce dimension
    '''
    from sklearn.decomposition import PCA
    pca = PCA(n_components=dimension)
    vector = pca.fit_transform(vector)
    print('using pca...', vector.shape)
    return vector

def train_test_eval_split(data, label, test_size=0.1, val_size=0.2):
    '''
        Split data into train, test, and evaluation, with test_size and val_size
    '''
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=test_size, random_state=0)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=val_size, random_state=0)
    print(f'train size:{len(x_train)}  val size:{len(x_val)} test size:{len(x_test)}')
    return (x_train, y_train), (x_val, y_val), (x_test, y_test)

# def confusion_matrix()

if __name__ == '__main__':
    input_folder = "C:/Users/ASUS/Desktop/科研/magpin/PINs数据/Nexus-Li-Lightness-PIN-1119"
    # print(divide_files_by_name(input_folder, different_char))
    # read_data(input_folder)
    # a = np.ones((3, 4))
    # print(fft_transform(a).shape)
    data = np.load('./data/PIN=1.npy')
    label = []
    train_test_eval_split(data, )