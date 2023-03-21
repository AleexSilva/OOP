from Car import Car
from Account import Account
from UberX import UberX
from Payment import Payment, Cash, Card, Paypal




if __name__ == '__main__':
    print('Hola Mundo')
    uberX = UberX('AMX485',Account('Felipe Piña','24987653'),'Hyundai','S201')
    payment1 = Paypal('12333','platzi','Sucursal Oeste')
    print(vars(uberX))
    print(vars(payment1))
    #print(vars(car.driver))