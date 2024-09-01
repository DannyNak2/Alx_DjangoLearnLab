from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly  # Import your custom permission
from .models import Book
from .serializers import BookSerializer

# BookList view using generics.ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  # Apply permissions

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  # Apply permissions