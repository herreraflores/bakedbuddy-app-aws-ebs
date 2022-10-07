from django.urls import path
from . import views

urlpatterns=[

  path('', views.index),
  path('daily-deals/', views.daily_deals),
  path('daily-deals/<str:product_type>/', views.product_type),
  path('dispensaries/<dispensary_id>/', views.dispensary),

]