from django.contrib import admin

from .models import Ad, Comment

# register 2 models Ad and Comment
admin.site.register(Ad)
admin.site.register(Comment)

