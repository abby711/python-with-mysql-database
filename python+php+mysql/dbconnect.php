<?php

$mysqli=new mysqli("localhost","root1","root1","database1");
//$mysqli-> query("insert into prof set profid='i79',profession='singer' ,salary=78000");
$result=$mysqli-> query("select id,firstname,profession from name,prof where name.id=profid and profession='singer' ");
$res_cnt=$mysqli->field_count;
$html=
"<html>
    <body>
     <table>
         <tr>
          <td><b>ID</b></td>
          <td><b>FIRST NAME</b></td>
          <td><b>PROFESSION</b></td>
         </tr>";
while ($row=$result->fetch_array())
{
	$html.="<tr>";
	for($i=0;$i<$res_cnt;$i++)
	{
		$html.= "<td>".$row[$i]."</td>";

	}
		$html.="</tr>";


}
$html.="
</table> </body></html>";    

echo $html;    
          



          

?>