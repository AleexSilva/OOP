<?php

require_once('Car.php');
require_once('UberX.php');
require_once('Account.php');

$UberX = new UberX("AW456", new Account("Andres Herrera", "25789456"),'Chevrolet','Spark');
$UberX-> printDataCar();
?>