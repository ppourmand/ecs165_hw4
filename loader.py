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

# Creates the table for mkwh
sql_statement = "CREATE TABLE EIA_MkWh_2014("
sql_statement += "MSN VARCHAR,"
sql_statement += "YYYYMM INT,"
sql_statement += "Value FLOAT,"
sql_statement += "Column_Order VARCHAR,"
sql_statement += "Description VARCHAR,"
sql_statement += "Unit VARCHAR);"
cursor.execute(sql_statement)
conn.commit()

# skips the header in the csv
next(EIA_CO2_Electric)

# First line of the insert
sql_statement = "INSERT INTO eia_co2_electric_2014 VALUES"

# iterates through the csv and breaks up the items and joins them into an INSERT query
for row in EIA_CO2_Electric:
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

