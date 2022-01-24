class Car:
    def __init__(self, brand, model, engine, fuel, color, passengers_quantity, price):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string0')
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model should be string')
        if isinstance(engine, str):
            self.engine = engine
        else:
            raise ValueError('Engine should be string')
        if isinstance(fuel, float):
            self.fuel = fuel
        else:
            raise ValueError('Fuel should be float')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(passengers_quantity, int):
            self.pass_q = passengers_quantity
        else:
            raise ValueError('Passengers should be integer')
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError('Price should be integer')

    def tunning(self, price_t):
        total = self.price + price_t
        return f'Total price of Car: {total}\n'

    def __str__(self):
        return f'Brand: {self.brand}\n' \
               f'Model: {self.model}\n' \
               f'Engine: {self.engine}\n' \
               f'Fuel: {self.fuel}\n' \
               f'Color: {self.color}\n' \
               f'Passengers Quantity: {self.pass_q}\n' \
               f'Price: {self.price}$\n'


car_1 = Car(brand='Mersedes', model='S-class 500', engine='Germany bomb',
            fuel=5.0, color='black', passengers_quantity=5, price=50000)
car_2 = Car(brand='Lexus', model='570', engine='Katana',
            fuel=5.7, color='silver', passengers_quantity=8, price=134789)
print(car_1)
print(car_1.tunning(1654))
print(car_2)
print(car_2.tunning(1963))
