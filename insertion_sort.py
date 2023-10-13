a = [5, 6, 2, 0, 9, 1, 3]
print(a)

index = 0
i = len(a) - 2
for k in range(len(a)-1):
    now_number = a[-1]
    while now_number < a[i]:
        i = i-1
    
    index = i + 1
    print(index)
    for j in range(len(a)-1, index, -1):
        a[j] = a[j-1]
    # a[index] = now_number    

# print(a) 

#исправить ошибку с index