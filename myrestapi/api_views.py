
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from myrestapi.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from myrestapi.models import *

class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class ProductList(ListAPIView):
    queryset = Productitems.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name','author')
    pagination_class = ProductsPagination

"""
    def get_queryset(self):
        quantity = self.request.query_params.get('quantity',0)
        if quantity is 0:
            return super().get_queryset()
        queryset = Productitems.objects.all()
        if quantity > 0 :
            return queryset.filter(
                quantity=0
            )

"""

class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <=0.0:
                raise ValidationError({'price':'Must be above Rs0.00'})
        except ValueError:
            raise  ValidationError({'price':'A valid number is required'})
        return super().create(request, *args, **kwargs)


class ProductDestroy(DestroyAPIView):
    queryset = Productitems.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data{}'.format(product_id))
        return response


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Productitems.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data{}'.format(product['id']),{
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
            })
        return response