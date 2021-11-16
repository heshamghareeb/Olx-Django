from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('<slug:category_slug>', views.product_list, name='product_list_category'),
    path('detail/<slug:product_slug>', views.product_detail, name='product_detail'), #<int:id><type:varibale>

]