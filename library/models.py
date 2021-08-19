from datetime import datetime, timedelta

from django.db import models
from django.urls import reverse
from users.models import User

CATEGORY = (
    ("Sci-Fi", "Sci-Fi"),
    ("Programming", "Programming"),
    ("Thriller", "Thriller"),
    ("Science", "Science"),
    ("Business", "Business"),
    ("History", "History"),
    ("Literature", "Literature"),
    ("Detective and Mystery", "Detective and Mystery"),
)


def get_expiry_date():
    return datetime.today() + timedelta(days=30)


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, unique=True)
    category = models.CharField(choices=CATEGORY, max_length=30)
    description = models.TextField()
    cover = models.ImageField(upload_to="book_cover/")
    quantity = models.IntegerField(default=0)
    issue_date = models.DateField(auto_now_add=True, null=True)
    return_date = models.DateField(default=get_expiry_date, null=True)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.book_name}"


class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=get_expiry_date)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.book)

    def save(self, *args, **kwargs):
        if not self.pk:  # only for creating not for update:
            self.book.quantity = self.book.quantity - 1
            self.book.save()
        super().save(*args, **kwargs)


class BookReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_issue = models.ForeignKey(BookIssue, on_delete=models.CASCADE)
    return_date = models.DateField(default=get_expiry_date)

    def __str__(self):
        return str(self.book_issue)

