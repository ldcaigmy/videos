#coding=utf-8
from django.contrib import admin 
from .models import Category,Course,Video,TextInfo,ImgInfo,Singlepage

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title',)
class CourseAdmin(admin.ModelAdmin):
	list_display=('title',)
class VideoAdmin(admin.ModelAdmin):
	list_display=('title',)
class TextInfoAdmin(admin.ModelAdmin):
    list_display =('text','tagname',)

class ImgInfoAdmin(admin.ModelAdmin):
    list_display =('image_tag','tagname',)
class SinglepageAdmin(admin.ModelAdmin):
    list_display =('title',)
    class Media:
	js=("/static/game/js/jquery.min.js","/static/ckeditor.js","/static/adapters/jquery.js","/static/game/js/edit.js",)
admin.site.register(Course,CourseAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(TextInfo,TextInfoAdmin)
admin.site.register(ImgInfo,ImgInfoAdmin)
admin.site.register(Singlepage,SinglepageAdmin)
