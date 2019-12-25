from django.shortcuts import render,redirect
from app1.models import Post, Picture, Comment
from django.forms import modelformset_factory

def view1(request):
	eg=modelformset_factory(Post, fields=('title','author')) #extra=4, then it will input data till 4 items
	if request.method=='POST':
		form=eg(request.POST)
		instances=form.save()
	form=eg
	return render(request, 'app1/index.html', {'form':form})