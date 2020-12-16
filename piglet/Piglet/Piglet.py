from requests import get
from requests.exceptions import (HTTPError, MissingSchema, ConnectionError)


class piglet(object):
    """docstring for piglet.
        base de los scrapies"""

    def __init__(self):
        print('__init__.piglet')
        self.http = ''
        self.code = ''
        self.connectionSucess = False

    def addUrl(self, url):
        try:
            self.html = get(url)
            self.code = self.html.status_code

        except (ConnectionError, MissingSchema, HTTPError) as error:
            print(error)

    def confirmEnabled(self):
        if self.code == 200:
            self.connectionSucess = True
        else:
            self.connectionSucess = False


class sopeando(piglet):
    """docstring for sopeando."""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg
