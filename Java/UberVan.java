import java.util.Map;

class UberVan extends Car{
    Map<String, Map<String,Integer>> typeCarAccepted;
    Map<String> seatMaterial;



    public UberVan(String license, Account driver, Map<String, Map<String,Integer>> typeCarAccepted){
        super(licence, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    
    }
}