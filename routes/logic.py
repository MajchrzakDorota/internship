import json
from datetime import datetime
from flask import jsonify

from flask import Blueprint, request, session, render_template
from bill import Bill

logic_routes = Blueprint('logic_routes', __name__)


@logic_routes.route('/')
def index():
    return render_template('layout.html')


@logic_routes.route('/add_meal', methods=['POST'])
def add_meal():
    bill = get_bill()
    name = request.form['meal_name']
    try:
        price = float(request.form['meal_price'])
    except ValueError:
        return render_template('default_template.html', message="Unable to convert price")
    bill.add_meal(name, price)
    session['entries'] = bill.entries
    return render_template('default_template.html', message= "Success")


@logic_routes.route('/add_service', methods=['POST'])
def add_service():
    bill = get_bill()
    name = request.form['service_name']
    price = float(request.form['service_price'])
    guests_number = float(request.form['service_guests'])
    bill.add_service(name, price, guests_number)
    session['entries'] = bill.entries
    return render_template('default_template.html', message="Success")


@logic_routes.route('/sum')
def sum():
    #return render_template('404.html', message="Unable to access the route"), 404
    bill = get_bill()
    return render_template('default_template.html', message=f"Overall sum: {bill.calculate()}")

@logic_routes.route('/create_a_bill')
def create_a_bill():
    bill = get_bill()
    bill_cration = []
    for entry in bill.entries:
        bill_cration.append(entry)
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y %H-%M-%S")
    filename = f"Bill {date_time}.json"
    with open(filename, "w") as file:
        json.dump(bill_cration, file)
    return jsonify(bill_cration)



@logic_routes.route('/check', methods=['POST'])
def check():
    overall_sum = float(request.form['overall_sum'])
    discount_value = int(request.form['discount'])
    value = Bill.check_discount(overall_sum,discount_value)
    return render_template('default_template.html', message=f"Whole order will cost: {value} after discount")


@logic_routes.route('/save/<filename>')
def save(filename):
    bill = get_bill()
    try:
        bill.print_to_file(filename)
        return "Success!"
    except:
        return "Unable to save the file"


@logic_routes.route('/add_discount/<discount>')
def add_discount(discount):
    bill = get_bill()
    discount = int(discount)
    return render_template('default_template.html', message=f"Cost with discount is: {bill.calculate_with_discount(discount)}")


@logic_routes.route('/contact', methods=['POST'])
def send_message():
    name = request.form['user_name']
    text = request.form['user_text']
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y %H-%M-%S")
    filename = f"Contact {date_time}.json"
    form = {"name": name, "text": text}
    with open(filename, "w") as file:
        # file.writelines(f"Name: {name}, Message: {text}")
        json.dump(form, file)
    return render_template('default_template.html', message=f"Your message was saved")


def get_bill():
    bill = Bill()
    if 'entries' in session:
        entries = session['entries']
        bill.entries = entries
    return bill