from django.urls import path

from .views import (
    AdminAddedBookListView,
    AdminBookIssueListView,
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookIssueListView,
    BookIssueSearchView,
    BookListView,
    BookSearchView,
    BookUpdateView,
    admin_view,
    bookIssueView,
    bookReturnView,
)

urlpatterns = [
    #####---------------------------Admin Related Urls ----------------------------------
    path("", BookListView.as_view(), name="home"),
    path("admin-dashboard/", admin_view, name="admin_page"),
    path("admin-added-books/", AdminAddedBookListView.as_view(), name="admin_added_books"),
    path("admin-book-issue/", AdminBookIssueListView.as_view(), name="admin_book_issue"),
    #####------------------------------User Related Urls ----------------------------------
    #####---------------------------------- -----------------------------------------------
    path("book-create/", BookCreateView.as_view(), name="book_create"),
    path("book-detail/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book-return/<int:pk>/", bookReturnView, name="book_return"),
    path("book-update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("book-delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
    path("book-issue/<int:id>/", bookIssueView, name="book_issue"),
    path("book-issue-list/", BookIssueListView.as_view(), name="book_issue_list"),
    path("book-search-result/", BookSearchView.as_view(), name="book_search_results"),
    path(
        "book-issue-search-result/", BookIssueSearchView.as_view(), name="book_issue_search_results"
    ),
]
