# ethicodeServer

## About News Crawler   

NAVER news search API

### Keyword-based Search   

| Ethical standard            | Keyword                            |
|-----------------------------|------------------------------------|
| Environmental performance   | Eco-friendly production (친환경 생산) |
| Corporate philanthropy      | Donation, sponsorship, sharing, volunteer activities, public benefit campaigns (기부, 후원, 나눔활동, 봉사활동, 공익캠페인) |
| Non-discrimination related to human rights, Labor practices | Boss around, ethical management, discrimination and abhor (갑질, 윤리경영, 차별 혐오) |
| Product liability           | FDA, hygiene management, HACCP (식약처, 위생관리 기준, 위생검사, HACCP) |
| Etc                         | Unfair transaction, fair trade commission, prosecution, boycott (부당거래, 공정위, 검찰, 불매) |

### Preprocessing   

- 주가 관련 뉴스 삭제
- 홍보 관련 뉴스 삭제
- 동일 내용 뉴스 삭제

## About Server

Server : oracle free instance   
apache2 - php - mysql
public ip : 193.122.105.82   

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
