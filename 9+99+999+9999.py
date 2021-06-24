a = input('enter an integer:')
s = 0
for i in range(1,5):
    print(a*i,end='')
    if i != 4:
        print(' + ',end='')
    else:
        print(' =',end=' ')
for i in range(1,5):
    s = s + int(a*i)            
print(s)
