class Car{
    Integer id;
    String licence;
    Account driver;
    Integer n_passangers;

    public Car(String licence, Account Driver){
        this.licence = licence;
        this.driver = driver;
    }

    void printDataCar(){
        System.Out.println('Licence '+ licence+ 'Name Driver '+driver.name);
    }
} 