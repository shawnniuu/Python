driving = input('請問你有沒有開過車: ')

age = int(input('你問你的年齡?: '))

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼有開過車')
		
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了阿, 怎麼還不去考')
	else:
		year = 18 - age
		print('很好, 再幾%d年就可以考駕照了'%year)
