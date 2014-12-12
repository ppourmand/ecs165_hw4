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

sql_statement = "select count(*) FROM (select distinct house_id, person_id from daytrips) as number_of_people;"
cursor.execute(sql_statement)
people_query = cursor.fetchall()

total_num_people =  people_query[0][0]

sql_statement = "select total_miles FROM(select house_id, person_id, COALESCE(SUM(trpmiles),0) AS total_miles from daytrips group by house_id, person_id) AS individual_miles;"
cursor.execute(sql_statement)
list_of_sums = cursor.fetchall()

array_sums = []
for x in list_of_sums:
 	if x[0] != "None":
 		array_sums.append(x[0])

count = 0

print "\nPart 3A"
for y in range(5,105,5):
	for x in array_sums:
		if x < y: 
			count += 1
	print "at < ", y, "miles there are ", 100.00 * (float(count) / float(total_num_people)),"%"		
	count = 0

print "\nPart 3B"
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


print "\nPart 3C"
sql_statement = "select value from eia_co2_transportation_2014 where msn = 'TEACEUS' and yyyymm >= 200803 AND yyyymm <= 200904 AND yyyymm <> 200813;"
cursor.execute(sql_statement)
fetch = cursor.fetchall()

total_transport_co2 = []

for x in fetch:
	total_transport_co2.append(x[0])

household_co2 = 0.0

increments = 200803

for index in range(14):
	total_household_miles = []
	sql_statement = "select trpmiles from( select vehicle.tdaydate, epatmpg, trpmiles from vehicle JOIN daytrips on vehicle.house_id = daytrips.house_id AND vehicle.veh_id = daytrips.vehid AND daytrips.vehid >=1 where vehicle.tdaydate = %d AND trpmiles > 0.0 group by vehicle.tdaydate, epatmpg, trpmiles order by vehicle.tdaydate ASC ) AS total_miles;" % increments
	cursor.execute(sql_statement)
	fetch = cursor.fetchall()
	for a in fetch:
		total_household_miles.append(a[0])

	total_household_mpg = []
	sql_statement = "select epatmpg from( select vehicle.tdaydate, epatmpg, trpmiles from vehicle JOIN daytrips on vehicle.house_id = daytrips.house_id AND vehicle.veh_id = daytrips.vehid AND daytrips.vehid >=1 where vehicle.tdaydate = %d AND trpmiles > 0.0 group by vehicle.tdaydate, epatmpg, trpmiles order by vehicle.tdaydate ASC ) AS total_mpg;" % increments
	cursor.execute(sql_statement)
	fetch = cursor.fetchall()
	for b in fetch:
		total_household_mpg.append(b[0])

	household_count = 0
	sql_statement = "select count(*) FROM( select distinct vehicle.house_id from vehicle JOIN daytrips on vehicle.house_id = daytrips.house_id AND vehicle.veh_id = daytrips.vehid AND daytrips.vehid >=1 where vehicle.tdaydate = %d AND trpmiles > 0.0 ) AS total_households ;" % increments
	cursor.execute(sql_statement)
	fetch = cursor.fetchall()
	household_count = fetch[0][0]

	co2_ratio = 0.0
	co2_ratio = 117538000.00 / float(household_count)

	miles_length = len(total_household_miles)

	gallons_per_month = 0.0
	for y in range(miles_length):
		gallons_per_month += (total_household_miles[y] / total_household_mpg[y])

	household_co2 = float(gallons_per_month) * 0.0000008887
	transport_co2 = total_transport_co2[index]

	print ((household_co2 * co2_ratio) / transport_co2) * 100.00
	household_co2 = 0.0
	transport_co2 = 0.0


	if increments == 200812:
		increments = 200901
	else:
		increments += 1

print "\nPart 3D\n :("






