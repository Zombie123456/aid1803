def swap(l,i,j):
    t = l[i]
    l[i] = l[j]
    l[j] = t

def select_sort(l):
    i = 0
    while i < len(l) - 1:
        minindex = i
        j = i + 1
        while j < len(l):
            if l[j] < l[minindex]:
                minindex = j
            j += 1
        if minindex != i:
            swap(l,minindex,i)
        i += 1
        print(l)
    print(l)

l = [5,4,2,1,3]
select_sort(l)