from django.contrib import admin
from .models import *

class TeachersAdmin(admin.ModelAdmin):
    list_display = ['tname','tphone','isActive','temail']
    list_display_links = ['tname']
    list_editable = ['isActive']

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['sname','snum','isActive']
    list_display_links = ['sname']
    list_editable = ['isActive']

class ClassesAdmin(admin.ModelAdmin):
    list_display  = ['sclass','grade']
    list_display_links = ['sclass']

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['subject','score']
# Register your models here.
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Classes)
admin.site.register(Subjects)