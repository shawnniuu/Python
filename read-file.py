#讀檔

data = []
with open('food.txt','r') as f:
	for line in f:
		data.append(line.strip())
#在whih外面就關閉檔案了
print(data)