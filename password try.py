#2-14程式練習 密碼重試程式

x = 0
correct = 'a123456'
print('最多輸入三次密碼')
print()

while x<3:
	passw = input("請輸入密碼: ")
	if passw != correct:
		x+=1
		if x < 3:
			print('密碼錯誤! 還有%d次機會'%(3-x))
		else:
			print('3次密碼錯誤! 冷卻30秒')
	else:
		print('登入成功')
		x=3