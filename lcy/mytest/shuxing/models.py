from django.db import models

# Create your models here.

class Zhuangbei(models.Model):
    name = models.CharField(max_length=100)
    # shuxing = models.OneToOneField('Shuxing')
    z_type = models.IntegerField()

# class Shuxing(models.Model):
#     naili = models.CharField(max_length=20)
#     tili = models.CharField(max_length=20)
#     liliang = models.CharField(max_length=20)
#     zhili = models.CharField(max_length=20)


class Zb_type(models.Model):
    zbb_type = models.CharField(max_length=50)