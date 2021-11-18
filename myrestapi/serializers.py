from rest_framework import serializers
from myrestapi.models import Productitems

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productitems
        fields = ['id','name','author','description','quantity','price','photo']


