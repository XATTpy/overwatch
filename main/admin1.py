from django.contrib import admin
from .models import Hero, Video, Comment

class эщкере:
    model = Comment
    readonly_fields = ['Comment_likes']
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_filter = ['Video_date']
    readonly_fields = ['Video_likes']

admin.site.register(Hero)
admin.site.register(Video, VideoAdmin)

# Register your models here.
