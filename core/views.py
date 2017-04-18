from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.middleware import csrf

from .forms import FrontendBlockForm
from core.models import Block

# Given a list of names of Block objects, builds a dictionary of format {block_name: block_object}
def block_dict(block_names):
    blocks = {}
    for name in block_names:
        blocks[name] = get_object_or_404(Block, name=name)
    return blocks

### DO NOT INSTANTIATE. THIS WILL CRASH. 
###                     Make a child class that inherits from this and overrides self.names and self.template
###                     See below (HomeView, etc.) for examples.
class PublicViewWithBlocks(View):
    blocks = {}

    def __init__(self):
        self.blocks = block_dict(self.names)

    def get(self, request):
        context = {name: block.content for (name, block) in self.blocks.items()}
        return render(request, self.template, context)

### DO NOT INSTANTIATE. THIS WILL CRASH. 
###                     Make a child class that inherits from this and overrides self.names and self.template
###                     See below (HomeEditView, etc.) for examples.
class EditView(View):
    blocks = {}

    editBtn = '<a class="btn btn-default" href="{}?editor={}" role="button">Edit</a>'
    formBody = '''
        <form method="post">
            {}
            {}
            <input type="submit"\>
            <input type="hidden" name="csrfmiddlewaretoken" value="{}" />
        </form>
    '''

    def __init__(self):
        self.blocks = block_dict(self.names)

    # Creates a context to populate the page. We loop through all blocks and store
    # either the content of the block with an edit button or a FrontendBlockForm
    # so that the user can edit it. 
    # NOTE: We should only ever display one FrontendBlockForm on a page at a time.
    #       Django-ckeditor has a bug that prevents rendering more than one using
    #       this approach.
    def get(self, request):
        blockToEdit = request.GET.get('editor', 'DefaultValue')
        context = {}
        for (name, block) in self.blocks.items():
            if blockToEdit == name:
                token = csrf.get_token(request)
                form = FrontendBlockForm(instance=block)
                context[name] = self.formBody.format(form.media, form.as_p(), token)
            else:
                context[name] = block.content + self.editBtn.format(request.path, name)
        return render(request, self.template, context)

    # Reads a form from the post and tries to update the corresponding block 
    # in the database with the contents of the form. Redirects to the same page
    # without '?editor=value' on the URL.
    def post(self, request):
        # create a form instance and populate it with data from the request:
        data = request.POST.copy()
        form = FrontendBlockForm(request.POST, instance=self.blocks[data['name']])
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.path)

############################################
# Block related views for specific classes
############################################

class Home:
    names = ['home_left', 'home_right']
    template = 'core/home.html'
class HomeView(PublicViewWithBlocks, Home):
    pass
class EditHomeView(EditView, Home):
    pass

class Support:
    names = []
    template = 'core/support.html'
class SupportView(PublicViewWithBlocks, Support):
    pass
class EditSupportView(EditView, Support):
    pass

class Events:
    names = ['events_right']
    template = 'core/events.html'
class EventsView(PublicViewWithBlocks, Events):
    pass
class EditEventsView(EditView, Events):
    pass
    
class Projects:
    names = ['projects_main']
    template = 'core/projects.html'
class ProjectsView(PublicViewWithBlocks, Projects):
    pass
class EditProjectsView(EditView, Projects):
    pass

# No edit view, currently unneeded
class Contact:
    names = ['support_contribute', 'support_partners_sponsors']
    template = 'core/contact.html'
class ContactView(PublicViewWithBlocks, Contact):
    pass
