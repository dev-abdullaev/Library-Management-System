from django.urls import path

from .views import AdminAddedBookListView  # bookReturnView,
from .views import (
    AdminBookIssueListView,
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookIssueListView,
    BookIssueSearchView,
    BookListView,
    BookSearchView,
    BookUpdateView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
    admin_view,
    bookIssueView,
    bookReturnView,
)

urlpatterns = [
    #####----------------------------------------------------------------------------------
    #####---------------------------Admin Urls --------------------------------------------
    #####----------------------------------------------------------------------------------
    path("", BookListView.as_view(), name="home"),
    path("admin-dashboard/", admin_view, name="admin_page"),
    path("admin-added-books/", AdminAddedBookListView.as_view(), name="admin_added_books"),
    path("admin-book-issue/", AdminBookIssueListView.as_view(), name="admin_book_issue"),
    #####----------------------------------------------------------------------------------
    #####------------------------------User Urls ------------------------------------------
    #####---------------------------------- -----------------------------------------------
    path("book-create/", BookCreateView.as_view(), name="book_create"),
    path("book-detail/<slug:slug>/", BookDetailView.as_view(), name="book_detail"),
    path("book-return/<slug:slug>/", bookReturnView, name="book_return"),
    path("book-update/<slug:slug>/", BookUpdateView.as_view(), name="book_update"),
    path("book-delete/<slug:slug>/", BookDeleteView.as_view(), name="book_delete"),
    path("book-issue/<slug:slug>/", bookIssueView, name="book_issue"),
    path("book-issue-list/", BookIssueListView.as_view(), name="book_issue_list"),
    path("book-search-result/", BookSearchView.as_view(), name="book_search_results"),
    path(
        "book-issue-search-result/", BookIssueSearchView.as_view(), name="book_issue_search_results"
    ),
    #####----------------------------------------------------------------------------------
    #####------------------------------Category Urls---------------------------------------
    #####---------------------------------- -----------------------------------------------
    path("category-list/", CategoryListView.as_view(), name="category_list"),
    path("category-create/", CategoryCreateView.as_view(), name="category_create"),
    path("category-detail/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category-update/<slug:slug>/", CategoryUpdateView.as_view(), name="category_update"),
    path("category-delete/<slug:slug/", CategoryDeleteView.as_view(), name="category_delete"),
]
