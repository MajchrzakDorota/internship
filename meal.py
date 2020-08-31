from entry import Entry

class Meal(Entry):

    def __init__(self, name, price):
        super().__init__(name,price)

    @classmethod
    def from_dict(cls, dictionary):
        returnObject = Meal(None, None)
        for k, v in dictionary.items():
            setattr(returnObject, k, v)
        return returnObject