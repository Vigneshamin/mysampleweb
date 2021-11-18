from django.contrib import admin
from django.urls import path, include
import myrestapi.api_views

urlpatterns = [
    path('myrest/p1/products',myrestapi.api_views.ProductList.as_view()),
    path('myrest/p1/products/new',myrestapi.api_views.ProductCreate.as_view()),
    path('myrest/p1/products/<int:id>/destroy',myrestapi.api_views.ProductDestroy.as_view()),
    path('myrest/p1/products/all/<int:id>/', myrestapi.api_views.ProductRetrieveUpdateDestroy.as_view()),
]
