#3-7 程式練習 留言分析程式

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 ==0:
			print(len(data))
print(len(data))

print(data[0])
print('---------------------')
print(data[1])