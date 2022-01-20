#3-7 程式練習 留言分析程式 及 留言篩選

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

new = []
num = 100

for d in data:
	if len(d) < num :
		new.append(d)

print('一共有', len(new), '筆留言長度小於', num)
print(new[0])
print(new[1])


good = []

for d in data:
	if 'good' in d:
		good.append(d)

print('一共有', len(good), '個留言提到good')
print(good[0])

#清單快寫法
good_fast = [d for d in data if 'good' in d]
print('一共有', len(good_fast), '個留言提到good')
