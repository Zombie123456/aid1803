from django.contrib import admin
from .models import *

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'picture', 'desc']
    list_display_links = ['title']
    list_editable = ['picture', 'desc']

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title','price', 'spec', 'isActive']
    list_display_links = ['title']
    list_editable = ['price', 'spec', 'isActive']

class UserAdmin(admin.ModelAdmin):
    list_display = ['uname', 'uphone', 'uemail', 'isActive']
    list_display_links = ['uname']
    list_editable = ['isActive']

# Register your models here.
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(UserInfo, UserAdmin)
admin.site.register(CartInfo)
admin.site.register(Order)
admin.site.register(Address)
