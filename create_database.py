import psycopg2
connection = psycopg2.connect(host='localhost', user='postgres',password='postgres', port="5432")
connection.autocommit = True
cursor = connection.cursor()
cursor.execute('CREATE DATABASE report_db')

import psycopg2
connection = psycopg2.connect(dbname='report_db', host='localhost', user='postgres', password='postgres', port="5432")
cursor = connection.cursor()
connection.autocommit = True
cursor.execute('CREATE EXTENSION postgis')
connection.close()
