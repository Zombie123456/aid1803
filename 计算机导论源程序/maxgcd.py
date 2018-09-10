# 最大公约数_贪心
def main():
    x = int(input('please enter integer x:'))
    y = int(input('please enter integer y:'))
    print('x和y的最大公约数是:', gcd(x, y))


def gcd(x, y):
    if x > y:
        a, b = x, y
    else:
        a, b = y, x
    if a % b == 0:
        return b
    return gcd(a % b, b)


if __name__ == '__main__':
    main()
