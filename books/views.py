from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Book, Borrow
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