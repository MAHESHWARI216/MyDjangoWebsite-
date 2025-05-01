from django.contrib import admin

from .models import BlogPost, Contact, Category


admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(Category)

# Register your models here.
