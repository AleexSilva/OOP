from datetime import datetime as dt

class Payment:
    id = int
    
    def __init__(self,id):
        self.id = id
    

class Paypal(Payment):
    reference = str
    branch = str
    
    def __init__(self,id,reference,branch):
        super().__init__(id)
        self.reference = reference
        self.branch = branch
        

class Card(Payment):
    brand = str
    end_date = dt.today()
    cvv = int

    def __init__(self,id,brand,end_date,cvv):
        super().__init__(id)
        self.brand = brand
        self.end_date = end_date
        self.cvv = cvv
        
class Cash(Payment):
    def __init__(self, id):
        super().__init__(id) 