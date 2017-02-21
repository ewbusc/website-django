from django.shortcuts import render

def home(request):
	return render(request, 'core/home.html', {})
	
def support(request):
	return render(request, 'core/support.html', {})

def events(request):
	return render(request, 'core/events.html', {})

def contact(request):
	return render(request, 'core/contact.html', {})
