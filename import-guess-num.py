#3-2程式練習 猜數字遊戲
import random

r = random.randint(1,100)
while True:
	num = int(input('請輸入猜測數字: '))
	if r > num:
		print("還要再猜大一點的數字")
	elif r < num:
		print("還要再猜小一點的數字")
	elif r == num:
		print('恭喜你! 終於猜對了')
		break