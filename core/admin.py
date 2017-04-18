from django.contrib import admin

from .forms import BackendBlockForm

from core.models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = BackendBlockForm

admin.site.register(Block, BlockAdmin)
