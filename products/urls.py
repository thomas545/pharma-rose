from django.urls import path
from .views import category_product_list, ProductListView, ProductDetailView
# create urls here


app_name = 'products'





urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', category_product_list, name='category_product_list'),
    path('single-product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),


]
