from django.contrib import admin

from .models import BlogPost, Contact, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('title', 'content', 'category', 'image', 'video')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Contact)
admin.site.register(Category)




# Register your models here.
