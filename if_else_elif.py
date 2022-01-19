age = input('請輸入年齡: ')
age = int(age)
if age < 13:
	print('國小生')
elif age >= 13 and age <18 :
	print('國高中生')
elif age >=18 and age <22:
	print('大學生')
else:
	print('社會人士')

