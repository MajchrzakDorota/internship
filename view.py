def ask_for_meal():
    name = input("Provide meal name: ")
    price = input("Provide meal price")
    try:
        return name, float(price)
    except ValueError:
        print("Unable to add a product, you need to provide a valid price")
        return None, None

def ask_for_discount():
    discount = input("Provide discount level(%):")
    return int(discount)

def ask_for_filename():
    filename = input("Provide filename")
    return filename

def ask_for_service():
    name = input("Provide service type:")
    price = input("Provide price:")
    guests = input("Provide number of guests:")
    try:
        return name, float(price), guests
    except ValueError:
        print("Unable to add a service, you need to provide a valid")
        return None, None, None