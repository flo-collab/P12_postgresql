import psycopg2
import os.path, time

user="postgres"
password="postgree"
host="127.0.0.1"
port="5432"
database="P12"


def add_magic(func):
    def magic(*args):
        print('Tentative de connection...')
        connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)
        cursor = connection.cursor()  
        
        func(cursor,*args)

        if (connection):
            connection.commit()
            cursor.close()
            connection.close()
            print("\n PostgreSQL connection is closed\n")
    return magic

@add_magic
def make_stuff(cursor,query):
    cursor.execute(query)
    # print(cursor.fetchall())
    for r in cursor.fetchall():
        print(r)

make_stuff("""SELECT * FROM promoteur WHERE balcony = 'True'""")