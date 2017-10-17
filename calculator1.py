import sys

def tax(i):
	i = i-3500
	if i < 0:
		i = 0
	if i <= 1500:
		i = i*0.03-0
	if 1500 < i <= 4500:
		i = i * 0.1 - 105
	if 4500 < i <= 9000:
		i = i  - 555
	if 9000 < i <= 35000:
		i = i* 0.25 - 1005
	if 35009 < i <= 55000:
		i = i * 0.30 - 2755
	if 55000 < i <= 80000:
		i = i * 0.35 - 5505
	if i > 80000:
		i = i * 0.45 - 13505
	return format(i,".2f")	#将i格式化为 保留两位小数格式注意‘.’不要忘了

def main():
	try:
		pay = int(sys.argv[1]) #将输入的内容转换为int，如果不能转换，则返回except内容
		print (tax(pay))

	except ValueError:
		print ("plesse input an integer.")

if __name__ == '__main__':
	main()

