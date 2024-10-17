from rest_framework import serializers
from .models import Customer,Product,Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','description', 'price')
class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'customer', 'products', 'total_amount')