#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :Recv.py
@Date         :2022/03/04 13:08:10
@Author       :Xinqi Chen 
@Software     :VScode
@Description  :Receive mag data from mobile phone
'''

import socket, time, os
import pandas as pd, numpy as np
import math
from config import save_folder
saveTime = 0.4  # Minutes


def collect_mag(data_save):
    folder_save = save_folder
    if not os.path.exists(folder_save):
        os.mkdir(folder_save)
    if os.path.exists(folder_save + data_save):
        os.remove(folder_save + data_save)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 8090))  # 10.162.117.28
    packages_data = []
    save_packages = 500
    st = time.time()
    count_packages = 0
    while True:
        # 读数
        data, _ = sock.recvfrom(150)
        # print("111")
        one_package = data.decode('ascii')
        split_package = one_package.split(',')
        if len(split_package) >= 13:  # WARNING HERE: Different phones are different
            packages_data.append(eval(one_package))  
            count_packages += 1
        # 存盘
        if len(packages_data) > save_packages:
            fid = open(folder_save + data_save, 'a')
            packages_data = pd.DataFrame(packages_data)
            packages_data.to_csv(fid, header=False, index=False)
            fid.close()
            packages_data = []
            print('Saving mag data\t', count_packages)
        et = time.time()  
        if et - st > saveTime * 60:
            print('Mag Sensor Used time: %d seconds, collected %d samples' % (et - st, count_packages))
            break
        

if __name__ == '__main__':
    # Collect
    data_save = 'adb5.txt'
    collect_mag(data_save)

