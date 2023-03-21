from Car import Car

if __name__ == '__main__':
    print('Hola Mundo')
    car = Car()
    car.licence = 'AMS789'
    car.driver = 'Andrés Herrera'
    print(vars(car))
    
    car2 = Car()
    car2.licence = 'AXM951'
    car2.dirver = 'Save Martha'
    print(vars(car2))