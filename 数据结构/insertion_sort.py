# insertion_sort.py
def insertion_sort(l):
    i = 1
    while i < len(l):
        item = l[i] 
        j = i - 1
        while j >= 0:
            if item < l[j]:
                l[j + 1] = l[j]
                j -= 1
            else:
                break
        l[j + 1] = item
        i += 1
        print(l)
    print(l)

l= [2,5,1,4,3]
insertion_sort(l)
