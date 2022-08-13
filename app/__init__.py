from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # создаём объект db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # это вместо импортирования

    db.init_app(app)

    with app.app_context():

        from app import routes

        # db.drop_all()  # удаляем таблицы
        db.create_all()  # создаём таблицы

        from app import migrate

        migrate.migrate_user_roles(app.config['USER_ROLES_FIXTURE_PATH'])
        migrate.migrate_users(app.config['USERS_FIXTURE_PATH'])
        migrate.migrate_orders(app.config['ORDERS_FIXTURE_PATH'])
        migrate.migrate_offers(app.config['OFFERS_FIXTURE_PATH'])

        return app
