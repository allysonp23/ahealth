from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, Owner, Car

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/add-owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name']
        new_owner = Owner(name=name)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('main.owners_list'))
    return render_template('add_owner.html')

@main.route('/add-car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        owner_id = request.form['owner_id']
        model = request.form['model']
        color = request.form['color']
        owner = Owner.query.get(owner_id)
        if owner and len(owner.cars) < 3:
            new_car = Car(model=model, color=color, owner=owner)
            db.session.add(new_car)
            db.session.commit()
            return redirect(url_for('main.owners_list'))
        return jsonify({"error": "Owner cannot have more than 3 cars"}), 400
    return render_template('add_car.html')

@main.route('/owners-list')
def owners_list():
    owners = Owner.query.all()
    return render_template('owners_list.html', owners=owners)
