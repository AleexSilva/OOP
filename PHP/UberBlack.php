<?php
require_once('car.php');
class UberBlack extends Car{
    public $typeCarAccepted;
    public $SeatMaterial;

    public function __construct($license, $driver){
        parent::__construct($license, $driver, $typeCarAccepted,$SeatMaterial)
        $this->typeCarAccepted = $typeCarAccepted
        $this->SeatMaterial = $SeatMaterial
    }
}

?>