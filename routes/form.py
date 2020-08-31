from flask import Blueprint, request, session, render_template
from bill import Bill

form_routes = Blueprint('form_routes', __name__)

@form_routes.route('/add_meal_form')
def add_meal_form():
    return render_template('add_meal_form.html')

@form_routes.route('/add_service_form')
def add_service_form():
    return render_template('add_service_form.html')

@form_routes.route('/check_discount_form')
def check_discount_form():
    return render_template('/check_discount_form.html')

@form_routes.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')
