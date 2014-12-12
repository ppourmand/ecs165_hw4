#!/usr/bin/env python
#Anirudh Agarwala
#Pasha Pourmand
#2014-12-8

import psycopg2
import csv
import os

# obtains the user for the system
user = os.getlogin()

# connects to default data base
conn = psycopg2.connect("dbname='postgres' user='%s' host='localhost'" % user)
cursor = conn.cursor()

# open the co2 electric csv file and read it in
EIA_CO2_Electric = csv.reader(open('EIA_CO2_Electric_2014.csv'))

# open the co2 transportation csv file and read it in
EIA_CO2_Transportation = csv.reader(open('EIA_CO2_Transportation_2014.csv'))

# open the MkWh csv file and read it in
EIA_MkWh = csv.reader(open('EIA_MkWh_2014.csv'))

# opens the day trip csv
day_trip_csv = csv.reader(open('DAYV2PUB.csv'))

# opens the household csv
hh_csv = csv.reader(open('HHV2PUB.csv'))

# opens the person csv
person_csv = csv.reader(open('PERV2PUB.csv'))

# opens the vehicle csv
vehicle_csv = csv.reader(open('VEHV2PUB.csv'))

# Creates the table for EIA_CO2 electric
sql_statement = "CREATE TABLE EIA_CO2_Electric_2014("
sql_statement += "MSN VARCHAR,"
sql_statement += "YYYYMM INT,"
sql_statement += "Value FLOAT,"
sql_statement += "Column_Order VARCHAR,"
sql_statement += "Description VARCHAR,"
sql_statement += "Unit VARCHAR);"
cursor.execute(sql_statement)
conn.commit()

# Creates the table for eia co2 transportation
sql_statement = "CREATE TABLE EIA_CO2_Transportation_2014("
sql_statement += "MSN VARCHAR,"
sql_statement += "YYYYMM INT,"
sql_statement += "Value FLOAT,"
sql_statement += "Column_Order VARCHAR,"
sql_statement += "Description VARCHAR,"
sql_statement += "Unit VARCHAR);"
cursor.execute(sql_statement)
conn.commit()

# # Creates the table for mkwh
sql_statement = "CREATE TABLE EIA_MkWh_2014("
sql_statement += "MSN VARCHAR,"
sql_statement += "YYYYMM INT,"
sql_statement += "Value FLOAT,"
sql_statement += "Column_Order VARCHAR,"
sql_statement += "Description VARCHAR,"
sql_statement += "Unit VARCHAR);"
cursor.execute(sql_statement)
conn.commit()

# creates table for day trip data
sql_statement = "CREATE TABLE daytrips("
sql_statement += "house_id FLOAT,"
sql_statement += "person_id FLOAT,"
sql_statement += "tdcase_id FLOAT,"
sql_statement += "hhvehcnt FLOAT,"
sql_statement += "strtttime FLOAT,"
sql_statement += "travday FLOAT,"
sql_statement += "vehid FLOAT,"
sql_statement += "tdtrpnum FLOAT,"
sql_statement += "tdaydate FLOAT,"
sql_statement += "trpmiles FLOAT,"
sql_statement += "trvl_min FLOAT);"
cursor.execute(sql_statement)
conn.commit()

# # creates a table for household data
sql_statement = "CREATE TABLE household("
sql_statement += "house_id INT,"
sql_statement += "hhvehcnt INT,"
sql_statement += "travday INT,"
sql_statement += "tdaydate INT);"
cursor.execute(sql_statement)
conn.commit()

# creates a table for person data
sql_statement = "CREATE TABLE person("
sql_statement += "house_id INT,"
sql_statement += "person_id INT,"
sql_statement += "yearmile INT,"
sql_statement += "tdaydate INT);"
cursor.execute(sql_statement)
conn.commit()

# creates a table for vehicle data
sql_statement = "CREATE TABLE vehicle("
sql_statement += "house_id INT,"
sql_statement += "veh_id INT,"
sql_statement += "hybrid INT,"
sql_statement += "tdaydate INT,"
sql_statement += "person_id INT,"
sql_statement += "annmiles INT,"
sql_statement += "epatmpg FLOAT);"
cursor.execute(sql_statement)
conn.commit()

#==============================================================================================================================
#  EIA DATA
#==============================================================================================================================
# skips the header in the csv
next(EIA_CO2_Electric)

# First line of the insert
sql_statement = "INSERT INTO eia_co2_electric_2014 VALUES"

# iterates through the csv and breaks up the items and joins them into an INSERT query
for row in EIA_CO2_Electric:
   if row[2] == 'Not Available':
        sql_statement += "('%s', %d, %s, '%s', '%s', '%s')," % (row[0], int(row[1]), "NULL", row[3], row[4], row[5])

   else:
   		sql_statement += "('%s', %d, %f, '%s', '%s', '%s')," % (row[0], int(row[1]), float(row[2]), row[3], row[4], row[5])

