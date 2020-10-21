<?php
    $con = mysqli_connect("localhost", "cs409", "barcodereader", "CS409DB");
    mysqli_set_charset($con, "utf8");

    $barcode = "'".$_GET['barcode']."'";

    $query = "select * from item where barcode = ".$barcode;
    $res = mysqli_query($con, $query);
    $result = array();

    while ($row = mysqli_fetch_array($res)) {
        array_push($result,
                array("BARCODE"=>$row[0],
                "ITEMNAME"=>$row[1],
                "COMPANYNAME"=>$row[2]));
    }
    echo json_encode(array("Item"=>$result), JSON_UNESCAPED_UNICODE);
    mysqli_close($con);

?>