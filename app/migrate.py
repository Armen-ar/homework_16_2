import json
import os

from app import db, models
from datetime import datetime


def load_fixture(file_path):
    """
    Загружает содержимое фикстуры.
    :param file_path: путь до файла с фикстурой.
    :return: данные из фикстуры, либо пустой список если не найдено.
    """
    content = []
    if os.path.isfile(file_path):
        with open(file_path, encoding="utf-8") as file:
            content = json.load(file)

    return content


def migration(fixture_path, model, convert_dates=False):
    """
    Унифицированная функция
    :param fixture_path: путь до фикстуры, модель, конвертация даты
    """
    fixture_content = load_fixture(fixture_path)

    for fixture in fixture_content:

        # Конвертация даты из формата mm/dd/YYYY в ISO-8601.
        if convert_dates:
            for field_name, field_value in fixture.items():
                if isinstance(field_value, str) and field_value.count('/') == 2:
                    fixture[field_name] = datetime.strptime(field_value, '%m/%d/%Y').date()

        if db.session.query(model).filter(model.id == fixture['id']).first() is None:
            db.session.add(model(**fixture))

    db.session.commit()


def migrate_user_roles(fixture_path):
    """
    Записывает данные из json-файла user_roles в таблицу user_roles,
    вызывая внутри унифицированную функцию migration()
    :param fixture_path:  путь до фикстуры.
    """
    migration(
        fixture_path=fixture_path,
        model=models.UserRole,
    )


def migrate_users(fixture_path):
    """
    Записывает данные из json-файла users в таблицу users,
    вызывая внутри унифицированную функцию migration()
    :param fixture_path: путь до фикстуры.
    """
    migration(
        fixture_path=fixture_path,
        model=models.User,
    )


def migrate_orders(fixture_path):
    """
    Записывает данные из json-файла orders в таблицу orders,
    вызывая внутри унифицированную функцию migration()
    :param fixture_path:  путь до фикстуры.
    """
    migration(
        fixture_path=fixture_path,
        model=models.Order,
        convert_dates=True,
    )


def migrate_offers(fixture_path):
    """
    Записывает данные из json-файла offers в таблицу offers,
    вызывая внутри унифицированную функцию migration()
    :param fixture_path: путь до фикстуры.
    """
    migration(
        fixture_path=fixture_path,
        model=models.Offer,
    )
