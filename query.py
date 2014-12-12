#!/usr/bin/env python
#Anirudh Agarwala
#Pasha Pourmand
#2014-12-11

import psycopg2
import csv
import os

# obtains the user for the system
user = os.getlogin()

# connects to default data base
conn = psycopg2.connect("dbname='postgres' user='%s' host='localhost'" % user)
cursor = conn.cursor()

# sql_statement = "select count(*) FROM (select distinct house_id, person_id from daytrips) as number_of_people;"
# cursor.execute(sql_statement)
# people_query = cursor.fetchall()

# total_num_people =  people_query[0][0]

# sql_statement = "select total_miles FROM(select house_id, person_id, COALESCE(SUM(trpmiles),0) AS total_miles from daytrips group by house_id, person_id) AS individual_miles;"
# cursor.execute(sql_statement)
# list_of_sums = cursor.fetchall()

# array_sums = []
# for x in list_of_sums:
# 	if x[0] != "None":
# 		array_sums.append(x[0])

# count = 0

# for y in range(5,105,5):
# 	for x in array_sums:
# 		if x < y: 
# 			count += 1
# 	print "at < ", y, "miles there are ", 100.00 * (float(count) / float(total_num_people)),"%"		
# 	count = 0

test = []
for increments in range(5,105,5):
	mpg = "select epatmpg from(vehicle JOIN daytrips ON vehicle.house_id = daytrips.house_id AND vehicle.veh_id = daytrips.vehid AND daytrips.vehid >=1) as vehicle_daytrips where trpmiles < %d;" % increments
	mpg_count = "select count(*) from (select epatmpg from(vehicle JOIN daytrips ON vehicle.house_id = daytrips.house_id AND vehicle.veh_id = daytrips.vehid AND daytrips.vehid >=1) as vehicle_daytrips where trpmiles < %d) as count;" % increments

	cursor.execute(mpg)
	data_mpg = cursor.fetchall()
	cursor.execute(mpg_count)
	data_mp = cursor.fetchall()

	mpg_count_total = data_mp[0][0]

	for blah in data_mpg:
		test.append(blah[0])

	average = 0.0	
	for x in test:
		average += x 

	answer = float(average) / float(mpg_count_total)
	print "Average for day trip less than ", increments, ":", answer
	answer = 0.0
	mpg_count_total = 0
	test = []
