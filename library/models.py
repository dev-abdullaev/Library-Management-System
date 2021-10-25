from datetime import date, datetime, timedelta

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
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
    return_date = models.DateField(default=30)
    charge_amount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.book_name}"


class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=30)
    quantity = models.IntegerField(default=0)
    charge_amount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return str(self.book)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.book.book_name)
            self.book.quantity = self.book.quantity - 1
            self.book.save()
        else:
            self.book.quantity = self.book.quantity + 1
            self.book.save()
        super(BookIssue, self).save(*args, **kwargs)

        # def save(self, *args, **kwargs):
        #     if self.pk:
        #     raise StandardError('Can\'t modify bla bla bla.')
        # super(Payment, self).save(*args, **kwargs)

        # Need to ipmlement this login in save method
        # I tried but did not work
        # date.today() >= self.book.return_date:
        # overdue_days = (date.today() - self.book.return_date).days
        # charge_rate = int(1.50)  ###  $1.50 per day
        # self.charge_amount = charge_rate * overdue_days


class BookReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_issue = models.ForeignKey(BookIssue, on_delete=models.CASCADE)
    return_date = models.DateField(default=30)
    charge_amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.book_issue)

