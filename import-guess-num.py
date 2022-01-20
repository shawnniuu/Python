#3-2程式練習 猜數字遊戲
import random

start = int(input('請決定隨機數字範圍開始值: '))
end = int(input('請決定隨機數字範圍結束值: '))
i = 0
r = random.randint(start,end)
while True:
	i+=1
	num = int(input('請輸入猜測數字: '))
	if r > num:
		print("還要再猜大一點的數字")

	elif r < num:
		print("還要再猜小一點的數字")

	elif r == num:
		print('恭喜你! 終於猜對了')
		print('這是你猜的第',i,'次')
		break

	print('這是你猜的第',i,'次')
	
	print()