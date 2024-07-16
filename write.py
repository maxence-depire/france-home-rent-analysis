import sqlite3
import csv
import time

BDD = sqlite3.connect("BDD.sqlite")
cursor = BDD.cursor()


cursor.execute('''DROP TABLE IF EXISTS loyerMaison_2022;''')


cursor.execute('''
               CREATE TABLE loyerMaison_2022
               (
                    id INTEGER PRIMARY KEY,
                    id_zone INT,
                    insee_c INT,
                    libgeo TEXT,
                    epci INT,
                    dep TEXT,
                    reg TEXT,
                    loypredm2 INT,
                    lwr_IPm2 INT,
                    upr_IPm2 INT,
                    typpred TEXT,
                    nbobs_com INT,
                    nbobs_mail INT,
                    R2_adj INT
               );
               ''')
BDD.commit()


with open("data/loyer-maison-2022.csv", newline='') as csv_maison:
    spamreader = csv.reader(csv_maison, delimiter='%', quotechar='|')

    header = True
    for row in spamreader :
        if not header:
            value = row[0]
            value = value.replace('"', "").split(";")
            print(value)

            cursor.execute(f'''
                           INSERT INTO loyerMaison_2022
                           (
                                id_zone,
                                insee_c,
                                libgeo,
                                epci,
                                dep,
                                reg,
                                loypredm2,
                                lwr_IPm2,
                                upr_IPm2,
                                typpred,
                                nbobs_com,
                                nbobs_mail,
                                R2_adj
                           )
                           VALUES
                           (
                            {value[0]},
                            {value[1]},
                            "{value[2]}",
                            {value[3] if value[3] != "ZZZZZZZZZ" else 0},
                            "{value[4]}",
                            "{value[5]}",
                            {value[6].split(",")[0]},
                            {value[7].split(",")[0]},
                            {value[8].split(",")[0]},
                            "{value[9]}",
                            {value[10]},
                            {value[11]},
                            {value[12].split(",")[0]}
                           );
                           ''')
            BDD.commit()
        else:
            header = False


BDD.close()