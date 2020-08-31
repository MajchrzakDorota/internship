from service import Service
from meal import Meal

class Bill:

    def __init__(self):
        self.__entries = []

    @staticmethod
    def check_discount(overall_sum, discount):
        return overall_sum - overall_sum * discount/100

    def calculate_with_discount(self, discount):
        current_sum = self.calculate()
        return current_sum - current_sum * discount/100

    def calculate(self):
        cost = 0.0
        for entry in self.__entries:
            cost += entry.price
        return cost

    def print_to_file(self, filename):
        with open(filename, "w") as file:
            for entry in self.__entries:
                file.write(entry.generate_description())

    def add_meal(self, name, price):
        meal = Meal(name,price)
        self.__entries.append(meal)

    def add_service(self, name, price, guest_number):
        service = Service(name, price, guest_number)
        self.__entries.append(service)

    @property
    def entries(self):
        return [element.__dict__ for element in self.__entries]

    @entries.setter
    def entries(self, entries):
        if entries == []:
            print("Entries can't be empty")
            return
        self.__entries = [Meal.from_dict(entry) for entry in entries]