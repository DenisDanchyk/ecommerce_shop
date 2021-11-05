from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage ,name='homepage'),
    path('detail/', views.product_detail ,name='product_detail')
]
