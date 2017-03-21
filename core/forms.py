from django import forms
from ckeditor.widgets import CKEditorWidget

from core.models import Block

class BlockForm(forms.ModelForm): 
    class Meta:
        model = Block
        fields = '__all__'
