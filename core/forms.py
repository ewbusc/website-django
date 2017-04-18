from django import forms
from ckeditor.widgets import CKEditorWidget

from core.models import Block

# To be used on the staff user interface, where the names of blocks should not be changed
class FrontendBlockForm(forms.ModelForm): 
    class Meta:
        model = Block
        fields = '__all__'
        widgets = {'name': forms.HiddenInput()}

# To be used in Django admin interface, where we want to be able to modify blocks' names or
# to create new ones.
class BackendBlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'