#!/usr/bin/env python
#Anirudh Agarwala
#Pasha Pourmand
#2014-12-6

import psycopg2
import csv

# tries to connect to data base
try:
    conn = psycopg2.connect("dbname='test' user='ppourmand' host='localhost'")
    print "I connected to the database successfully"
except:
    print "I am unable to connect to the database"

# open the csv file and read it in
f = open('EIA_CO2_Electric_2014.csv')
csv_f = csv.reader(f)

# prints outs the csv to standard out
for row in csv_f:
	print row