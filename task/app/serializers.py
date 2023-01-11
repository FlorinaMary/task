from rest_framework import serializers
from .models import Product

class proserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'category','price', 'desc']