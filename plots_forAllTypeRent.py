import sqlite3
import matplotlib.pyplot as plt

BDD = sqlite3.connect("BDD/BDD.sqlite")
cursor = BDD.cursor()

cursor.execute('''
               SELECT AVG(loypredm2) FROM loyerMaison_2022
               ''')
maison_PriceAVG = cursor.fetchall()[0][0]

cursor.execute('''
               SELECT AVG(loypredm2) FROM loyerAppart_2022
               ''')
appart_PriceAVG = cursor.fetchall()[0][0]

cursor.execute('''
               SELECT AVG(loypredm2) FROM loyerAppart1ou2P_2022
               ''')
appart1ou2P_PriceAVG = cursor.fetchall()[0][0]

cursor.execute('''
               SELECT AVG(loypredm2) FROM loyerAppart_3piece_2022
               ''')
appart3P_PriceAVG = cursor.fetchall()[0][0]


BDD.close()


names = [
    'Maison',
    'Appartement',
    'Appartement\n1, 2 pièce',
    'Appartement\n3 pièce'
    ]
values = [
    maison_PriceAVG,
    appart_PriceAVG,
    appart1ou2P_PriceAVG,
    appart3P_PriceAVG
    ]

plt.bar(names, values)
plt.title("Loyer logement France 2022.")
plt.show()