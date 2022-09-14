# ads_scraper
Script for scraping apartment ads 
### How to run code
1. Clone the repository
2. Set all dependecies from requirements.txt
3. docker-compose up to activate postgres
4. type in the terminal: python adds.py

After code is completed:
- check postgres adminer in localhost 8080
- enter the crdentials:
  postgresql12,
  postgres,
  postgres1234,
  my_database
- inside adminer you can find your scraped database

Database schema:


|Column	|Type	|Comment|
| :---  |:---:| ---:  |
|index	|bigint NULL|	
|images	|text NULL	|
|titles	|text NULL|	
|created_date	|text NULL|	
|locations	|text NULL|	
|badrooms	|text NULL|	
|descriptions	|text NULL|	
|currancy	|text NULL|	
|prices	|text NULL|

SQL dump of data is in repository
