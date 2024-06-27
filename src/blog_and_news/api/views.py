from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from blog_and_news.api.serializers import BlogNewsSerializer, SlidersSerializer
from blog_and_news.models import BlogNews
from blog_and_news.api.filters import BlogNewsFilter

from blog_and_news.models import Slides


class BlogNewsListView(generics.ListAPIView):
    queryset = BlogNews.objects.all().prefetch_related('slides')
    serializer_class = BlogNewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogNewsFilter
    search_fields = ['title', 'category']


class BlogNewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogNews.objects.all().prefetch_related('slides')
    serializer_class = BlogNewsSerializer


class SliderListView(generics.ListAPIView):
    queryset = Slides.objects.all()
    serializer_class = SlidersSerializer


class SliderRetrieveView(generics.RetrieveAPIView):
    queryset = Slides.objects.all()
    serializer_class = SlidersSerializer
