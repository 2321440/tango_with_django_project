from django.contrib import admin
from rango.models import Category, Page

#admin page display

class CategoryAdmin(admin.ModelAdmin):

	prepopulated_fields = {"slug":("name",)}
	fields = ["name","slug","views","likes",]
	list_display = ("name","views","likes","slug")

class PageAdmin(admin.ModelAdmin):
	list_display = ("title","category","url")



# Register your models here.

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
