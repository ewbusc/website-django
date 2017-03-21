from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import BlockForm
from core.models import Block

def home(request):
        block = get_object_or_404(Block, id=1)
        contentBlock = block.content
        return render(request, 'core/home.html', {'contentBlock': contentBlock})

# source: https://docs.djangoproject.com/en/1.10/topics/forms/
def edit_home(request):
    block = get_object_or_404(Block, id=1)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        ## Temporary code: get a specific Block to edit.
        # create a form instance and populate it with data from the request:
        form = BlockForm(request.POST, instance=block)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlockForm(instance=block)

    return render(request, 'core/home_editor.html', {'form': form})

def support(request):
	return render(request, 'core/support.html', {})

def events(request):
	return render(request, 'core/events.html', {})

def contact(request):
	return render(request, 'core/contact.html', {})
	
def projects(request):
	return render(request, 'core/projects.html', {})

