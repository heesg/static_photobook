from django.contrib import admin
from .models import Photo,Comment
# Register your models here.

class PhotoModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Photo , PhotoModelAdmin)
admin.site.register(Comment)