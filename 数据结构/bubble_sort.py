# bubble_sort.py
def swap(l,i,j):
    t = l[i]
    l[i] = l[j]
    l[j] = t

def bubblesort(l):
    n = len(l)
    while n > 1:
        i = 1
        while i < n:
            if l[i] < l[i-1]:
                swap(l,i,i-1)
            i+=1
        n -= 1
        print(l)
    print(l)

def bubblesortwhittweek(l):
    n = len(l)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if l[i] < l[i-1]:
                swap(l,i,i-1)
                swapped = True
            i+=1
        if not swapped:return
        n -= 1
        print(l)
    print(l)

l = [5,4,2,1,3]
bubblesort(l)
# bubblesortwhittweek(l)
