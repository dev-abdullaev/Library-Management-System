from django.contrib import admin
from library.models import Book, BookIssue, BookReturn  # Reader

from .models import User

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookIssue)
# admin.site.register(Reader)
admin.site.register(BookReturn)
