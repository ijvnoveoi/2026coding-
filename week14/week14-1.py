#week14-1.py
t = 1
while True:
	M, N = list(map(int, input() .split() ))
	if M==0 and N==0: break
	a = []
	for i in range(M):
		a.append( list(input()) )

	for i in range(M):
		for j in range(N):
			if a[i][j]=='*': continue
			a[i][j] = 0
			for ii in range(i-1, i+2):
				for jj in range(j-1, j+2):
					if ii<0 or jj<0 or ii>=M or jj>=N:
						continue
					if a[ii][jj]=='*':
						a[i][j] += 1

	if t>1: print()
	print( f'Field #{t}:' )
	for i in range(M):
		#print(a[i])
		for j in range(N):
			print(a[i][j], end='')
		print()
	t += 1
