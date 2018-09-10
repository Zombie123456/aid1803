# 汉诺塔.py
count = 1


def main():
    n = int(input('输入盘子个数:'))
    hanoi(n, 'A', 'C', 'B')


def hanoi(n, A, C, B):
    global count
    if n < 1:
        print('False')
    elif n == 1:
        print('%d:\t%s -> %s' % (count, A, C))
        count += 1
    elif n > 1:
        hanoi(n - 1, A, B, C)
        hanoi(1, A, C, B)
        hanoi(n - 1, B, C, A)


if __name__ == '__main__':
    main()
