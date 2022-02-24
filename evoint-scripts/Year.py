from collections import OrderedDict

years = OrderedDict()


class Year:
    def __init__(self, year, titel='', text='', extra=''):
        self.year = str(year)
        self.titel = titel
        self.text = text
        self.extra = extra

        self.add_to_years()

    def add_to_years(self):
        years[self.year] = self
