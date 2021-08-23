from datetime import date, datetime, timedelta

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from users.models import User


def get_expiry_date():
    return date.today() + timedelta(days=30)


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # this line below give to the instance slug field a slug name
        self.slug = slugify(self.title)
        # this line below save every fields of the model instance
        super(Category, self).save(*args, **kwargs)


class Book(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="books"
    )
    book_name = models.CharField(max_length=50, unique=True)
    author_name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to="book_cover/")
    quantity = models.IntegerField(default=100000)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=get_expiry_date)
    charge_amount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.book_name}"

    def save(self, *args, **kwargs):
        # this line below give to the instance slug field a slug name
        self.slug = slugify(self.book_name)
        # this line below save every fields of the model instance
        super(Book, self).save(*args, **kwargs)


class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=get_expiry_date)
    quantity = models.IntegerField(default=0)
    charge_amount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return str(self.book)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.book.quantity = self.book.quantity - 1
            self.slug = slugify(self.book.book_name)
            self.book.save()
        super(BookIssue, self).save(*args, **kwargs)


class BookReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_issue = models.ForeignKey(BookIssue, on_delete=models.CASCADE)
    return_date = models.DateField(default=get_expiry_date)
    charge_amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.book_issue)
