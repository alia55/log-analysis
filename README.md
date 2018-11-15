# Logs Analysis Report

## Introduction

This is a PostgreSQL project for the Udacity 2018 FSND course. It runs on python3, psycopg2 library, and PostgreSQL.

this project work on 	“newsdata.sql” DB and  contain	three	different	tables:
i. Authors:	table	includes	information	about	the	authors	of	articles.
ii. Articles:	table	includes	the	articles	themselves.
iii. Log:	table	includes	one	entry	for	each	time	a	user	has	accessed	the	site.
## Software	Installation

   * Vagrant:	https://www.vagrantup.com/downloads.html
   * Virtual Machine:	https://www.virtualbox.org/wiki/Downloads
   * Download	a	FSND	virtual	machine:	https://github.com/udacity/fullstack-nanodegree-vm
   After downloading requierd software you can access VM by e	following	commands:
      1) cd vagrant 
      2) vagrant	up 
      3) vagrant	ssh 
      4) cd	/vagrant
  
## 	Download	and	Load	the	Data
In this project you need to download "newsdata.sql" DB from the link
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat
    
* To load the DB in your project type

    psql -d news -f newsdata.sql
* To run the database type

   psql -d news

## Views we create a view for answering third question :
* You need to run the database type
     psql -d news 
* Then crate the view

       CREATE VIEW summary AS Select t1.date,t1.error,t2.total from

      (select DATE(time) as date,count (status) as error from log  where status !='200 OK' group by date ) t1
      join

      (select DATE(time) as date,count (*) as total from log  group by date) t2
      On t1.date = t2.date;
## Running

* Use  below command to run the python program that fetches query results.

    python log-analysis.py
