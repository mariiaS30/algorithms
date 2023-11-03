a = ['a', 'b', 'g', 'h', 'c']

pointer = 0
for k in range(len(a)-1):
    now_number = a[pointer + 1]
    index = pointer + 1   
    j = 0
    while now_number > a[j]:
        j = j + 1   
    index = j   
    pointer = pointer + 1
   
    for j in range(pointer, index, -1):
        a[j] = a[j-1]
    a[index] = now_number
       
print(a) 

