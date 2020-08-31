from entry import Entry

class Service(Entry):

    def __init__(self, name, price, guest_number):
        super().__init__(name,price)
        self.guest_number = guest_number

    def generate_description(self):
        return "Product name: {}, price: {}, guest number {} \n"\
            .format(self.name, self.price, self.guest_number)

