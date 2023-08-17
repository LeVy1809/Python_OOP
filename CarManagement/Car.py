class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def increase_mileage(self, miles):
        self.mileage += miles

    def display_info(self):
        print('Make:', self.make)
        print('Model:', self.model)
        print('Year:', self.year)
        print('Mileage:', self.mileage)
        
car = Car('Toyota', 'Celica', 1971, 1005)
car.increase_mileage(500)

car.display_info()