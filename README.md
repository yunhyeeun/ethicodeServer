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
Database name : CS489DB   
Table name : item   
mysql username : cs489   
mysql host : localhost   
mysql password : 

| Field       | Type         | Null | Key | Default | Extra |
|-------------|--------------|------|-----|---------|-------|
| barcode     | varchar(13)  | NO   | PRI | NULL    |       |
| itemname    | varchar(100) | NO   |     | NULL    |       |
| companyname | varchar(20)  | NO   |     | NULL    |       |   

Database name : CS489DB   
Table name : news   
mysql username : cs489   
mysql host : localhost   
mysql password : 

| Field       | Type         | Null | Key | Default | Extra               |
|-------------|--------------|------|-----|---------|---------------------|
| id          | int(11)      | NO   | PRI | NULL    |                     |
| companyname | varchar(20)  | YES  |     | NULL    |                     |
| keyword     | varchar(10)  | YES  |     | NULL    |                     |   
| title       | varchar(100) | YES  |     | NULL    |                     |   
| description | varchar(200) | YES  |     | NULL    |                     |   
| originallink| varchar(300) | YES  |     | NULL    |                     |   
| link        | varchar(300) | YES  |     | NULL    |                     |   
| pubDate     | varchar(300) | YES  |     | NULL    |                     |   

<br>   

## About PHP
We just need query event.   
METHOD : GET   
INPUT : barcode   
OUTPUT : JSONobject({ itemname, companyname, news: Array({ title, date, description, link } ] }   

<br>   

## How to Use in Client
HTTP URL : http://193.122.105.82/query.php   
parameter : ?barcode=YOURBARCODENUMBER   

