x=open('iris.data','r')
y=list()
for a in x:
    if a=='\n':
        break
    t=a.split(',')
    t[0] = float(t[0])
    t[1] = float(t[1])
    t[2] = float(t[2])
    t[3] = float(t[3])
    t[4] = t[4][0:-1]
    y.append(t)

#FUNTION TO FIND MAXIMUM VALUE OF A COLUMN
def find_max(y,col):
    max_val = y[0][col]
    #print(col)
    for i in range(len(y)):
        
        if (y[i][0] > max_val):
            max_val = y[i][col]  
    print('maximum value in column {} = {}'.format(col+1,max_val))

#FUNTION TO FIND MINIIMUM VALUE OF A COLUMN
def find_min(y,col):
    min_val = y[0][col]
    #print(col)
    for i in range(len(y)):
        
        if (y[i][0] < min_val):
            max_val = y[i][col]  
    print('minimum value in column {} = {}'.format(col+1,min_val))

#FUNCTION TO FIND THE MEAN FOR A CCOLUMN
def find_mean(y,col):
    s=0
    for i in range(len(y)):
        s = s + y[i][col]
    mean = s/len(y)
    print('Mean value for column {} = {}'.format(col+1,mean))

for i in range(4):
    find_max(y,i)
    find_min(y,i)
    find_mean(y,i)
    print('\n')
