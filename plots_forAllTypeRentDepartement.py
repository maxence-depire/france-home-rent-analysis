import sqlite3
import matplotlib.pyplot as plt

print("START")

BDD = sqlite3.connect("BDD/BDD.sqlite")
cursor = BDD.cursor()
plt.figure(figsize=(20, 3), dpi=100)

print("OPEN BDD END")

cursor.execute('''SELECT DISTINCT dep FROM loyerMaison_2022;''')
loyer_perMaison = {}
for departement in cursor.fetchall() :
    cursor.execute(f'''
                   SELECT AVG(loypredm2) FROM loyerMaison_2022 WHERE dep="{departement[0]}";
                   ''')
    loyer_perMaison.update({departement[0] : cursor.fetchall()[0][0]})

print("SELECT MAISON")

cursor.execute('''SELECT DISTINCT dep FROM loyerAppart_2022;''')
loyer_perAppart = {}
for departement in cursor.fetchall() :
    cursor.execute(f'''
                   SELECT AVG(loypredm2) FROM loyerAppart_2022 WHERE dep="{departement[0]}";
                   ''')
    loyer_perAppart.update({departement[0] : cursor.fetchall()[0][0]})

print("SELECT APPART")

cursor.execute("SELECT DISTINCT dep FROM loyerAppart1ou2P_2022;")
loyer_Appart1ou2P = {}
for departement in cursor.fetchall():
    cursor.execute(f'''
                   SELECT AVG(loypredm2) FROM loyerAppart1ou2P_2022 WHERE dep="{departement[0]}";
                   ''')
    loyer_Appart1ou2P.update({departement[0] : cursor.fetchall()[0][0]})

print("SELECT APPART 1 ou 2")

cursor.execute("SELECT DISTINCT dep FROM loyerAppart_3piece_2022;")
loyer_Appart3P = {}
for departement in cursor.fetchall():
    cursor.execute(f'''
                   SELECT AVG(loypredm2) FROM loyerAppart_3piece_2022 WHERE dep="{departement[0]}";
                   ''')
    loyer_Appart3P.update({departement[0] : cursor.fetchall()[0][0]})

print("SELECT APPART 3")

departement_list = list(loyer_perMaison.keys())
res_departement = []
res_loyer = []
for departement in departement_list :
    value = (
        int(loyer_perMaison[departement])
        + int(loyer_perAppart[departement])
        + int(loyer_Appart1ou2P[departement])
        + int(loyer_Appart3P[departement])
        ) / 4
    res_departement.append(departement)
    res_loyer.append(value)
    
print("GET AVERAGE")

BDD.close()
plt.scatter(res_departement, res_loyer)
plt.show()