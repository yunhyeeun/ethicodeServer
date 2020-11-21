<?php
    $con = mysqli_connect("localhost", "cs409", "barcodereader", "CS409DB");
    mysqli_set_charset($con, "utf8");

    $barcode = "'".$_GET['barcode']."'";

    $query = "select * from item where barcode = ".$barcode;
    $res = mysqli_query($con, $query);

    class Item {

    }

    class News {

    }

    $row = mysqli_fetch_array($res);
    $item = new Item();
    $item->itemname = $row[1];
    $item->companyname = trim($row[2], "\r");
    $news_query = "select * from news where companyname = ".$row[2];
    $news_res = mysqli_query($con, $news_query);
    $news_array = array();
    while ($row = mysqli_fetch_array($news_res)) {
        $news_elem = new News();
        $news_elem->title = $row[1];
        $news_elem->date = $row[2];
        $news_elem->description = $row[3];
        $news_elem->link = $row[4];
        array_push($news_array, $news_elem);
    }
    $item->news = $news_array;
    $jsonData = json_encode($item, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    echo $jsonData. "\n";
    mysqli_close($con);

?>