#！/bin/bash
for ((i=1;i<=100;i++));
do
sleep 5
adb shell input tap 597 534  # 点击屏幕打开输入法
sleep 5
adb shell input keyevent 4 # 返回键
done