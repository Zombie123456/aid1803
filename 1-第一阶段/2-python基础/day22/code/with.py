# with.py

# 此示例用来演示用with语句来打开和关闭文件
try:
    with open("text.txt") as f:
        while True:
            s = f.readline()
            if not s:
                break
            print(s)
            raise ValueError  # 故意制造错误进入异常状态
except IOError:
    print("打开文件失败!")
except:
    print("有其它异常发生,已经处理!")


# 用try-finally语句来处理异常,来关闭文件
# def read_line():
#     try:  # 此try语句用来捕获异常
#         f = open("text.txt")
#         try:  # 此try语句确保能关闭文件
#             while True:
#                 s = f.readline()
#                 if not s:
#                     return
#                 print(s)
#                 int(input("请输入继续打印下一行:"))  # 抛出异常
#         finally:
#             f.close()
#             print('已关闭')
#     except IOError:
#         print("文件打开失败")
#     except:
#         print("有其它异常发生,已经处理!")

# read_line()
