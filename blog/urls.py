from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('product/',views.product_detail,name='detail'),
    path('It/',views.it,name='It')
]