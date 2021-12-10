import psycopg2

user="postgres"
password="postgree"
host="127.0.0.1"
port="5432"
database="P12"

connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)

cursor = connection.cursor()

cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

cursor.execute(open("init_db.sql", "r").read())

f = open(r'Promoteur_imo.csv', 'r')
next(f)
cursor.copy_from(f, 'promoteur', sep=';',null='')
f.close()
connection.commit()
'''
query = """select * from promoteur"""
cursor.execute(query)
# print(cursor.fetchall())
for r in cursor.fetchall():
    print(r)
'''
query = """select id_lot from promoteur"""
cursor.execute(query)
list_id_lot = [r[0].split('_') for r in cursor.fetchall()]

list_surface = []
list_etage = []
list_promoteur = []
list_nomprogramme = []
 
for stuff in list_id_lot:
    list_surface.append(stuff.pop(0))
    list_promoteur.append(stuff.pop(-1))
    list_nomprogramme.append(stuff.pop(-1))
    list_etage.append('_'.join(stuff).replace('__','-').replace('_',''))

cursor.execute(open("add_columns.sql", "r").read())

for i in range(len(list_id_lot)):
    cursor.execute("""UPDATE promoteur 
    SET surface=%s, etage=%s, nom_programme=%s, nom_promoteur=%s 
    WHERE id=%s""",
    (list_surface[i],list_etage[i],list_nomprogramme[i],list_promoteur[i],i))

query = """SELECT * FROM promoteur WHERE balcony = 'True'"""
outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
balcony = 'only_balcony.csv'
with open(balcony, 'w') as f:
    cursor.copy_expert(outputquery, f)

import os.path, time
print(f"Derniere modification du fichier {balcony} : %s" % time.ctime(os.path.getmtime(balcony)))

if (connection):
    connection.commit()
    cursor.close()
    connection.close()
print(" PostgreSQL connection is closed\n")



