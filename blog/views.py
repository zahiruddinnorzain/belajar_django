from django.shortcuts import render
from .models import Post

from .forms import NameForm, ContactForm
from django.core.mail import send_mail

def get_contact(request):
    # if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['info@example.com']
			if cc_myself:
				recipients.append(sender)

		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()

	return render(request, 'blog/name.html', {'form': form})
	
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'blog/name.html', {'form': form})


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