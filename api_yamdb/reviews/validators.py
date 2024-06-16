from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(year) -> None:
    """Validates title's year."""
    if year > datetime.now().year:
        raise ValidationError(
            f'Дата выхода произведения не может быть раньше, '
            f'чем {datetime.now().year}.'
        )
