# filewrite.py
class FileWrite:
    def __init__(self, filename):
        self.filename = filename  # 此属性用于记住文件名

    def writeline(self, s):
        '''此方法用于向文件中写入字符串'''
        self.file.write(s + '\n')

    def __enter__(self):
        '''此方法用于实现环境管理器'''
        self.file = open(self.filename, 'w')
        print('已进入__enter__方法,文件打开成功')
        return self  # 返回值用于with中的as绑定

    def __exit__(self, exec_type, exec_value, exec_tb):
        '''exec_type为异常类型,无异常时为None
           exet_value为错误的对象,无异常时为None
           exec_tb为错误的tranceback对象
        '''
        self.file.close()
        print('文件', self.filename, '已关闭')
        if exec_type is None:
            print('无异常')
        else:
            print('发生异常,类型是', exec_type, '错误是:', exec_value)
        print('__exit__方法被调用,已离开with语句')


try:
    with FileWrite('log.txt') as fw:
        while True:
            s = input('输入一行:')
            if s == 'exit':
                break
            if s == 'error':
                raise ValueError('故意制造的值错误')
            fw.writeline(s)
except:
    print('有错误发生,已正常')
print('这是with语句之外,也是程序的最后一行语句')
