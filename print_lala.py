import time
import psycopg2
import os.path, time

user="postgres"
password="postgree"
host="127.0.0.1"
port="5432"
database="P12"

try:
    connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)

    if (connection):
        connection.commit()
        cursor.close()
        connection.close()
    print(" PostgreSQL connection is closed\n")

except:
    print('looooupééééééé !!\n'*20)




for i in range (2000):
    print('lala')
    time.sleep(5)