# 找零钱_贪心
v = [50, 20, 10, 5, 1]
n = [0, 0, 0, 0, 0]


def change():
    t = int(input('要找给顾客的零钱,单位(元):'))
    greedy(t)
    for i in range(len(v)):
        print('要找给顾客', v[i], '元的纸币:', n[i])
    s = 0
    for i in n:
        s += i
    print('要找给顾客的纸币数最少为:', s)


def greedy(t):
    if t == 0:
        return
    elif t >= v[0]:
        t = t - v[0]
        n[0] = n[0] + 1
        greedy(t)
    elif v[0] > t >= v[1]:
        t = t - v[1]
        n[1] = n[1] + 1
        greedy(t)
    elif v[1] > t >= v[2]:
        t = t - v[2]
        n[2] = n[2] + 1
        greedy(t)
    elif v[2] > t >= v[3]:
        t = t - v[3]
        n[3] = n[3] + 1
        greedy(t)
    else:
        t = t - v[4]
        n[4] = n[4] + 1
        greedy(t)


if __name__ == '__main__':
    change()
