from django.contrib import admin
from .models import Feedback


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'comment', 'latitude', 'longitude')


admin.site.register(Feedback, PostAdmin)
