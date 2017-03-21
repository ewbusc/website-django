from django.contrib import admin

from .forms import BlockForm

from core.models import Block

class BlockAdmin(admin.ModelAdmin):
    form = BlockForm

admin.site.register(Block, BlockAdmin)
