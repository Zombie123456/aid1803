# file.py
import os
import multiprocessing as mp


def cp1(f, num1):
    try:
        f1 = open('./test1.txt', 'r+b')
        s = f.read(num1)
        f1.write(s)
    finally:
        f1.close()


def cp2(f, num1, num2):
    try:
        f1 = open('./test1.txt', 'r+b')
        f.seek(num1)
        s = f.read(num2)
        f1.seek(num1)
        f1.write(s)
    finally:
        f1.close()


def main():
    f = open('./test.txt', 'r+b')
    num = os.path.getsize('./test.txt')
    num1 = num // 2
    num2 = num - num1
    p1 = mp.Process(target=cp1, args=(f, num1))
    p2 = mp.Process(target=cp2, args=(f, num1, num2))
    p1.start()
    p2.start()
    f.close()


if __name__ == '__main__':
    main()
