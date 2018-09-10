a = int(input("请输入你要查找的数字"))
l = [20,44,48,55,62,66,74,88,93,99]
left = 0
right = len(l)-1
n = 0
while left <= right:
    mid = (left+right)//2
    n += 1
    if a == l[mid]:
        print("找到,索引为:",mid)
        break
    elif a < l[mid]:
        right = mid - 1
    elif a > l[mid]:
        left = mid + 1
else:
    print("未找到")
print(n)



