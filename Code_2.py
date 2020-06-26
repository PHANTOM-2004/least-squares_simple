from statistics import mean
import math


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass


while(True):
	Question = input('A:最小二乘估计\nB:卡方计算\n')


	while(Question == 'B'):#卡方运算
		a = float(input('Enter a:\n'))
		b = float(input('Enter b:\n'))
		c = float(input('Enter c:\n'))
		d = float(input('Enter d:\n'))
		X__2 = ((a+b+c+d)*(a*d-b*c)**2)/((a+b)*(c+d)*(a+c)*(b+d))
		print(f'卡方为:{X__2}')
		Q_1 = input('Switch?(Y/N)\n')
		if(Q_1 == 'Y'):
			break

	while(Question == 'A'):		#最小二乘估计
		Xi = []		#s输入Xi
		while(True):
			Xs = input('Type xi:\nType \'end\' to end\n\
If there is a wrong number typed,type \'C\'\n')
			if(is_number(Xs)):
				Xi.append(float(Xs))
				print(Xi)
			elif(Xs == 'end'):
				break
			elif(Xs == 'C'):
				Number_a_1=input('Which one is it?\n(Type the sequence number.)\n')
				if(is_number(Number_a_1)):
					Number_a_1 = int(Number_a_1) - 1
					Number_c_1 = input('Type the right value.\n')
					if(is_number(Number_c_1)):
						del Xi[Number_a_1]
						Xi.insert(Number_a_1, float(Number_c_1))
						print('Changed succesfully.')
						print(Xi)
					else:
						print('\aError!Enter a number.\n')
				else:
					print('\aError!Enter a number.\n')
			else:
				print('\aError!Enter a number.\n')
		Yi = []		#s输入Yi
		while(len(Yi) < len(Xi)):
			Ys = input('Type yi:\nIf there is a wrong number entered,type \'C\'.\n')
			if(is_number(Ys)):
				Yi.append(float(Ys))
				print(Yi)
			elif(Ys == 'C'):
				Number_a_2 = input('Which one is it?\n(Type the sequence number.)\n')
				if(is_number(Number_a_2)):
					Number_a_2 = int(Number_a_2) - 1
					Number_c_2 = input('Type the right value.\n')
					if(is_number(Number_c_2)):
						del Yi[Number_a_2]
						Yi.insert(Number_a_2, float(Number_c_2))
						print('\aChanged succesfully.')
						print(Yi)
					else:
						print('\aError!Enter a number.\n')
				else:
					print('\aError!Enter a number.\n')
			else:
				print('\aError!\nType again.\n')
		q_extra = input('\a是否使用指数拟合?\n(Y/N)\n')
		if(q_extra == 'Y'):
			Yi = [math.log(Y_0,math.e) for Y_0 in Yi]


		Y_2s = [Y_2**2 for Y_2 in Yi]	#Yi^2的列表
		X_2s = [X_2**2 for X_2 in Xi]	#Xi^2的列表
		XY = [m1*m2 for m1,m2 in zip(Xi,Yi)]	#XiYi的列表
		X_average = mean(Xi)	#所需数值
		Y_average = mean(Yi)
		Xi2_sum = sum(X_2s)
		Yi2_sum = sum(Y_2s)
		XY_sum = sum(XY)
		n = len(Xi)
		r = (XY_sum -  n*X_average*Y_average)/((Xi2_sum - n*X_average**2)**0.5\
		*(Yi2_sum - n*Y_average**2)**0.5)	#判断是否线性

		if(r == 0):
			print('相关系数r=0,不线性相关')
			break
		else:
			print('\nEstimated\n')


		b = (XY_sum -  n*X_average*Y_average)/(Xi2_sum - n*X_average**2)#参数a,b
		a = Y_average - b*X_average
		print(f'\nsum(XiYi)={XY_sum}\n\nsum(Xi^2)={Xi2_sum}\
			\n\nE(X)={X_average}\n\nE(Y)={Y_average}\n\nr={r}\n')

		Done = input('\nEnter \'E\' to switch.\n')
		if(Done == 'E'):
			break
		else:
			exit()