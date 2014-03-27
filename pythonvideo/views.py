#coding:utf-8

from django.template import Template,Context
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *
def dump_item(cls,name):
	temp	= {}
	count	= 0
	for n in cls:
		temp[name+str(count)] = n
		count +=1
	return temp

def home(request):
	d	= {}
	cates	= Category.objects.all().order_by('-id')[:4]
	courses	= Course.objects.all().order_by('-id')[:4]
	videos	= Video.objects.all().order_by('-id')[:4]
	#d.update(dump_item(cates,'cates'))
	d['cates']=cates
	d['courses']=courses
	d['videos']=videos
        alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image





	return render_to_response('home_tag.html',d,context_instance=RequestContext(request))
def cates(request):
	d	= {}
	cates	= Category.objects.all().order_by('-id')
	
	d['cates']=cates
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('cates_tag.html',d,context_instance=RequestContext(request))
				
def courses(request):
	d	= {}
	if 'cateid' in request.GET:
		courses = Course.objects.filter(cateid=request.GET['cateid']).order_by('-id')
	else:
		courses	= Course.objects.all().order_by('-id')
	
	d['courses']=courses
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('courses_tag.html',d,context_instance=RequestContext(request))
def videos(request):
	d	= {}
	p = 0
	if 'page' in request.GET:
		p = int(request.GET['page'])-1
	if 'vid' in request.GET:
		videos	= Video.objects.filter(cateid=request.GET['vid']).order_by('-id')
	else:
		videos  = Video.objects.all().order_by('id')
	print len(videos)
	videos = list(videos)[p * 9: (p+1) * 9]

	d['videos']=videos
	print len(videos)
	d['page_next'] = p+2
	return render_to_response('videos_tag.html',d,context_instance=RequestContext(request))

def video(request,id):
	d	= {}

	videos	= Video.objects.filter(courseid=id)
	
	d['videos']	=videos
		

	d['courses']	= Course.objects.get(id=id)
	if 'vid' in request.GET:
		d['vid'] = Video.objects.get(id=request.GET['vid'])
		d['vid'].count+=1
		d['vid'].save()
	else:
		if videos:
			d['vid'] = list(videos)[0]
 	alltext = TextInfo.objects.all()
        allimg = ImgInfo.objects.all()
        for text in alltext:
		d[text.tagname]        = text.text
        for img in allimg:
		d[img.tagname]        = img.image
	
	return render_to_response('video_tag.html',d,context_instance=RequestContext(request))
	
def showpage(request,id):
    d = {}
    alltext = TextInfo.objects.all()
    allimg  = ImgInfo.objects.all()

    for text in alltext:
        d[text.tagname]       = text.text
    for img in allimg:
        d[img.tagname]        = img.image
 
    start = int(id)-2
    if start < 0:
	start = 0
    d['pages'] = Singlepage.objects.filter()[start:int(id)+2]
    try:
    	d['page'] = Singlepage.objects.get(id=id)
    except:
	d['page'] = 'Page Not Found'

    return render_to_response('show-single.html',d,context_instance=RequestContext(request))
			
				




	
