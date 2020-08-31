#打印1到100之间（包含1和100）、不是7的倍数、且不含7的数字，每行打印一个数字
for num in range(1,101):
	if((str(num).find('7') != -1) or (int(num) % 7 == 0)):
		continue
	else:
		print(num)
