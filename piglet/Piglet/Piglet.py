from requests import get
from requests.exceptions import (HTTPError, MissingSchema, ConnectionError)
from bs4 import BeautifulSoup
"""
commends of imports
"""


class piglet(object):
    """docstring for piglet.
        base de los scrapies"""

    def __init__(self):
        print('__init__.piglet')
        self.http = ''
        self.code = ''
        self.connectionSucess = False
        self.error = None

    def addUrl(self, url):
        try:
            self.html = get(url)
            self.code = self.html.status_code

        except (ConnectionError, MissingSchema, HTTPError) as error:
            self.error = error

    def confirmEnabled(self):
        if self.code == 200:
            self.connectionSucess = True
        else:
            self.connectionSucess = False

    def returnHtml(self):
        """Short summary.

        Returns
        -------
        type
            un str para ser sopeado.

        """
        if self.connectionSucess:
            return self.html.text
        else:
            return self.error


class sopero(object):
    """docstring for sopero.
        requiere de bs4
        """

    def __init__(self):
        print('__init__.sopero')
        self.domain = None
        self.depurado = False
        self.listaDepurada = []
        self.specialChars = ['=', '?', '/']
        self.listaSinDepurar = []

    def getAurl(self, html):
        BigSopa = BeautifulSoup(html, 'html.parser')

        for url in BigSopa.find_all('a'):
            if url is None:
                continue
            elif url == '':
                continue
            elif len(url) < 5:
                continue
            else:
                self.listaDepurada.append(url.get('href'))
        # conocer el estado de la lista Depurado o no
        self.depurado = True

        return self.listaDepurada

    def getListByTxt(self, listOfUrls):
        self.listaSinDepurar = listOfUrls

    def addDomain(self, domainName):
        self.domain = domainName

    # def getDomainFromList(self):
        # listaOfDomain = []
        # listaOfUrls = self.listaDepurada
        # if len(listaOfUrls) > 0:
            # leght = len(listOfUrls)
        # else:
            # 'erroor'
            # break
        # for range(leght):
            # if listaOfUrls[i][]


    def depurarList(self):
        for url in self.listaSinDepurar:
            if url is None:
                continue
            elif url == '':
                continue
            elif len(url) < 5:
                continue
            else:
                self.listaDepurada.append(url)
        # conocer el estado de la lista Depurado o no
        self.depurado = True

    def getDomain(self):
        if len(self.listaPrima) == 0:
            self.domain = 'list dont ready'
        else:
            self.domain = self.listaPrima[0]
