from rest_framework import pagination, viewsets
from rest_framework.filters import SearchFilter

from reviews.models import Category, Genre, Title

from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from .mixins import GetCreateDeleteMixin


class CategoryViewSet(GetCreateDeleteMixin):
    """ViewSet for categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    pagination_class = pagination.LimitOffsetPagination


class GenreViewSet(GetCreateDeleteMixin):
    """ViewSet for genres."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    pagination_class = pagination.LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    """ViewSet for titles."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('category', 'genre', 'name', 'year')
    pagination_class = pagination.LimitOffsetPagination
