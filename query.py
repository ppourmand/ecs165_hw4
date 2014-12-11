#!/usr/bin/env python
#Anirudh Agarwala
#Pasha Pourmand
#2014-12-10

import psycopg2
import csv
import os

# obtains the user for the system
user = os.getlogin()

# connects to default data base
conn = psycopg2.connect("dbname='postgres' user='%s' host='localhost'" % user)
cursor = conn.cursor()