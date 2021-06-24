def fibo(n):
	a,b,=0,1
	if n==0:
		print(0)
	elif n==1:
		print('0  1')
	else:	
		while True:
      c = a + b
  		if(c>n):
       	break
      print(c,' ',end='')
   		a,b=b,c
      		
        	#print(b,' ',end="")
fibo(20)        
