from django.contrib import admin
from .models import News, Contact, CommentNew


admin.site.register(News)
admin.site.register(Contact)
admin.site.register(CommentNew)