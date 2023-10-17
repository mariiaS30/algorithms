a = [5, 6, 2, 0, 9, 1, 3]
# a = [1, 3, 4, 5, 2]
print(a)

pointer = 0
index = 0
for k in range(len(a)-1):
    now_number = a[-1]
    # print(now_number)
    index = pointer
    for j in range(0, pointer + 1):
        if now_number < a[j]:
            index = j   
    pointer = pointer + 1
    # print(index)       
 # print(f'i = {i}')
    for j in range(len(a)-1, index, -1):
        a[j] = a[j-1]
    a[index] = now_number
    
    print(now_number, index)
    print(a)    
    
print(a) 

#исправить ошибку с index
# 1, 3, 4, 5, 2
# i = 0
# index = 0 
# 5 2 4 7 3