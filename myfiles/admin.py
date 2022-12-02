from django.contrib import admin
from myfiles.models import Project,Banner
# Register your models here.

class project(admin.ModelAdmin):
    list_display = ['id','link','rasim','nomi','tafsiya']

admin.site.register(Project,project)

class banner(admin.ModelAdmin):
    list_display=['id','rasim']

admin.site.register(Banner,banner)