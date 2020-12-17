from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books',views.EbookViewSet)







urlpatterns = [

    path('',include(router.urls)),
    path('books/<slug:slug>/rate/',views.ReviewCreateAPIView.as_view()),
    path('books/<slug:slug>/rates/',views.ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/',views.ReviewRUDAPIView.as_view()),
]