from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

from .models import Category, Product, Order, Coupon, Review, Brand

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


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = ('id', 'name', 'products')


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerAll(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    coupons = CouponSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'coupons')


class OrdersOfUserSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    birth_date = serializers.CharField(required=False)
    orders = OrderSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'orders')
