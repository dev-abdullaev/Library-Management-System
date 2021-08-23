from django.contrib import admin
from library.models import Book, BookIssue, BookReturn, Category  # Reader

from .models import User

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookIssue)
admin.site.register(Category)
admin.site.register(BookReturn)


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_name", "slug")
    prepopulated_fields = {"slug": ("slug",)}


class BookIssueAdmin(admin.ModelAdmin):
    list_display = ("book", "slug")
    prepopulated_fields = {"slug": ("slug",)}
