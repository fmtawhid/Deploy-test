from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(category)

class AdminBlog(admin.ModelAdmin):
    list_display=('title','category')

    list_filter=('title',)
    list_per_page= (10)
    search_fields = ('title',)

    prepopulated_fields = {"slug":['title']}
admin.site.register(blog, AdminBlog)
