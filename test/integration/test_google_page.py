import os

from pytest import fixture

from nicelka import GoogleSearcher


@fixture(scope='module')
def test_cases():
    return ['no_result',
            'no_result_twice',
            'single_result',
            'single_result_with_two_lines',
            'single_result_with_four_lines',
            'single_result_indirect_match_by_city_skipped',
            'single_result_indirect_match_by_zip_code_skipped',
            'single_result_indirect_match_by_city_allowed',
            'single_result_indirect_match_by_zip_code_head_allowed',
            'single_result_indirect_match_by_zip_code_tail_allowed',
            'single_result_duplicate_skipped',
            'single_result_duplicate_allowed',
            'single_result_twice',
            'multiple_results_not_on_top']


@fixture(scope='module')
def create_results_dir(test_cases):
    for test_case in test_cases:
        _, result_dir_path = _get_io_dir_paths(test_case)
        if not os.path.exists(result_dir_path):
            os.mkdir(result_dir_path)


@fixture(scope='module')
def remove_results_dir(test_cases, request):
    def teardown():
        for test_case in test_cases:
            _, result_dir_path = _get_io_dir_paths(test_case)
            if os.path.exists(result_dir_path):
                os.system('cmd /k "rmdir /Q /S {}"'.format(result_dir_path))
    request.addfinalizer(teardown)


