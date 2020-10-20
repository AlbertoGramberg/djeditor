
from django.contrib import admin

from .models import (
    Blog,
    Tag,
)

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
   list_display = (
       'title',
       'author',
   )
   search_fields = ('title',)
   #solo si hay many to many
   filter_horizontal = ('tag',)

admin.site.register(Tag)
