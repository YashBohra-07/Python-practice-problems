y = list()
result=list()

for i in range(1000,3000):
    y.append(i)

print('list = ',y)


for i in range(len(y)):
    
    count=0
    x = str(y[i])
    
    for j in range(len(x)):
       
        t=int(x[j])
        if t!=0:
            
            if t%2==0:
                count+=1
                
            else:
                break

    if count==len(x):
        
        result.append(int(x))
        
print('result = ',result)
      
