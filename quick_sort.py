# a = [5, 8, 3, 13, 67, 0, 98, 5, 78, 17, 20, 1]
# a = [0, 54, 70, 41, 80, 56, 51, 30, 47, 20, 90, 42, 10, 40, 50]
# a = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
# a = [0, 7, 8, 3, 2, 9, 1, 4, 5]
# a = [98, 6, 7, 30, 12, 4, 0, 98, 7,0, 30, 98]
def quick_sort(a):
    smaller = []
    equal = []
    larger = []
    if len(a) <= 1:
        return a
    else:
        pivot_el = a[-1]
        for i in range(len(a)):
            if a[i] < pivot_el:
                smaller.append(a[i])
            elif a[i] == pivot_el:
                equal.append(a[i])
            else:
                larger.append(a[i])
        return quick_sort(smaller) + equal + quick_sort(larger)
        
print(quick_sort(a))

