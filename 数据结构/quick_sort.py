# quick_sort.py
import random

 
def swap(l, i, j):
    t = l[i]
    l[i] = l[j]
    l[j] = t


def quicksort(l):
    quicksorthelper(l, 0, len(l)-1)


def quicksorthelper(l, left, right):
    if left < right:
        pivotlocation = partition(l, left, right)
        quicksorthelper(l, left, pivotlocation-1)
        quicksorthelper(l, pivotlocation+1, right)


def partition(l, left, right):
    mid = (left+right)//2
    pivot = l[mid]
    l[mid] = l[right]
    l[right] = pivot
    boundary = left
    for index in range(left, right):
        if l[index] < pivot:
            swap(l, index, boundary)
            boundary += 1
    swap(l, right, boundary)
    return boundary


def main(size=20, sort=quicksort):
    l = []
    for count in range(size):
        l.append(random.randint(1, size+1))
    print(l)
    quicksort(l)
    print(l)


if __name__ == '__main__':
    main()
