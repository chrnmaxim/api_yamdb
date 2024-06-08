from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category."""

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
        )


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for genre."""

    class Meta:
        model = Genre
        fields = (
            'name',
            'slug',
        )


class TitleSerializer(serializers.ModelSerializer):
    """Serializer for titles."""
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    # rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            # 'rating',
            'description',
            'genre',
            'category'
        )
