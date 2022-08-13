from app import models, db
from flask import current_app as app, jsonify, abort, request


@app.route('/users', methods=['GET'])
def get_users():
    """Возвращает список пользователей."""
    users = db.session.query(models.User).all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'email': user.email,
            'role': user.role.name,
            'phone': user.phone,
        })
    return jsonify(users_list)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Возвращает пользователя по ID."""
    user = db.session.query(models.User).filter(models.User.id == user_id).first()  # first (если не найдёт id, не
                                                                                     # упадёт с ошибкой, а выдаст None)
    if user is None:

        return abort(404)

    return jsonify({
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age,
        'email': user.email,
        'role': user.role.name,
        'phone': user.phone,
    })


@app.route('/orders', methods=['GET'])
def get_orders():
    """Возвращает список заказов."""
    orders = db.session.query(models.Order).all()
    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'name': order.name,
            'description': order.description,
            'start_date': order.start_date.isoformat(),
            'end_date': order.end_date.isoformat(),
            'address': order.address,
            'price': order.price,
            'customer_id': order.customer_id,
            'executor_id': order.executor_id,
        })
    return jsonify(orders_list)


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Возвращает заказ по ID."""
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:

        return abort(404)

    return jsonify({
        'id': order.id,
        'name': order.name,
        'description': order.description,
        'start_date': order.start_date.isoformat(),
        'end_date': order.end_date.isoformat(),
        'address': order.address,
        'price': order.price,
        'customer_id': order.customer_id,
        'executor_id': order.executor_id,
    })


@app.route('/offers', methods=['GET'])
def get_offers():
    """Возвращает список предложений."""
    offers = db.session.query(models.Offer).all()
    offers_list = []
    for offer in offers:
        offers_list.append({
            'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id,
        })
    return jsonify(offers_list)


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    """Возвращает предложениe по ID."""
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:

        return abort(404)

    return jsonify({
        'id': offer.id,
        'order_id': offer.order_id,
        'executor_id': offer.executor_id,
    })


@app.route('/users', methods=['POST'])
def create_users():
    """Cоздаёт нового пользователя."""
    data = request.json

    db.session.add(models.User(**data))

    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_users(user_id):
    """Обновляет данные пользователя."""
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)

    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    """Удаляет данные пользователя."""
    db.session.query(models.User).filter(models.User.id == user_id).delete()

    db.session.commit()

    return {}


@app.route('/orders', methods=['POST'])
def create_orders():
    """Cоздаёт новый заказ."""
    data = request.json

    db.session.add(models.Order(**data))

    db.session.commit()

    return {}


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_orders(order_id):
    """Обновление заказа."""
    data = request.json

    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        abort(404)

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)

    db.session.commit()

    return {}


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_orders(order_id):
    """Удаляет заказ."""
    db.session.query(models.Order).filter(models.Order.id == order_id).delete()

    db.session.commit()

    return {}


@app.route('/offers', methods=['POST'])
def create_offers():
    """Cоздаёт новое предложение."""
    data = request.json

    db.session.add(models.Offer(**data))

    db.session.commit()

    return {}


@app.route('/offers/<int:offer_id>', methods=['PUT'])
def update_offers(offer_id):
    """Обновлеяет предложение."""
    data = request.json

    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)

    db.session.commit()

    return {}


@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offers(offer_id):
    """Удаляет предложение."""
    db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()

    db.session.commit()

    return {}
