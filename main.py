import view
from bill import Bill
from flask import Flask
from routes import logic, form

app = Flask(__name__)
app.register_blueprint(logic.logic_routes)
app.register_blueprint(form.form_routes)
bill = None


def main():
    action = "Start"

    while action != "End":
        action = input("What do you want to do?[Add meal, Add Service, Sum, Discount, Save, End]:")

        if action == "Add meal":
            name, price = view.ask_for_meal()
            if name is None or price is None:
                continue
            bill.add_meal(name, price)
        elif action == "Add Service":
            name,price,guest_number = view.ask_for_service()
            bill.add_service(name, price, guest_number)
        elif action == "Sum":
            print(bill.calculate())
        elif action == "Discount":
            discount = view.ask_for_discount()
            print(bill.calculate_with_discount(discount))
        elif action == "Check":
            overall_sum, discount = view.ask_for_check_discount()
            if overall_sum is None or discount is None:
                continue
            print(Bill.check_discount(overall_sum, discount))
        elif action == "Save":
            filename = view.ask_for_filename()
            bill.print_to_file(filename)


if __name__ == '__main__':
    app.secret_key = "secret value"
    app.run(debug=True)
