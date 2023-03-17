from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers
from .models import Category, Brand, Product, Order
from .custom_permissions import IsOwnerOrAdmin, IsOwner

CustomUser = get_user_model()

''' @NOTE: views for users and admin '''


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserRetrieveSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_object(self):
        return self.request.user


''' @NOTE: views for all '''


class CategoryList(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryListById(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializerAll
    lookup_field = 'id'


class BrandViewList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer


class BrandViewListById(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    lookup_field = 'id'


class ProductsViewList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductsViewListById(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'id'


''' @NOTE: views for admin & users '''


class UserInfoView(generics.RetrieveAPIView):
    permission_classes = (IsOwnerOrAdmin,)
    queryset = CustomUser.objects.all()
    serializer_class = serializers.OrdersOfUserSerializer
    lookup_field = 'id'


''' @NOTE: only user '''


# class OrderApiRetrieweDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsOwner,)
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderSerializer

class OrderListView(generics.ListAPIView):
    permission_classes = (IsOwnerOrAdmin, )
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderApiRetrieweDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrAdmin, )
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = 'id'
