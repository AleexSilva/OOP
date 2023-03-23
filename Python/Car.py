from Account import Account

class Car:
    id = int
    license = str
    driver = Account('','','','')
    n_passangers = int 
    
    def __init__(self,license,driver,n_passangers):
        self.license = license
        self.driver = driver
        self.n_passangers = n_passangers