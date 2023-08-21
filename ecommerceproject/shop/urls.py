from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # URL pattern to display all products and categories
    path('', views.allProdCat, name='allProdCat'),

    # URL pattern to display products based on a specific category
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
