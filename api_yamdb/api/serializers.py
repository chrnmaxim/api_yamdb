from django.conf import settings
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category."""

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
        )
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for genre."""

    class Meta:
        model = Genre
        fields = (
            'name',
            'slug',
        )


class TitleWriteSerializer(serializers.ModelSerializer):
    """Serializer for add titles."""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category'
        )


class TitleReadSerializer(serializers.ModelSerializer):
    """Serializer for get titles."""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for reviews."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    score = serializers.IntegerField(
        max_value=settings.MAX_SCORE,
        min_value=settings.MIN_SCORE
    )

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and title.reviews.filter(author=author).exists()
        ):
            raise ValidationError('Отзыв на данное произведение уже добавлен.')
        return data

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date'
        )
        error_messages = {
            'score': {
                'max_value': f'Оценка не может быть выше {settings.MAX_SCORE}',
                'min_value': f'Оценка не может быть ниже {settings.MIN_SCORE}'
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'pub_date'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for user creation."""

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, username):
        if username in 'me':
            raise serializers.ValidationError('Username не может быть "me".')
        return username


class UserRecieveTokenSerializer(serializers.Serializer):
    """Serializer for receiving token for user."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=settings.MAX_LENGTH,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=settings.MAX_LENGTH,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )

    def validate_username(self, username):
        if username in 'me':
            raise serializers.ValidationError('Username не может быть "me".')
        return username
