
import RPi.GPIO as GPIO
import time
 
# 设置编码方式
GPIO.setmode(GPIO.BOARD)
 
# 设置引脚
COM = 32
g = 29
f = 18
a = 11
b = 12
e = 16
d = 15
c = 13
h = 22
 
# 设置各个数字的显示方式
num0 = [a, f, b, e, c, d]
num1 = [f, e]
num2 = [a, b, g, e, d]
num3 = [a, b, g, c, d]
num4 = [f, g, b, c]
num5 = [a, f, g, c, d]
num6 = [a, f, g, e, c, d]
num7 = [a, b, c]
num8 = [a, f, b, g, e, c, d]
num9 = [a, f, g, b, c]
 
countdown = [num9, num8, num7, num6, num5, num4, num3, num2, num1, num0]
 
# COM端给高电平
GPIO.setup(COM, GPIO.OUT)
GPIO.output(COM, GPIO.HIGH)
 
for num in countdown:
    # 其他引脚给低电平
    for i in num:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)
 
    time.sleep(1)
    GPIO.cleanup(num)
 
# 释放COM引脚
GPIO.cleanup(COM)