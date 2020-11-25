# ethicodeServer

## About Server

Server : oracle free instance   
public ip : 193.122.105.82   
=======
oracle free instance   
apache2 - php - mysql
public ip : 193.122.105.82   
<br>
## About Database
Database name : CS409DB   
Table name : item   
mysql username : cs409   
mysql host : localhost   
mysql password : 

| Field       | Type         | Null | Key | Default | Extra |
|-------------|--------------|------|-----|---------|-------|
| barcode     | varchar(13)  | NO   | PRI | NULL    |       |
| itemname    | varchar(100) | NO   |     | NULL    |       |
| companyname | varchar(20)  | NO   |     | NULL    |       |   

<br>   

## About PHP
We just need query event.   
METHOD : GET   
INPUT : barcode   
OUTPUT : JSONobject(Array [barcode, itemname, companyname])   
<br>   

## How to Use in Client
HTTP URL : http://193.122.105.82/query.php   
parameter : ?barcode=YOURBARCODENUMBER   

