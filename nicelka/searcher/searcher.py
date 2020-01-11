from abc import abstractmethod
from os import path
from datetime import datetime


# TODO: move all files activities to separate class
# TODO: handle multiple result pages in KrkgwPage
# TODO: write functional tests
# TODO: google_page should return more then max 3 results
# TODO: narrow all Exceptions into more specific classes
# TODO: add unit tests
# TODO: store results in custom classes
# TODO: use REST API instead of Selenium
# TODO: add logger
# TODO: add AI to evaluate results found
# TODO: add docs, type hints etc.


class Searcher:
    _FILE_ENCODING = 'utf8'

    def __init__(self,
                 data_dir_path='data',
                 results_dir_path='results',
                 skip_indirect_matches=True,
                 skip_duplicates=True):
        self._engine = None
        self._data_dir_path = data_dir_path
        self._cities_file = self._assemble_data_file_path('cities.txt')
        self._cities = self._get_cities()

        self._skip_indirect_matches = skip_indirect_matches
        self._skip_duplicates = skip_duplicates

        self._results = []
        self._results_count = 0
        self._results_dir_path = results_dir_path
        self._results_file_path = None

    @property
    def engine_name(self):
        return None if self._engine is None else self._engine.name

    @property
    def results_file_path(self):
        return self._results_file_path

    @abstractmethod
    def search(self):
        self._raise_not_implemented_error('search')

    def _raise_not_implemented_error(self, method_name):
        raise NotImplementedError('{} class missing required implementation of method: {}'.format(self.__class__.__name__, method_name))

    def _assemble_data_file_path(self, file_name):
        return path.join(self._data_dir_path, file_name)

    def _get_cities(self):
        with open(self._cities_file, encoding=self._FILE_ENCODING) as file:
            return [city.strip() for city in file.readlines()]

    def _assemble_result_file_path(self):
        return path.join(self._results_dir_path, '{}_{}.txt'.format(datetime.now(), self.engine_name).replace(' ', '_').replace(':', '.'))

    def _add_city_header(self, city):
        self._results.append('=' * 70 + '\n')
        self._results.append(city + '\n\n')

    @staticmethod
    def _get_zip_code_prefix(city):
        return city.split('-')[0] + '-'

    @staticmethod
    def _get_city_name(city):
        city_split = city.split(' ', maxsplit=1)
        return city_split[1] if len(city_split) >= 2 else city

    @staticmethod
    def _is_indirect_match(result, city_name, zip_code_prefix):
        return city_name.lower() not in result.lower() or zip_code_prefix not in result.lower()

    def _is_duplicate(self, result):
        return result + '\n' in self._results

    def _add_results(self, *args, **kwargs):
        self._raise_not_implemented_error('_add_results')

    def _add_results_count(self):
        self._results.append('Liczba znalezionych adresow: {}'.format(self._results_count))

    def _save_results(self):
        try:
            with open(path.join(self._results_file_path), mode='w', encoding=self._FILE_ENCODING) as file:
                file.writelines(self._results)
        except Exception:
            pass
