import java.util.Map;

class UberBlack extends Car{
    Map<String, Map<String,Integer>> typeCarAccepted;
    Map<String> seatMaterial;



    public UberBlack(String license, Account driver, Map<String, Map<String,Integer>> typeCarAccepted){
        super(licence, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    
    }
}