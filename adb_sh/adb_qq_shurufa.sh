#！/bin/bash
for ((i=1;i<=100;i++));
do
sleep 4
adb shell input tap 704 2342 # 开启聊天框
sleep 4
adb shell input tap 765 883 # 关闭
done
