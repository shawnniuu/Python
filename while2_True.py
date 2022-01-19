while True:
	mode = input('請輸入遊戲模式(1/2/q): ')
	if mode == 'q':
		print('退出')
		break
	elif mode == '1':
		print('啟動模式一')
	elif mode == '2':
		print('啟動模式二')
	else:
		print('只能輸入1/2/q')