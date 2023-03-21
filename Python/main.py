from Car import Car
from Account import Account

if __name__ == '__main__':
    print('Hola Mundo')
    car = Car('AMX485',Account('Felipe Piña','24987653'))
    print(vars(car))
    print(vars(car.driver))