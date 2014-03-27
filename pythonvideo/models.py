#coding=utf-8
from django.db import models


class Category(models.Model):
	image	   = models.ImageField(upload_to='./image',default="default.jpg")
	icon	   = models.CharField(max_length=64)
	count      = models.IntegerField(default=0)
	title      = models.CharField(max_length=256)
	intro      = models.CharField(max_length=1024)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="kw")
	createdate = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
class Course(models.Model):
	title      = models.CharField( max_length=256)
	count      = models.IntegerField(default=0)
	intro      = models.CharField( max_length=1024)
	image	   = models.ImageField(upload_to='./image',default="default.jpg")
	cateid     = models.ForeignKey(Category)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="kw")
	def __unicode__(self):
		return self.title

class Video(models.Model):
	title      = models.CharField( max_length=256)
	url	   = models.CharField( max_length=4096)
	count      = models.IntegerField(default=0)
	content    = models.TextField()
	intro      = models.CharField( max_length=1024)
	image	   = models.ImageField(upload_to='./image',default="default.jpg")
	courseid   = models.ForeignKey(Course)
	createdate = models.DateField(auto_now=True)
	order      = models.IntegerField(default=0)
	kw	   = models.CharField(max_length=64,default="kw")

class Singlepage(models.Model):
    title         = models.CharField(max_length=1024)
    content       = models.TextField()
    image         = models.ImageField(upload_to='./image',default='page.png')
    order         = models.IntegerField(default=0)
    count         = models.IntegerField(default=0)
    kw            = models.CharField(max_length=64,default='open')



class TextInfo(models.Model):
    text       = models.TextField()
    tagname    = models.CharField(max_length=64)


class ImgInfo(models.Model):
    image      = models.ImageField(upload_to='./image')
    tagname    = models.CharField(max_length=64)
    def image_tag(self):
    	return u'<img src="/%s" />' % self.image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