# Removes the final comma and replaces with a semicolon
sql_statement = sql_statement[:-1]
sql_statement += ";"

# Executes the INSERT query for table 1
cursor.execute(sql_statement)
conn.commit()

# skips the header in the next csv
next(EIA_CO2_Transportation)

# First line of the insert
sql_statement = "INSERT INTO eia_co2_transportation_2014 VALUES"

# iterates through the csv and breaks up the items and joins them into an INSERT query
for row in EIA_CO2_Transportation:
   if row[2] == 'Not Available':
        sql_statement += "('%s', %d, %s, '%s', '%s', '%s')," % (row[0], int(row[1]), "NULL", row[3], row[4], row[5])

   else:
   		sql_statement += "('%s', %d, %f, '%s', '%s', '%s')," % (row[0], int(row[1]), float(row[2]), row[3], row[4], row[5])

# Removes the final comma and replaces with a semicolon
sql_statement = sql_statement[:-1]
sql_statement += ";"   

# Executes the INSERT query for table 2
cursor.execute(sql_statement)
conn.commit()

# skips the header in the next csv
next(EIA_MkWh)

# First line of the insert
sql_statement = "INSERT INTO eia_mkwh_2014 VALUES"

for row in EIA_MkWh:
    if row[2] == 'Not Available':
        sql_statement += "('%s', %d, %s, '%s', '%s', '%s')," % (row[0], int(row[1]), "NULL", row[3], row[4], row[5])

    else:
        sql_statement += "('%s', %d, %f, '%s', '%s', '%s')," % (row[0], int(row[1]), float(row[2]), row[3], row[4], row[5])

# Removes the final comma and replaces with a semicolon
sql_statement = sql_statement[:-1]
sql_statement += ";"

# Executes the INSERT query for table 1
cursor.execute(sql_statement)
conn.commit();

#==============================================================================================================================
#  NHTS DATA
#==============================================================================================================================

# skips the header
next(day_trip_csv)

# first line of insert
sql_statement = "INSERT INTO daytrips VALUES"
count = 0
for row in day_trip_csv:
	sql_statement += "(%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)," % (float(row[0]), float(row[1]), float(row[19]), float(row[28]), float(row[57]), float(row[64]), float(row[83]), float(row[91]), float(row[93]), float(row[94]), float(row[75]))
	count += 1
	if count % 10000 == 0:
		sql_statement = sql_statement[:-1]
		sql_statement += ";"
		cursor.execute(sql_statement)
		conn.commit()
		sql_statement = "INSERT INTO daytrips VALUES"

sql_statement = sql_statement[:-1]
sql_statement += ";"

cursor.execute(sql_statement)
conn.commit()

# skips the header
next(hh_csv)

# first line of insert
sql_statement = "INSERT INTO household VALUES"
count = 0
for row in hh_csv:
	sql_statement += "(%d, %d, %d, %d)," % (int(row[0]), int(row[15]), int(row[24]), int(row[29]))
	count += 1
	if count %10000 == 0:
		sql_statement = sql_statement[:-1]
 		sql_statement += ";"
 		cursor.execute(sql_statement)
 		conn.commit()
 		sql_statement = "INSERT INTO daytrips VALUES"
sql_statement = sql_statement[:-1]
sql_statement += ";"

cursor.execute(sql_statement)
conn.commit()

next(person_csv)

sql_statement = "INSERT INTO person VALUES"
count = 0
for row in person_csv:
	sql_statement += "(%d, %d, %d, %d)," % (int(row[0]), int(row[1]), int(row[100]), int(row[104]))
	if count %10000 == 0:
		sql_statement = sql_statement[:-1]
		sql_statement += ";"
		cursor.execute(sql_statement)
		conn.commit()
		sql_statement = "INSERT INTO person VALUES"

# # Removes the last character in the sql statement which is a , from the loop
sql_statement = sql_statement[:-1]

# # Checks to see if the last line isnt just an empty line
if sql_statement != "INSERT INTO person VALUE":
	sql_statement += ";"
	cursor.execute(sql_statement)
	conn.commit()

next(vehicle_csv)

sql_statement = "INSERT INTO vehicle VALUES"
count = 0
for row in vehicle_csv:
	sql_statement += "(%d, %d, %d, %d, %d, %f, %f)," % (int(row[0]), int(row[2]), int(row[14]), int(row[30]), int(row[32]), float(row[38]), float(row[55]))
	if count %10000 == 0:
		sql_statement = sql_statement[:-1]
		sql_statement += ";"
		cursor.execute(sql_statement)
		conn.commit()
		sql_statement = "INSERT INTO vehicle VALUES"

# Removes the last character in the sql statement which is a , from the loop
sql_statement = sql_statement[:-1]

# Checks to see if the last line isnt just an empty line
if sql_statement != "INSERT INTO vehicle VALUE":
	sql_statement += ";"
	cursor.execute(sql_statement)
	conn.commit()
