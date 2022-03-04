#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :read_realtime.py
@Date         :2022/03/04 19:03:59
@Author       :Xinqi Chen 
@Software     :VScode
@Description  :plot mag data in real time
'''

# 手机IP是10.162.214.150
# 本机IP是10.162.142.205
import socket, time, os, numpy as np, pandas as pd
from collections import deque
import matplotlib.pyplot as plt

minutes_save_total = 5
url = "10.162.142.205"
folder_save = "./real_time_data" + time.strftime('%m%d', time.localtime(time.time())) + '/'
data_save = 'sumsung-test.txt'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((url, 8090))
check_save_window_length = 20
max_entries = 1000  # 保存的最大个数，之后开始向右移动
sample_rate = 50

# Real Plot
class RealtimePlot:
    def __init__(self, axes):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axes = axes
        self.max_entries = max_entries
        self.lineplot, = axes.plot([], [], "b-")
        self.axes.set_autoscaley_on(True)
        
    def add(self, x, y):
        self.axis_x.extend(x)
        self.axis_y.extend(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim()
        self.axes.autoscale_view()  # rescale the y-axis
        
    def animate(self, figure, callback, interval=50):
        import matplotlib.animation as animation
        
        def wrapper(frame_index):
            self.add(*callback(frame_index))
            self.axes.relim()
            self.axes.autoscale_view()  # rescale the y-axis
            return self.lineplot
        animation.FuncAnimation(figure, wrapper, interval=interval)


# 文件检查
if not os.path.exists(folder_save):
    os.mkdir(folder_save)
if os.path.exists(folder_save + data_save):
    pass
    # os.remove(folder_save + data_save)

# 处理
packages_data = []
packages_save_once = 10 
start_time = time.time()

i = 0

# Plot related
fig = plt.figure()
axes1 = fig.add_subplot(111)  # define figures
plt.xlabel('Time(s) %.2fs/data' % (1 / sample_rate))
plt.ylabel('Magnetic Signals(Not uT)')
display1 = RealtimePlot(axes1)
previous_package_time = start_time
packages_data_plot = []
i = 0
while True:        
    # 读取数据
    data, address = sock.recvfrom(150)
    one_package = data.decode('ascii')
    # Real Plot
    time_now = time.time()
    previous_package_time = time_now
    # print(one_package)
    one_package = one_package.split(',')
    # print(len(one_package))
    if i == 0:
        previous = float(one_package[-3])
        # previous_previous = 0
    if len(one_package) > 4:  
        # WARNING HERE: Different phones are different
        all_ = float(one_package[-2])  # - np.abs(float(one_package[-2]))  # + np.abs(float(one_package[-3]))
        one_package_plot = all_  # - previous
        one_package = [one_package[0], one_package[-3], one_package[-2], one_package[-1]]        
        # print(one_package_plot)
        # one_package_plot__ = one_package_plot - previous_previous
        packages_data_plot.append(one_package_plot)  # Four info: time, x-mag,y-mag,z-mag
        packages_data.append(one_package)  # Four info: time, x-mag,y-mag,z-mag
        # previous = all_
        # previous_previous = one_package_plot
        i += 1
        print(i)

    # 存盘, 绘图
    if len(packages_data) > 1 and i % 5 == 0:
        # 绘图
        time_axis = np.linspace((previous_package_time - start_time), (time_now - start_time), len(packages_data_plot))
        # print(time_axis, one_package)
        display1.add(time_axis, packages_data_plot)
        plt.pause(0.00001)
        fid = open(folder_save + data_save, 'a')
        packages_data = pd.DataFrame(packages_data)
        packages_data.to_csv(fid, header=False, index=False)
        fid.close()
        packages_data_plot = []
        packages_data = []
        
        
    # 存一段时间，结束
    now_time = time.time()  
    if now_time - start_time > minutes_save_total * 60:
        print("\n\nDone!")
        break
