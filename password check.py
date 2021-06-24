'''print("password validity critirea:")
print('1. At least 1 letter between [a-z]')
print('2. At least 1 number between [0-9]')
print('3. At least 1 letter between [A-Z]')
print('4. At least 1 character from [$#@]')
print('5. Minimum length of transaction password:6')
print('6. Maximum length of transaction password: 12')'''



valid = list()

x = input("Enter a sequence of password seperated by commas :")
y = x.split(',')

for i in range(len(y)):

    flag = y[i]
    lwr,upr,num,sp_ch=0,0,0,0
    if not(len(flag)>=6 and len(flag)<=12):
        continue

    for j in range(len(flag)):
        
        if(flag[j].islower()):
            lwr += 1
        elif(flag[j].isupper()):
            upr += 1
        elif(flag[j].isnumeric()):
            num += 1
        else:
            sp_ch+=1
    if (lwr>=1 and upr>=1 and num>=1 and sp_ch>=1):
        valid.append(flag)
x=','.join(valid)
print('\nvalid passwords :',x)

        
