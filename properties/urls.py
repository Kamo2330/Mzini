from django.urls import path
from . import views


urlpatterns = [
    path('', views.browse, name='browse'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
    path('sell/', views.sell_property, name='sell_property'),
]


