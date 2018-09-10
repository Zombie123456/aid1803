from django.db import models

# Create your models here.
class Teachers(models.Model):
    tname = models.CharField(max_length=20,verbose_name='教师姓名')
    tphone = models.CharField(max_length=20, verbose_name='电话号码')
    tpwd = models.CharField(max_length=20, verbose_name='密码')
    temail = models.EmailField(verbose_name='电子邮件')
    isActive = models.BooleanField(default=True, verbose_name='在职')
    thead = models.ImageField(
        upload_to='static/upload/thead', verbose_name='教师头像')
    def __str__(self):
        return self.tname

    class Meta:
        verbose_name_plural = '教师'


class Students(models.Model):
    sname = models.CharField(max_length=20,verbose_name='学生姓名')
    snum = models.CharField(max_length=20, verbose_name='学号')
    spwd = models.CharField(max_length=20, verbose_name='密码')
    shead = models.ImageField(
        upload_to='static/upload/shead', verbose_name='学生头像')
    isActive = models.BooleanField(default=True, verbose_name='在读')
    def __str__(self):
        return self.sname
    
    class Meta:
        verbose_name_plural = '学生'


class Subjects(models.Model):
    subject = models.CharField(max_length=20,verbose_name='课程名称')
    score = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='学生成绩')
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name_plural = '学科'

class Classes(models.Model):
    sclass = models.CharField(max_length=10,verbose_name='班')
    grade = models.CharField(max_length=10,verbose_name='年级')
    def __str__(self):
        return self.sclass

    class Meta:
        verbose_name_plural = '年级'
