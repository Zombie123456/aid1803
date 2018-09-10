from django.db import models

# Create your models here.

# 1. Users - 用户表
class UserInfo(models.Model):
    uphone = models.CharField(max_length=20, verbose_name='电话号码')
    upwd = models.CharField(max_length=128, verbose_name='密码')
    uemail = models.EmailField(verbose_name='电子邮件',null=True)
    uname = models.CharField(max_length=50, verbose_name='用户名')
    utime = models.TimeField(verbose_name='注册时间')
    isban = models.BooleanField(default=False,verbose_name='是否禁用')
    isdelete = models.BooleanField(default=True, verbose_name='是否删除')

    def __str__(self):
        return self.uname

    class Meta:
        # db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

# 2.GoodsType - 商品类型表
class GoodsType(models.Model):
    title = models.CharField(max_length=30, verbose_name='类型标题')
    desc = models.TextField(verbose_name='描述')
    picture = models.ImageField(
        upload_to='static/upload/goodstype', verbose_name='图片')
    isdelete = models.BooleanField(default=True,verbose_name='是否删除')

    def __str__(self):
        return self.title

    class Meta:
        # db_table = 'goodstype'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


# 3.Goods - 商品表(商品分类)
class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='商品名称')
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='商品价格')
    desc = models.CharField(max_length=100,verbose_name='商品描述')
    spec = models.CharField(max_length=30, verbose_name='商品规格')
    picture = models.ImageField(
        upload_to='static/upload/goods', verbose_name='商品图片')
    detail = models.CharField(max_length=100,verbose_name='商品详情')
    isActive = models.BooleanField(default=True, verbose_name='是否上架')

    def __str__(self):
        return self.title

    class Meta:
        # db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

# 4.carts购物车表(用户,商品)
class CartInfo(models.Model):
    ccount = models.IntegerField(verbose_name='商品数量')

# 5.地址表(用户)
class Address(models.Model):
    ads = models.CharField(max_length=100, verbose_name='收货地址')
    aname = models.CharField(max_length=20, verbose_name='收货人')
    aphone = models.CharField(max_length=20, verbose_name='收货号码')

# 6.订单表(用户)
class Order(models.Model):
    orderid = models.CharField(max_length=15, verbose_name='订单号')
    # 商品,数量,单价,描述
    orderdetail = models.CharField(max_length=100, verbose_name='商品描述')
    adname = models.CharField(max_length=20, verbose_name='收货人')
    adsphone = models.CharField(max_length=20, verbose_name='收货号码')
    ads = models.CharField(max_length=100, verbose_name='收货地址')
    time = models.TimeField(verbose_name='下单时间')
    acot = models.IntegerField(verbose_name='商品总数')
    acount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='商品总价')
    orderstatus = models.BooleanField(default=True, verbose_name='订单状态')

