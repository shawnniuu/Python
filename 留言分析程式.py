#3-7 程式練習 留言分析程式

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完畢,總共有', len(data),'筆資料')
sum_len = 0 
for d in data:
	sum_len+=len(d)
print('每一筆留言的平均長度為:', int(sum_len/len(data)), '個字')