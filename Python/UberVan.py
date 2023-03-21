from Car import Car

class UberVan(Car):
    TypeCarAccepted =[]
    SeatMaterial = []
    
    
    def __init__(self,license,driver,TypeCarAccepted,SeatMaterial):
        super().__init__(license,driver)
        self.TypeCarAccepted=TypeCarAccepted
        self.SeatMaterial=SeatMaterial