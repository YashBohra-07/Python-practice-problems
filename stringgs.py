# WAP TO INPUT STRING CONTAINING COMMA SEPERATED VALUES AND CONVERT THOSE NUMBERS TO THEIR SQUARES

values = input('Enter some numbers seperated by commas : ')
x = values.split(',')
print('square of the entered numbers :',end=' ')
for i in range(len(x)):
    x[i] = int(x[i])
    print(x[i]**2,end=',')
print('\n\n')

#  WAP TO READ A STRING WHICH CONTAINS COMMA SEPERATED STRING TOKENS AND SORT THEM ALPHABETICALLY
#   AND DISPLAY SORTED LIST

x = input("enter some words seperated by commas :")
y = x.split(',')
print(sorted(y))
print('\n\n')


#  WAP TO READ A SENTENCE AS STRING AND SORT THEM ALPHABETICALLU,ALSO REMOVE THE DUPLICATE WORDS
#  PRINT THE RESULT

x = input('Write a sentence :')
y = x.split(' ')
temp = list()
for i in y:
    if i not in temp:                      #better and short method is to use set
        temp.append(i)
    else:
        continue
z=sorted(temp)
print(' '.join(z))
        
