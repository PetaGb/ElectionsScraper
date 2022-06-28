"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Peter Gbelec
email: peter.gbelec@gmail.com
discord: PeťaG#4695
"""


import requests
import bs4
import csv
from sys import *

script, url, file = argv

if len(argv) != 3:
    print("Please follow these instructions: insert name of the script ('script.py'), url address "
          "('https://volby.cz...') and name of the file ('file.csv'). \nTerminating...")
    quit()

else:
    pass


res = requests.get(url)
election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = election_soup.select('td[class="cislo"] a')
name_elems = election_soup.select('td[class="overflow_name"]')


def obecni_cislo():

    list_cisel = []
    for elem in elems:
        cisla = elem.text
        list_cisel.append(cisla)

    return list_cisel


def nazev_obce():

    list_obci = []
    for name_elem in name_elems:
        obce = name_elem.text
        list_obci.append(obce)

    return list_obci


def seznam_volicu():

    list_seznamu = []
    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        seznamy = muni_soup.find('td', {'headers': 'sa2'}).text
        list_seznamu.append(seznamy)

    return list_seznamu


def pocet_obalek():

    list_obalek = []
    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        vydane_obalky = muni_soup.find('td', {'headers': 'sa3'}).text
        list_obalek.append(vydane_obalky)

    return list_obalek


def platne_hlasy():

    seznam_hlasu = []
    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        hlas = muni_soup.find('td', {'headers': 'sa6'}).text
        seznam_hlasu.append(hlas)

    return seznam_hlasu


def politicke_strany():

    seznam_stran = []
    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        pol_strany = muni_soup.find_all('td', {'class': 'overflow_name'})

        ciste_strany = []
        for strana in pol_strany:
            cista_strana = strana.text
            ciste_strany.append(cista_strana)

        stringed_seznam = ', '.join(ciste_strany)
        seznam_stran.append(stringed_seznam)

    return seznam_stran


nazev = nazev_obce()
cislo = obecni_cislo()
volici = seznam_volicu()
obalky = pocet_obalek()
hlasy = platne_hlasy()
strany = politicke_strany()


def csv_maker():

    with open(file, "a", newline="", encoding="ISO8859-2") as csv_soubor:
        zahlavi = ["ČÍSLO", "OBEC", "POČET VOLIČŮ", "VYDANÉ OBÁLKY", "PLATNÉ HLASY", "KANDIDUJÍCÍ STRANY"]
        writer = csv.DictWriter(csv_soubor, delimiter=",", fieldnames=zahlavi)
        writer.writeheader()

        for c, n, v, o, h, s in zip(cislo, nazev, volici, obalky, hlasy, strany):
            writer.writerow(
                {

                    "ČÍSLO": c,
                    "OBEC": n,
                    "POČET VOLIČŮ": v,
                    "VYDANÉ OBÁLKY": o,
                    "PLATNÉ HLASY": h,
                    "KANDIDUJÍCÍ STRANY": s

                }
            )


csv_maker()