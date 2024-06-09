from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from api_yamdb.settings import LENGTH_TEXT, LENGTH_TEXT, LIMIT_EMAIL


class User(AbstractUser):
    """Класс пользователей."""

    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
    ROLE_CHOICES = (
        (USER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Администратор"),
    )
    username = models.CharField(
        "Имя пользователя",
        max_length=LENGTH_TEXT,
        unique=True,
        validators=[RegexValidator(
            regex=r"^[\w.@+-]+$",
            message="Имя пользователя содержит недопустимый символ"
        )],
        error_messages={
            "unique": "Пользователь с таким именем уже существует!",
        },
    )
    email = models.EmailField(
        "email",
        max_length=LIMIT_EMAIL,
        unique=True
    )
    role = models.CharField(
        "Роль",
        max_length=max(len(role) for role, _ in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=USER,
    )
    bio = models.TextField(
        "Биография",
        blank=True
    )
    first_name = models.CharField(
        "Имя",
        max_length=LENGTH_TEXT,
        blank=True
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=LENGTH_TEXT,
        blank=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.username[:LENGTH_TEXT]

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser or self.is_staff
