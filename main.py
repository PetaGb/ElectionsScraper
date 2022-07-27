"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Peter Gbelec
email: peter.gbelec@gmail.com
discord: PeťaG#4695
"""


from sys import *
from funcs import *
import csv
import os

script, url, file = argv


def main(name):

    if len(argv) != 3:
        print("Please follow these instructions: insert name of the script ('script.py'), url address ",
              "('https://volby.cz...') and name of the file ('file.csv'). \nTerminating...")
        quit()

    else:
        obce = nazev_obce(url)
        cislo = obecni_cislo(url)
        volici = seznam_volicu(url)
        obalky = pocet_obalek(url)
        hlasy = platne_hlasy(url)
        strany_1 = vysledky_1(url)
        strany_2 = vysledky_2(url)
        mena = jmena_stran(url)

        data = zip(cislo, obce, volici, obalky, hlasy, strany_1[0], strany_1[1], strany_1[2], strany_1[3], strany_1[4],
                   strany_1[5], strany_1[6], strany_1[7], strany_1[8], strany_1[9], strany_1[10], strany_1[11],
                   strany_1[12], strany_2[0], strany_2[1], strany_2[2], strany_2[3], strany_2[4], strany_2[5],
                   strany_2[6], strany_2[7], strany_2[8], strany_2[9], strany_2[10], strany_2[11], strany_2[12])

        if name in os.listdir():

            with open(file, "a", newline="", encoding="ISO8859-2") as csv_soubor:
                writer = csv.writer(csv_soubor)
                for row in data:
                    writer.writerow(row)

        else:
            with open(file, "w", newline="", encoding="ISO8859-2") as csv_soubor:
                zahlavi = ["ČÍSLO", "OBEC", "POČET VOLIČŮ", "VYDANÉ OBÁLKY", "PLATNÉ HLASY"] + mena
                writer = csv.writer(csv_soubor)
                writer.writerow(zahlavi)
                for row in data:
                    writer.writerow(row)


if __name__ == "__main__":
    main(file)
