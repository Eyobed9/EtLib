from django.urls import path
from .views import BookListCreateView, BookDetailView, BorrowBookView, ReturnBookView, MyBorrowedBooksView, AllBorrowedBooksView

urlpatterns = [
    path("", BookListCreateView.as_view(), name="book-list-create"),
    path("<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("checkout/", BorrowBookView.as_view(), name="book-checkout"),
    path("return/<int:pk>/", ReturnBookView.as_view(), name="book-return"),
    path("my-borrows/", MyBorrowedBooksView.as_view(), name="my-borrows"),
    path("all-borrows/", AllBorrowedBooksView.as_view(), name="all-borrows"),
]
