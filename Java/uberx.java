class UberX extends Car{
    String brand;
    String model;

    public UberX(String license, Account driver, Strng brand, String model){
        super(license,driver);
        this.brand = brand;
        this.model = model;
        
    }
}