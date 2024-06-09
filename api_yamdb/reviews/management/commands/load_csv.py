import csv

from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from reviews.models import Category, Genre, Title

from api_yamdb.settings import CSV_DIR


MODELS: dict = {
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
}


class Command(BaseCommand):
    """Class for management commands."""

    def handle(self, *args, **options):
        """
        Uploads data to db from csv file.

        To run the command do the following:
        'python api_yamdb/manage.py load_csv'.
        """

        try:
            for model, file in MODELS.items():
                with open(
                    f'{CSV_DIR}{file}',
                    encoding='utf-8'
                ) as f:
                    reader = csv.DictReader(f)
                    model.objects.bulk_create(model(**data) for data in reader)
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'Файл {file} не найден.')
            )
        except (ValueError, IntegrityError) as error:
            self.stdout.write(
                self.style.ERROR(f'Ошибка данных в файле {file}. {error}.')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Все данные успешно загружены.')
            )
