from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

from .models import Category, Product, Order, OrderItem, Coupon, Review

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """
    We use this serializer for user registration. Most of the fields have
    `required=False`, but can be configured as needed. This serializer is used
    in `accounts.viewsets.CustomUserModelViewSet`.
    """
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password', 'bio', 'gender', 'birth_date')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    """
    We use this serializer to retrieve data of the currently logged in user.
    It is used in `accounts.views.UserRetrieveUpdateDestroyAPIView`
    """
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date', 'id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'products', 'order_date', 'status', 'delivery_address', 'total_price')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')


class UserStatisticSerializer(serializers.ModelSerializer):
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date')
