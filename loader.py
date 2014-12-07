#!/usr/bin/env python
#Anirudh Agarwala
#Pasha Pourmand
#2014-12-6

import psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='ppourmand' host='localhost'")
    print "I connected to the database successfully"
except:
    print "I am unable to connect to the database"