from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.forms.models import ModelMultipleChoiceField
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import BookModelForm, CategoryForm
from .models import Book, BookIssue, Category


@login_required
def admin_view(request):
    book = Book.objects.all().count()
    book_issue = BookIssue.objects.all().count()

    context = {"book": book, "book_issue": book_issue}
    return render(request, "admin/admin.html", context)


class AdminAddedBookListView(ListView):
    model = Book
    template_name = "admin/added_books.html"
    context_object_name = "added_books"


class AdminBookIssueListView(LoginRequiredMixin, ListView):
    model = BookIssue
    template_name = "admin/admin_book_issue.html"
    context_object_name = "admin_book_issue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        admin_book_issue = BookIssue.objects.all()
        context["admin_book_issue"] = admin_book_issue
        return context


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = "books"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "book/book_create.html"
    form_class = BookModelForm
    success_url = reverse_lazy("home")


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "book/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "book/book_update.html"
    form_class = BookModelForm


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book/book_delete.html"
    success_url = reverse_lazy("home")


@login_required
def bookIssueView(request, slug):
    book = get_object_or_404(Book, slug=slug)
    issue_date = book.issue_date
    charge_amount = book.charge_amount
    return_date = book.issue_date + timedelta(days=30)
    quantity = book.quantity
    book_issue = BookIssue.objects.create(
        issue_date=issue_date,
        book=book,
        user=request.user,
        quantity=quantity,
        charge_amount=charge_amount,
        return_date=return_date,
    )
    book = book_issue
    return redirect("book_issue_list")


class BookIssueListView(LoginRequiredMixin, ListView):
    model = BookIssue
    template_name = "book/book_issue.html"
    context_object_name = "book_issue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_issue = BookIssue.objects.filter(user=self.request.user)
        context["book_issue"] = book_issue
        return context


@login_required
def bookReturnView(request, slug):
    book_issue = get_object_or_404(BookIssue, slug=slug)
    book = book_issue
    if request.method == "POST":
        try:
            book.delete()
            return redirect("book_issue_list")
        except AttributeError:
            return redirect("book_issue_list")
    context = {"book": book}
    return render(request, "book/book_return.html", context)


class BookSearchView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "book/book_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(book_name__icontains=query) | Q(isbn__icontains=query)
        ).distinct()


class BookIssueSearchView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "book/book_issue_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return BookIssue.objects.filter(
            Q(book__book_name__icontains=query)
            | Q(book__isbn__icontains=query)
            | Q(user__id_number__icontains=query)
        ).distinct()


class CategoryListView(ListView):
    model = Category
    template_name = "category/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "category/category_create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "category/category_detail.html"
    context_object_name = "category"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "category/category_update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("admin_page")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = reverse_lazy("admin_page")
