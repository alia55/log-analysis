# Logs Analysis Report

## Introduction

This is a PostgreSQL project for the Udacity 2018 FSND course. It runs on python3, psycopg2 library, and PostgreSQL.

this project work on 	“newsdata.sql” DB and  contain	three	different	tables:
i. Authors:	table	includes	information	about	the	authors	of	articles.
ii. Articles:	table	includes	the	articles	themselves.
iii. Log:	table	includes	one	entry	for	each	time	a	user	has	accessed	the	site.

## Running

* To load the DB type
 psql -d news -f newsdata.sql
* To run the database type
 psql -d news
* Use  below command to run the python program that fetches query results.
python log-analysis.py

## Views

 we create a view for answering third question :

 Select t1.date,t1.error,t2.total from

(select DATE(time) as date,count (status) as error from log  where status !='200 OK' group by date ) t1
join

(select DATE(time) as date,count (*) as total from log  group by date) t2
On t1.date = t2.date;
