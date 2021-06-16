from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('', views.ecv_list, name='ecv_list'),
    path('<slug:category_slug>/', views.ecv_list, name='ecv_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ecv_detail, name='ecv_detail'),
]