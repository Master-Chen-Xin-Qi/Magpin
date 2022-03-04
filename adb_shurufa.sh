#！/bin/bash

for ((i=1;i<=100;i++));
do
sleep 1.5
adb shell input tap 626 2216
sleep 1.5
adb shell input tap 626 1016
done

