#developed by VinayakMaini
#use database name is yours 

import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')