from django.db import models

CHARS_LIMIT: int = 30
MAX_LENGTH: int = 256


class Category(models.Model):
    """Model for categories."""
    name = models.CharField(
        'Название',
        max_length=MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )

    class Meta:
        """Inner Meta class of Category model."""
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Displays Category name in admin panel."""
        return self.name[:CHARS_LIMIT]


class Genre(models.Model):
    """Model for genres."""
    name = models.CharField(
        'Название',
        max_length=MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )

    class Meta:
        """Inner Meta class of Genre model."""
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        """Displays Genre name in admin panel."""
        return self.name[:CHARS_LIMIT]


class Title(models.Model):
    """Model for titles."""
    name = models.CharField(
        'Название',
        max_length=MAX_LENGTH
    )
    year = models.IntegerField(
        'Год'
    )
    description = models.TextField(
        'Описание',
        max_length=MAX_LENGTH,
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
        return self.name[:CHARS_LIMIT]
