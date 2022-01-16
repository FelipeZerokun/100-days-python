def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(3, 5, 2, 7, 3, 6))


def calculate(n, **kwargs):
    print(kwargs)
    for (key, value) in  kwargs.items():
        print(key)
        print(value)
        n*= value
    print(n)
calculate(10, add=3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make = "Nissan", model= "GTR")
print(my_car.model)