# 练习:
# 1创建文件夹myfiles
mkdir myfiles
#2在myfiles文件夹中创建文件:
#    a.mp3 ab.txt ac.mp3 abc.txt aabb.mp3
#    bc.txt cd.mp3
touch a.mp3 ab.txt ac.mp3 abc.txt aabb.mp3
    bc.txt cd.mp3
#  3列出所有以.MP3结束的文件
ls *.mp3
#  4删除.之前只有一个字符的文件
rm ?.*
#  5列出含有c这个字符的文件
ls *c*
 # 6删除myfiles文件内的所有mp3文件
rm *.mp3



# 练习:
#  1查找gzip和tar这两个文件在什么位置
find / -name "gzip"
find / -name "tar"
#  2查找/etc文件夹下的那些文件里含有'tarena'这个内容
cd /etc
grep "tarena" -nr /etc
#  3将/etc/group文件复制到当前文件夹
cd ~/aid1803/linux/day02
cp /etc/group .
#  4将/etc/passwd文件复制到当前文件夹并改名为:'系统账户管理配置文件.txt'
cp /etc/passwd 系统账户管理配置文件.txt

# 练习:
#  写一个test.py文件,此文本写入python三条打印语句,
# 打印如下:
#  这是我的python第一条语句
# 我现在开始学Python了
# 这是最后一条语句
# 要求:
#  用2种方式执行语句
# 1.1)Python3 test.py
#   2)./test.py
# 2.将这三条语句输出重定向到myprint.txt中
./test.py > myprint.txt


























