from django.contrib import admin
from django.forms import ModelForm
from portal.models import *

class TutorialForm(admin.ModelAdmin):
	class Media:
		js = ('/statis/tinymce/jscripts/tiny_mce/tiny_mce.js','/statis/tinymce/jscripts/tiny_mce/text_area.js',)

admin.site.register(Comment)
admin.site.register(Tutorial, TutorialForm)
admin.site.register(Blogrol)
admin.site.register(Categories)
