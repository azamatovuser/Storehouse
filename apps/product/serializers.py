from rest_framework import serializers
from .models import Place, Category, Product, Storehouse
from apps.account.serializers import AccountUpdateSerializer


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'is_active')


class StorehouseSerializer(serializers.ModelSerializer):
    account = AccountUpdateSerializer()
    product = ProductSerializer()

    class Meta:
        model = Storehouse
        fields = ('id', 'account', 'product', 'quantity')
