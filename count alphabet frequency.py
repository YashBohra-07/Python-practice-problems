name = input('enter your name:')
freq = {}
for i in name:
    if i not in freq:
        freq.setdefault(i,0)
    freq[i]+=1

print(freq)

     
