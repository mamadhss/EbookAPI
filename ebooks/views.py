from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status,viewsets
from .permissions import IsAdminUserOrReadOnly,IsAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Ebook,Review
from .serializers import EbookSerializer,ReviewSerializer



class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        kwarg_slug = self.kwargs.get("slug")

        ebook = Ebook.objects.get(slug = kwarg_slug)

        if ebook.reviews.filter(review_author=self.request.user).exists():
            raise ValidationError("you already submitted your rates!")

        serializer.save(review_author=self.request.user,ebook=ebook)


class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Review.objects.filter(ebook__slug=kwarg_slug)


class ReviewRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

        


   





