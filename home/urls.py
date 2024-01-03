
from django.urls import path
from . views import Book,Purchase

urlpatterns = [
    path('book/',Book.as_view(),name=''),
    path('purchase/<int:pk>/',Purchase.as_view())

]
