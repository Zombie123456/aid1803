# 三角树塔.py
def trinumpagoda():
    n = int(input('请输入树塔层数:'))
    p = [[]for i in range(n)]
    for i in range(n):
        L = []
        s = input('请输入' + str(i + 1) + '个数')
        L = s.split(sep=',')
        for a in L:
            p[i].append(int(a))
        if len(L) > i + 1:
            print('输入数值的个数不正确!')
            return
    D = [[]for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
                D[i].append(p[i][j])
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            if D[i + 1][j] + p[i][j] >= D[i + 1][j + 1] + p[i][j]:
                D[i][j] = D[i + 1][j] + p[i][j]
            else:
                D[i][j] = D[i + 1][j + 1] + p[i][j]
    print('最大数值之和为:', D[0][0])
    path = []
    path.append('(0,0)')
    m = 0
    mymax = D[0][0]
    for i in range(1, n):
        if mymax - p[i - 1][m] == D[i][m]:
            mymax = D[i][m]
        else:
            mymax = D[i][m + 1]
            m = m + 1
        path.append('(' + str(i) + ',' + str(m) + ')')
    print('路径为:', path)


if __name__ == '__main__':
    trinumpagoda()
# 请输入树塔层数:5
# 请输入1个数9
# 请输入2个数12,15
# 请输入3个数10,6,8
# 请输入4个数2,18,9,5
# 请输入5个数19,7,10,4,16
# 最大数值之和为: 59
# 路径为: ['(0,0)', '(1,0)', '(2,0)', '(3,1)', '(4,2)']
