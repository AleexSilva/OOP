from Payment import Payment

class Paypal(Payment):
    reference = str
    branch = str
    
    def __init__(self,id,reference,branch):
        super().__init__(id)
        self.reference = reference
        self.branch = branch