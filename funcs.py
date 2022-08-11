import requests
import bs4


def nazev_obce(url):

    list_obci = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    name_elems = election_soup.select('td[class="overflow_name"]')

    for name in name_elems:
        obce = name.text
        list_obci.append(obce)

    return list_obci


def obecni_cislo(url):

    list_cisel = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:
        cisla = elem.text
        list_cisel.append(cisla)

    return list_cisel


def seznam_volicu(url):

    list_seznamu = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        seznamy = muni_soup.find('td', {'headers': 'sa2'}).text
        list_seznamu.append(seznamy)

    return list_seznamu


def pocet_obalek(url):

    list_obalek = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        vydane_obalky = muni_soup.find('td', {'headers': 'sa3'}).text
        list_obalek.append(vydane_obalky)

    return list_obalek


def platne_hlasy(url):

    seznam_hlasu = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        hlas = muni_soup.find('td', {'headers': 'sa6'}).text
        seznam_hlasu.append(hlas)

    return seznam_hlasu


def jmena_stran(url):

    nazvy = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')[0]

    url_to_open = "https://volby.cz/pls/ps2017nss/" + elems.get("href")
    muni_res = requests.get(url_to_open)
    muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
    for party in muni_soup.find_all("td", {"class": "overflow_name"}):
        nazvy.append(party.string)

    return nazvy


def vysledky(url):

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    party_list = []

    for elem in elems:
        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        tables = muni_soup.find_all("div", {"class": "t2_470"})

        party = []
        for table in tables:
            cislice = table.select('td[class="cislo"]')[1::3]

            for cislo in cislice:
                stringed_cislo = cislo.string
                party.append(stringed_cislo)

        party_list.append(party)

    reversed_lists = list(map(list, zip(*party_list)))

    return reversed_lists
