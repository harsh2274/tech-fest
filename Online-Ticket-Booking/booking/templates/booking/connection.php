<?php
    $servername = "localhost" ;
    $username = "root" ;
    $password = "855fc1" ;
    $dbname = "newDB" ;
    $conn = mysqli_connect($username,$password,$servername,$dbname) ;
    
    if($conn)
        echo "Connection Success" ;
    else
        die ("Connection failed") ;
?>