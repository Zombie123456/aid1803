# debug.py
import pdb
import sys

def add(num1=0, num2=0):
    return int(num1) + int(num2)

def sub(num1=0, num2=0):
    return int(num1) - int(num2)

def main():
    print(sys.argv)
    pdb.set_trace()
    addi = add(sys.argv[1], sys.argv[2])
    print(addi)
    subs = sub(sys.argv[1], sys.argv[2])
    print(subs)


if __name__ == '__main__':
    main()
