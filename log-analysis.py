# !/usr/bin/env python3
# -*- coding: latin-1 -*-
import os
import sys
import psycopg2

DBNAME = "news"


def get_articles():
    """Return most popular three articles of all time"""


db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select count(path) as views,title from articles,log\
 where  concat('/article/',slug) =log.path\
 group by title order by views desc limit 3")
articles = c.fetchall()
db.close()
for row in articles:
    print "\"%s\" — %s views" % (row[1], row[0])


def get_authors():
    """Return most popular three articles of all time"""


db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select count(path) as views,name from articles,log,authors\
 where  concat('/article/',slug) =log.path\
 and articles.author = authors.id group by authors.id order by views desc")
articles = c.fetchall()
db.close()
for row in articles:
    print "%s — %s views" % (row[1], row[0])


def get_errors():
    """Return most popular three articles of all time"""


db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("Select to_char(date,'Mon dd,yyyy'), error *100.0 /total as percent\
 from summary where error *100.0 /total >1 ")
articles = c.fetchall()
db.close()
for row in articles:
    print " %s — %.2f%% errors" % (row[0], row[1])
