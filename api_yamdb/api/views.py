from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import pagination, permissions, viewsets
from rest_framework.filters import SearchFilter

from reviews.models import Category, Genre, Title, Review

from .mixins import GetCreateDeleteMixin
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          ReviewSerializer,
                          CommentSerializer)


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
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitleSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('category', 'genre', 'name', 'year')
    pagination_class = pagination.LimitOffsetPagination


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for reviews."""
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # Добавить кастомные ограничения для модераторов и админов

    def get_title(self):
        """
        Проверяет наличие запрашиваемого произведения в БД и возвращает его
        """
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(
            author=self.request.user,
            title=title
        )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        # Добавить разрешение на редактирование для модераторов и админов


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for comments."""
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # Добавить кастомные ограничения для модераторов и админов

    def get_review(self):
        """
        Проверяет наличие запрашиваемого отзыва в БД и возвращает его
        """
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review

    def get_queryset(self):
        review = self.get_review()
        return review.comments.all()

    def perform_create(self, serializer):
        review = self.get_review()
        serializer.save(
            author=self.request.user,
            review=review
        )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        # Добавить разрешение на редактирование для модераторов и админов
