from django.urls import path
from . import views
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('update/<int:pk>/', views.ArticleUpdateView.as_view(), name='update'),
    path('<int:id>/', views.article_detail, name='detail'),
]
