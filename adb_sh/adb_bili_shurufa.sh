#！/bin/bash
for ((i=1;i<=100;i++));
do
sleep 2
adb shell input tap 508 171  # 打开上边的输入法
sleep 2
adb shell input tap 1003 149 # 点击取消
done