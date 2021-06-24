def pascal(n):
    l=[1]
    print(' '*(n-1),1)
    for i in range(n-1):
        nl=[]
        nl.append(l[0])
        for j in range(len(l)-1):
            nl.append(l[j]+l[j+1])
        nl.append(l[-1])
        l=nl
        print(' '*(n-i-1),end='')
        for k in range(len(l)):
        	print(l[k],end=' ')
        #print('\n')	
n=int(input('enter the no. of rows you need in pascal triangle :'))
pascal(n)
