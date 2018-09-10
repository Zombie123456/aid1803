# exercise.py
def document():
    f=open('data.txt')
    while True:
        s=f.readline()
        l=s.split()
        try:
            print('姓名:',l[0],'电话:',l[1])
        except:
            break
    f.close()
document()









