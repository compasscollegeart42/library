# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import books, authors, translater, genre, public


# Register your models here.

@admin.register(books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'draft','get_image']
    list_display_links = ['title']
    readonly_fields = ('get_image',)
    search_fields = ('title', 'description')
    save_on_top = True
    list_editable = ('draft',)
    fieldsets = [
        (None, {
            'fields': (('title','get_image'),)
        }),
        (None, {
            'fields': (('authors','translater',),)
        }),
        (None, {
            'fields': ('public',)
        }),
        (None, {
            'fields': (('description',),)
        }),
        (None, {
            'fields': (('num_list','date_write','year_public','admission'),)
        }),
        (None, {
            'fields': ('genre',)
        }),
        (None, {
            'fields': (('files','image'),'url','draft')
        }),
    ]
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50"')
    get_image.short_description = "Обложка книги"
# admin.site.register(books, BooksAdmin)

@admin.register(authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
# admin.site.register(authors)
@admin.register(translater)
class TranslaterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
# admin.site.register(translater)
@admin.register(genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_display_links = ['title']
# admin.site.register(genre)

admin.site.register(public)

admin.site.site_header = 'Compass ADMIN'
admin.site.site_title = 'Compass ADMIN'