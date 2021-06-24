#write a program to generate a list of division along with topper of class using dictionary.

result = {}
n = int(input("enter the no. of divisons :"))
print('enter the divison name along with topper of that divison:')
i = 1
while i <= n:
    div = input('divison {}:'.format(i))
    top = input('topper :')
    result[div] = top
    i +=1

print('\nresult created successfully !\n')
print('press 1 to add a new detail')
print('press 2 to update an existing detail')
print('press 3 to delete a detail')
print('press 4 to see result')
print('press 5 to exit')      


while 1:
    q = input('want to perform any of above tasks?(yes or no) :')
    if q == 'yes':  
      choice = int(input('MAKE YOUR CHOICE :'))
    else:
      break

    if choice == 2:
      div = input('name of divison to be updated:')
      top = input('topper :')
      result[div] = top    

    elif choice == 1:
      div = input('divison name to be added:')
      if div in result:
          print('devison already exists,try updating.')
          continue
      top = input('topper :')
      result[div] = top

    elif choice ==  3:
      div = input('enter divison whose detail is to be deleted: ')
      result.pop(div)

    elif choice == 4:
      print('final result :-')
      x = sorted(result.keys())
      for i in x:
        print(i,result[i])

    else:
      break

      
        
    

    



    
