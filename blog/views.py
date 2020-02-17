from django.shortcuts import render
from .models import Post

'''
posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post boys',
		'date_posted': 'Ogos 27, 2019'
	},
	{
		'author': 'Zahir',
		'title': 'Blog Post 2',
		'content': 'Second post na boys',
		'date_posted': 'Ogos 29, 2019'
	}
]
'''

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})