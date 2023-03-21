class Car{

    constructor(license,driver){
        this.id;
        this.license = license;
        this.driver = driver;
        this.n_passangers;
    }

    printDataCar= () => {
        console.table(this.driver) //print a table with all the data
        console.log(this.driver.name)
        console.log(this.driver.document)
    }
}