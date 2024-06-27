from django.urls import path
from blog_and_news.api.views import BlogNewsListView, BlogNewsRetrieveUpdateDestroyView, SliderListView, \
    SliderRetrieveView

urlpatterns = [
    path('blog_news/', BlogNewsListView.as_view(), name='blog-news-list-create'),
    path('blog_news/<int:pk>/', BlogNewsRetrieveUpdateDestroyView.as_view(), name='blog-news_retrieve-update-destroy'),
    path('sliders/', SliderListView.as_view(), name='slider-list'),
    path('sliders/<int:pk>/', SliderRetrieveView.as_view(), name='slider-retrieve'),
]
