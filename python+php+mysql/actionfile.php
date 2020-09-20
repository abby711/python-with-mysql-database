<?php
if(isset($_POST["nam"]))
   {
    $t=$_POST["nam"];
   	echo "WELCOME".$t;
   }
else
 echo "no name";  

if(isset($_POST["squad"]))
   {
    $t=$_POST["squad"];
   	foreach ($t as $i) {
   		echo $i."<br>";
   		# code...
   	}
   }
 ?>