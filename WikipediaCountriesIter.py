import json

FILE_NAME = 'countries.json'


class WikipediaCountriesIter:
    def __init__(self):
        self.countries = self._get_countries(FILE_NAME)
        self.country_iter = iter(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.country_iter)
        url_country = 'https://en.wikipedia.org/wiki/' + country_name.replace(' ', '_')
        return country_name + ' - ' + url_country

    def _get_countries(self, path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            result = []
            for info in data:
                country_name = info['name']['common']
                result.append(country_name)
        return result