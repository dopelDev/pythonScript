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
        self.listaPrima = []
        self.specialChars = ['=', '?', '/']

    def getAurl(self, html):
        BigSopa = BeautifulSoup(html, 'html.parser')

        for url in BigSopa.find_all('a'):
            if url is None:
                continue
            elif url == '':
                continue
            elif len(url) < 2:
                continue
            else:
                self.listaPrima.append(url.get('href'))

        return self.listaPrima

    def getList(self, listOfUrls):
        pass

    def getDomain(self):
        if len(self.listaPrima) == 0:
            self.domain = 'list dont ready'
        else:
            self.domain = self.listaPrima[0]
