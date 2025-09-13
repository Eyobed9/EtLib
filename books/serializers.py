from rest_framework import serializers 
from .models import Book, Borrow

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "user", "book", "borrowed_at", "returned_at"]
        read_only_fields = ["borrowed_at", "returned_at"]

    def create(self, validated_data):
        book = validated_data["book"]

        if book.copies_available <= 0:
            raise serializers.ValidationError({"error": "No copies available for this book."})

        # decrease available copies
        book.copies_available -= 1
        book.save()

        return super().create(validated_data)