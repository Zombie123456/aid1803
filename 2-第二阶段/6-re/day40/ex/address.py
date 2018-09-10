# address.py
import re

def main():
    f = open('1.txt')
    s = ''
    x = input('输入端口号:')
    pattern = '^' + x + ' '
    a= 0
    while True:
        s = ''
        data = f.readline()
        if data =='\n':
            while True:
                data1 = f.readline()
                if data1 == '\n':
                    break
                a += 1
                s += data1
            if re.findall(pattern, s):
                l1 = re.findall('\w{4}\.\w+\.\w+', s)
                l2 = re.findall('\d+\.\d+\.\d+\.\d+.*', s)
                break 
    f.close()    
    print(l1)
    print(l2)

if __name__ == '__main__':
    main()
