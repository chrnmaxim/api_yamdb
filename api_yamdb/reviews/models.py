from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from reviews.validators import validate_year
from users.models import User


class Category(models.Model):
    """Model for categories."""
    name = models.CharField(
        'Название',
        max_length=settings.MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )

    class Meta:
        """Inner Meta class of Category model."""
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    def __str__(self):
        """Displays Category name in admin panel."""
        return self.name[:settings.CHARS_LIMIT]


class Genre(models.Model):
    """Model for genres."""
    name = models.CharField(
        'Название',
        max_length=settings.MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )

    class Meta:
        """Inner Meta class of Genre model."""
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('id',)

    def __str__(self):
        """Displays Genre name in admin panel."""
        return self.name[:settings.CHARS_LIMIT]


class Title(models.Model):
    """Model for titles."""
    name = models.CharField(
        'Название',
        max_length=settings.MAX_LENGTH
    )
    year = models.PositiveSmallIntegerField(
        'Год',
        db_index=True,
        validators=(validate_year,)
    )
    description = models.TextField(
        'Описание',
        max_length=settings.MAX_LENGTH,
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True,
        blank=True
    )

    class Meta:
        """Inner Meta class of Title model."""
        verbose_name = 'произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('id',)

    def __str__(self):
        """Displays Title name in admin panel."""
        return self.name[:settings.CHARS_LIMIT]


class Review(models.Model):
    """Model for title reviews."""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField('Текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[
            MaxValueValidator(
                settings.MAX_SCORE,
                message=f'Оценка не может быть выше {settings.MAX_SCORE}.'
            ),
            MinValueValidator(
                settings.MIN_SCORE,
                message=f'Оценка не может быть ниже {settings.MIN_SCORE}.'
            )
        ]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        """Inner Meta class of Review model."""
        ordering = ['-pub_date']
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]

    def __str__(self):
        """Displays Review text in admin panel."""
        return self.text[:settings.CHARS_LIMIT]


class Comment(models.Model):
    """Model for review comments."""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField('Текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        """Inner Meta class of Comment model."""
        ordering = ['-pub_date']
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Displays Comment text in admin panel."""
        return self.text[:settings.CHARS_LIMIT]
