from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.livro_list, name='livro_list'),
    path('<slug:category_slug>/', views.livro_list, name='livro_list_by_category'),
    path('<int:id>/<slug:slug>/', views.livro_detail, name='livro_detail'),
]