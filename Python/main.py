from Car import Car
from Account import Account,Driver,User
from UberX import UberX
from Payment import Payment, Cash, Card, Paypal




if __name__ == '__main__':
    print('Hola Mundo')
    uberX = UberX('AMX485',Account('Felipe Piña','24987653','Lipe91@live.com','Piña2001'),3,'Hyundai','S201')
    payment1 = Paypal('12333','platzi','Sucursal Oeste')
    driver1 = Driver('Felipe Piña','24987653','Lipe91@live.com','Piña2001')
    print(vars(uberX))
    print(vars(payment1))
    print(vars(driver1))
    #print(vars(car.driver))