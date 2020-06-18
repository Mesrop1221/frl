from django.contrib import admin
from .models import Group,Post,Links,Type
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

admin.site.site_header = 'Girls Consultant'
class PostAdminForm(forms.ModelForm):
     
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display =('title','date',)
    list_display_links = ('title','date',)
    list_filter = ('group','date',)
    search_fields = ('title',)

admin.site.register(Group)
admin.site.register(Type)

@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_name','url',)
    list_display_links = ('link_name','url',)
