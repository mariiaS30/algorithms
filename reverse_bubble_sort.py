def reverse_bubble(a):
    m = 0

    for k in range(len(a)-1):
        for i in range(len(a)-1, m, -1):
            if a[i] > a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
        m = m + 1
    return a