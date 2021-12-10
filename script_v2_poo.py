import psycopg2
import csv

user="postgres"
password="postgree"
host="127.0.0.1"
port="5432"
database="P12"

class BienImo():
    def __init__(self,id=None, id_lot=None, nb_piece=None,
    typologie=None, prix_tva_reduite=None, prix_tva_normale=None,
    prix_HT=None, prix_m2_HT=None, prix_m2_TTC=None, orientation=None,
    exterieur=None, balcony=None, garden=None, parking=None, ville=None,
    departement=None, date_fin_programme=None, adresse_entiere=None, date_extraction=None):

        self.id = id
        self.id_lot =id_lot
        self.nb_piece = nb_piece
        self.typologie = typologie
        self.prix_tva_reduite= prix_tva_reduite
        self.prix_tva_normale = prix_tva_normale
        self.prix_HT = prix_HT
        self.prix_m2_HT = prix_m2_HT
        self.prix_m2_TTC = prix_m2_TTC
        self.orientation= orientation
        self.exterieur= exterieur
        self.balcony= balcony
        self.garden= garden
        self.parking= parking
        self.ville= ville
        self.departement= departement
        self.date_fin_programme= date_fin_programme
        self.adresse_entiere= adresse_entiere
        self.date_extraction= date_extraction

        temp = self.id_lot.split('_')
        self.surface = temp.pop(0)
        self.nom_promoteur = temp.pop(-1)
        self.nom_programme = temp.pop(-1)
        self.etage = '_'.join(temp).replace('__','-').replace('_','')


    def to_db(self):        
        query = f"""INSERT INTO promoteur (id, id_lot, nb_piece, typologie,
        prix_tva_reduite, prix_tva_normale, prix_HT,
        prix_m2_HT, prix_m2_TTC, orientation,
        exterieur, balcony, garden, parking,
        ville, departement, date_fin_programme,
        adresse_entiere, date_extraction, surface,
        etage, nom_programme, nom_promoteur)
        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        vars = (self.id, self.id_lot, self.nb_piece, self.typologie,
        self.prix_tva_reduite, self.prix_tva_normale, self.prix_HT,
        self.prix_m2_HT, self.prix_m2_TTC, self.orientation,
        self.exterieur, self.balcony, self.garden, self.parking,
        self.ville, self.departement, self.date_fin_programme,
        self.adresse_entiere, self.date_extraction, self.surface,
        self.etage, self.nom_programme, self.nom_promoteur)

        return cursor.execute(query,vars)

connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)

cursor = connection.cursor()
cursor.execute(open("init_db.sql", "r").read())
cursor.execute(open("add_columns.sql", "r").read())

# test = BienImo(44,"63_1__1_L'alcve_Bouygues")
# print(test.__dict__)
# test.to_db()

list_bien_objects = []

f = open(r'Promoteur_imo.csv', 'r')
next(f)
reader = csv.reader(f, delimiter = ';')
for r in reader:
    for i in range(len(r)):
        if r[i] =='':
            r[i]= None
    list_bien_objects.append(BienImo(r[0], r[1], r[2], r[3], r[4],
    r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13],
    r[14], r[15], r[16], r[17], r[18]))

for item in list_bien_objects:
    item.to_db()

if (connection):
    connection.commit()
    cursor.close()
    connection.close()
print("PostgreSQL connection is closed")
