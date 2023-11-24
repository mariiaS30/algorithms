a = [6, 5, 1, 3, 8, 4, 7, 9, 2]

wall = 0

while wall != len(a)-1:
    pivot_el = a[-1]

    for i in range(wall, len(a)-2):
        if a[i] < pivot_el:
            a[wall], a[i] = a[i], a[wall]
            wall = wall + 1
    a[-1], a[wall] = a[wall], a[-1]
    wall = wall + 1
print(a)
