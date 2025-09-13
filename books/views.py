from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from .models import Book, Borrow
from rest_framework.response import Response
from django.utils import timezone
from .serializers import BookSerializer, BorrowSerializer
from .permissions import IsLibrarianOrReadOnly

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated & IsLibrarianOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated & IsLibrarianOrReadOnly]

class BorrowBookView(generics.CreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # attach logged-in user automatically
        serializer.save(user=self.request.user)


class BorrowBookView(generics.CreateAPIView):
    """Checkout a book"""
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReturnBookView(generics.UpdateAPIView):
    """Return a borrowed book"""
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        borrow = self.get_object()

        # Ensure only the user who borrowed OR librarian can return
        if borrow.user != request.user and getattr(request.user, "role", "").lower() != "librarian":
            return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)

        if borrow.returned_at is not None:
            return Response({"error": "Book already returned"}, status=status.HTTP_400_BAD_REQUEST)

        # mark as returned
        borrow.returned_at = timezone.now()
        borrow.save()

        # increase available copies
        borrow.book.copies_available += 1
        borrow.book.save()

        return Response(BorrowSerializer(borrow).data, status=status.HTTP_200_OK)


class MyBorrowedBooksView(generics.ListAPIView):
    """View my borrowed books"""
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)


class AllBorrowedBooksView(generics.ListAPIView):
    """Librarian view: all borrow records"""
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only librarians can see all records
        if getattr(self.request.user, "role", "").lower() == "librarian":
            return Borrow.objects.all()
        return Borrow.objects.none()
