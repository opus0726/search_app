from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('detail/<str:item_id>/', views.detail_view, name='detail'),
    path('review/<str:item_id>/', views.CreateReviewView.as_view(), name='review'),
    path('search/',views.search_view, name="search"),
]
