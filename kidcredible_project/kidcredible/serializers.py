from rest_framework import serializers
from .models import User, Product, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'reviews')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    products = serializers.HyperlinkedRelatedField(
        view_name='product_detail',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'name', 'body', 'users', 'rating', 'products')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'type', 'description',
                  'image', 'rating', 'reviews')
