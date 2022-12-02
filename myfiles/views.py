from django.shortcuts import render
from myfiles.models import Project,Banner

# Create your views here.
def home(malumot):
	ishlar = Project.objects.all().order_by('-id')[:3]
	banner = Banner.objects.all()
	return render(malumot,'index.html',{'project':ishlar,'banner':banner})


def project(malumot):
	ishlar = Project.objects.all().order_by('-id')
	return render(malumot, 'project.html',{'project':ishlar})