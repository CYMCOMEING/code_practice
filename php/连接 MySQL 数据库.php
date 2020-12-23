<?php

 $host="localhost";
 $uname="database username";
 $pass="database password";
 $database = "database name";
 $connection=mysql_connect($host,$uname,$pass) 
 or die("Database Connection Failed");

 $result=mysql_select_db($database)
 or die("database cannot be selected");

?>