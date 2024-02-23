def calculator(num, **kw):
    total = num
    total += kw.get('add')
    total -= kw.get('minus')
    total *= kw.get('multiply')
    
    print(total)
    
calculator(2, add = 4, minus = 3, multiply = 2)

class Car():
    def __init__(self, **kw):
        self.color = kw.get('color')
        self.model = kw.get('model')
        self.speed = kw.get('speed')

my_first_car = Car(color = 'red', speed = 10)
my_second_car = Car(model = 'nissan', color = 'white')

print(my_first_car.color)
print(my_second_car.model)