def test_searcher_when_no_result(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '24-200 BABIN' + '\n\n' + \
        'Liczba znalezionych adresow: 0'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='no_result')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_no_result_twice(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '24-200 BABIN' + '\n\n' + \
        '======================================================================' + '\n' + \
        '32-731 BYTOMSKO' + '\n\n' + \
        'Liczba znalezionych adresow: 0'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='no_result_twice')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '21-030 KONOPNICA' + '\n\n' + \
        '#Urząd' + '\n\n' + \
        'Urząd Gminy Konopnica' + '\n' + \
        'Kozubszczyzna 127a' + '\n' + \
        '21-030 Motycz' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_search_when_single_result_with_two_lines(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '34-603 UJANOWICE' + '\n\n' + \
        '#Klub' + '\n\n' + \
        'AKS UJANOWICE' + '\n' + \
        '34-603 Ujanowice' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_with_two_lines')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_search_when_single_result_with_four_lines(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '32-862 PORĄBKA IWKOWSKA' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'P.P.H.U. NITUS Piotr Nowak' + '\n' + \
        'Drużków Pusty' + '\n' + \
        'Porąbka Iwkowska 9' + '\n' + \
        '32-862 Porąbka Iwkowska' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_with_four_lines')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_indirect_match_by_city_skipped(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '24-300 WOLA RUDZKA' + '\n\n' + \
        '#Przedszkole' + '\n\n' + \
        'Liczba znalezionych adresow: 0'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_indirect_match_by_city_skipped')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_indirect_match_by_zip_code_skipped(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '24-400 CUPLE' + '\n\n' + \
        '#Biblioteka' + '\n\n' + \
        'Liczba znalezionych adresow: 0'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_indirect_match_by_zip_code_skipped')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_indirect_match_by_city_allowed(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '34-654 PISARZOWA' + '\n\n' + \
        '#Sąd' + '\n\n' + \
        'Sąd Rejonowy w Limanowej' + '\n' + \
        'Marka 19' + '\n' + \
        '34-600 Limanowa' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_indirect_match_by_city_allowed')
    searcher = _run_searcher(data_dir_path, results_dir_path, skip_indirect_matches=False)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_indirect_match_by_zip_code_head_allowed(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '32-725 RAJBRO' + '\n\n' + \
        '#ZNP' + '\n\n' + \
        'Związek Nauczycielstwa Polskiego. Oddział' + '\n' + \
        'Jana Pawła II 42' + '\n' + \
        '34-600 Limanowa' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_indirect_match_by_zip_code_head_allowed')
    searcher = _run_searcher(data_dir_path, results_dir_path, skip_indirect_matches=False)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_indirect_match_by_zip_code_tail_allowed(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '24-150 NAŁĘCZÓW' + '\n\n' + \
        '#Wydział' + '\n\n' + \
        'Urząd Miejski w Nałęczowie' + '\n' + \
        'Lipowa 3' + '\n' + \
        '24-140 Nałęczów' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_indirect_match_by_zip_code_tail_allowed')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_duplicate_skipped(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '34-603 STRZESZYCE' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'Olivea Małopolska Sp. z o. o.' + '\n' + \
        'Strzeszyce 115' + '\n' + \
        '34-603 Ujanowice' + '\n' + \
        '34-603' + '\n\n' + \
        '======================================================================' + '\n' + \
        '34-603 STRZESZYCE' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'Liczba znalezionych adresow: 1'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_duplicate_skipped')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_duplicate_allowed(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '34-603 UJANOWICE' + '\n\n' + \
        '#Bank' + '\n\n' + \
        'Bank Spółdzielczy w Limanowej. Punkt obsługi klienta' + '\n' + \
        'Ujanowice 2' + '\n' + \
        '34-603 Ujanowice' + '\n\n' + \
        '======================================================================' + '\n' + \
        '34-603 UJANOWICE' + '\n\n' + \
        '#Bank' + '\n\n' + \
        'Bank Spółdzielczy w Limanowej. Punkt obsługi klienta' + '\n' + \
        'Ujanowice 2' + '\n' + \
        '34-603 Ujanowice' + '\n\n' + \
        'Liczba znalezionych adresow: 2'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_duplicate_allowed')
    searcher = _run_searcher(data_dir_path, results_dir_path, skip_duplicates=False)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_single_result_twice(create_results_dir, remove_results_dir):
    expected_result = \
        '======================================================================' + '\n' + \
        '34-600 MORDARKA' + '\n\n' + \
        '#Przedszkole' + '\n\n' + \
        'Niepubliczne Przedszkole Integracyjne Chatka Małego Skrzatka' + '\n' + \
        '34-600 Mordarka' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'FUHP Stalkomplet S.C Walenty Szubryt Stanisław Bubula' + '\n' + \
        'Mordarka dz.1236' + '\n' + \
        '34-600' + '\n\n' + \
        'Liczba znalezionych adresow: 2'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='single_result_twice')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def test_searcher_when_multiple_results_not_on_top(create_results_dir):  # remove_results_dir
    expected_result = \
        '======================================================================' + '\n' + \
        '33-300 NOWY SĄCZ' + '\n\n' + \
        '#Fundacja' + '\n\n' + \
        'Fundacja Renovo' + '\n' + \
        'Krakowska 92/5' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja Tarcza' + '\n' + \
        'Jeremiego Wiśniowieckiego 125' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja im. dra Jerzego Masiora w Nowym Sączu' + '\n' + \
        'Tarnowska 25' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Liczba znalezionych adresow: 3'

    data_dir_path, results_dir_path = _get_io_dir_paths(test_case='multiple_results_not_on_top')
    searcher = _run_searcher(data_dir_path, results_dir_path)
    _assert_result_file_content_equals(expected_result, searcher.results_file_path)


def _get_io_dir_paths(test_case):
    return os.path.join('data', 'google_page', test_case), os.path.join('results', 'google_page', test_case)


def _run_searcher(data_dir_path, results_dir_path, skip_indirect_matches=True, skip_duplicates=True):
    searcher = GoogleSearcher(data_dir_path, results_dir_path, skip_indirect_matches=skip_indirect_matches, skip_duplicates=skip_duplicates)
    searcher.search()
    return searcher


def _assert_result_file_content_equals(expected_result, results_file_path):
    with open(results_file_path, encoding='utf8') as file:
        assert file.read() == expected_result


# TODO: scenarios
'''
multiple results - three
multiple results - two
multiple results skip all not direct match
multiple results skip one not direct match
multiple results allow one not direct match
multiple results skip all duplicated
multiple results skip one duplicated
multiple results allow one duplicated
multiple results twice
multiple results - zip code prefix matched

basic use case (mix of all scenarios)
'''
