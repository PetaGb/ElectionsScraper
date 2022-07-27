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


def vysledky_1(url):

    ods = []
    rn = []
    cos = []
    cssd = []
    rc = []
    starostove = []
    kscm = []
    zeleni = []
    rozumni = []
    svobodni = []
    blok = []
    oda = []
    pirati = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:

        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        vysledek = muni_soup.find_all("td", {"headers": "t1sa2 t1sb3"})

        ods.append(vysledek[0].string)
        rn.append(vysledek[1].string)
        cos.append(vysledek[2].string)
        cssd.append(vysledek[3].string)
        rc.append(vysledek[4].string)
        starostove.append(vysledek[5].string)
        kscm.append(vysledek[6].string)
        zeleni.append(vysledek[7].string)
        rozumni.append(vysledek[8].string)
        svobodni.append(vysledek[9].string)
        blok.append(vysledek[10].string)
        oda.append(vysledek[11].string)
        pirati.append(vysledek[12].string)

    return ods, rn, cos, cssd, rc, starostove, kscm, zeleni, rozumni, svobodni, blok, oda, pirati


def vysledky_2(url):

    referendum = []
    top = []
    ano = []
    dv = []
    spr = []
    kdu = []
    csns = []
    realiste = []
    sportovci = []
    dsss = []
    spd = []
    spo = []
    ns = []

    res = requests.get(url)
    election_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = election_soup.select('td[class="cislo"] a')

    for elem in elems:

        url_to_open = "https://volby.cz/pls/ps2017nss/" + elem.get("href")
        muni_res = requests.get(url_to_open)
        muni_soup = bs4.BeautifulSoup(muni_res.text, 'html.parser')
        vysledek = muni_soup.find_all("td", {"headers": "t2sa2 t2sb3"})

        referendum.append(vysledek[0].string)
        top.append(vysledek[1].string)
        ano.append(vysledek[2].string)
        dv.append(vysledek[3].string)
        spr.append(vysledek[4].string)
        kdu.append(vysledek[5].string)
        csns.append(vysledek[6].string)
        realiste.append(vysledek[7].string)
        sportovci.append(vysledek[8].string)
        dsss.append(vysledek[9].string)
        spd.append(vysledek[10].string)
        spo.append(vysledek[11].string)
        ns.append(vysledek[12].string)

    return referendum, top, ano, dv, spr, kdu, csns, realiste, sportovci, dsss, spd, spo, ns
