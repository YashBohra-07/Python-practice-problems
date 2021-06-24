list=[2,3,4,5,6,7,8,9,11]
for i in range(0,9):
    count=0
    for j in range(1,list[i]+1):
        if list[i]%j==0:
            count+=1
        #else:
            #continue
    if count<=2:
        print(list[i])
        
            
