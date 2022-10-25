from django.urls import path
from . import views

urlpatterns=[
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleListView.as_view(),name='article_edit'),
    path('<int:pk>/', views.ArticleListView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', views.ArticleListView.as_view(), name='article_edit')
]