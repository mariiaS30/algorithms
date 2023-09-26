a = [5, 6, 2, 0, 9, 1, 3]
print(a)
times = len(a)-1
m = 1
for k in range (times):
    for i in range (len(a)-m):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    m = m + 1

print(a)