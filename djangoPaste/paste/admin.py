from django.contrib import admin
from paste.models import Paste
class PasteAdmin(admin.ModelAdmin):
	list_display = ['title','url']
	list_filter = ['published','created']
	search_fields = ['title','content']
	date_hierarchy = 'created'
	save_on_top = True
	
	
admin.site.register(Paste,PasteAdmin)
# Register your models here.
