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

# open the co2 electric csv file and read it in
EIA_CO2_Electric = csv.reader(open('EIA_CO2_Electric_2014.csv'))

# open the co2 transportation csv file and read it in
EIA_CO2_Transportation = csv.reader(open('EIA_CO2_Transportation_2014.csv'))

# open the MkWh csv file and read it in
EIA_MkWh = csv.reader(open('EIA_MkWh_2014.csv'))


# prints outs the csv to standard out
for row in EIA_CO2_Electric:
	print row