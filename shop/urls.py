from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path(r'', views.product_list, name='product_list'),
    path(r'<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'),
]