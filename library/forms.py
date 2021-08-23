from django import forms

from .models import Book, Category


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


class CategoryForm(forms.ModelForm):
    category = forms.ChoiceField(choices=("", "-----"))

    class Meta:
        model = Category
        fields = ["title"]

