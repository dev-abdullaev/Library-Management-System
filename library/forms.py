from django import forms
from django.forms import fields

from .models import Book, BookIssue, BookReturn


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "book_name",
            "author_name",
            "isbn",
            "category",
            "quantity",
            "description",
            "cover",
        ]


# class BookIssueForm(forms.ModelForm):
#     class Meta:
#         model = BookIssue
#         fields = ["reader", "book"]


# class BookReturnForm(forms.ModelForm):
#     class Meta:
#         model = BookReturn
#         fields = ["reader", "book", "return_date"]
