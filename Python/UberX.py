from Car import Car

class UberX(Car):
    brand = str
    model = str
    
    def __init__(self,licence,driver,n_passangers,brand,model):
        super().__init__(licence,driver,n_passangers)
        self.brand = brand
        self.model = model