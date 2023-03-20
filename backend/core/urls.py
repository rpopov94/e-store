from django.urls import include, path
from . import routers, views


''' @NOTE: Auth '''
urlpatterns = [
    path('data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),
    path('users/', include(routers.router.urls)),
    path('orders/', views.OrderListView.as_view()),
    path('brands/', views.BrandViewList.as_view()),
    path('products/', views.ProductsViewList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('orders/<int:id>/', views.OrderApiRetrieveDestroyView.as_view()),
    path('brands/<int:id>/', views.BrandViewListById.as_view()),
    path('products/<int:id>/', views.ProductsViewListById.as_view()),
    path('categories/<int:id>/', views.CategoryListById.as_view()),

]