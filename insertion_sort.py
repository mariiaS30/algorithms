a = [5, 6, 2, 0, 9, 1, 3]
print(a)

for k in range(len(a)-1):
    for i in range(k-1, 0, -1):
        if a[k] < a[i]:
            a[i], a[k] = a[k], a[i]

print(a) 

