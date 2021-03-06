from pytest import fixture

from tests.integration.utilities.utilities import get_io_dir_paths, create_dir, remove_dir, run_google_searcher, assert_report_file_content_equals


test_suite = 'google_page'
test_cases = ['no_result',
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
              'single_result_blacklisted_skipped',
              'single_result_blacklisted_allowed',
              'single_result_twice',
              'multiple_results',
              'multiple_results_indirect_matches_by_city_skipped',
              'multiple_results_indirect_matches_by_zip_code_head_skipped',
              'multiple_results_indirect_matches_by_city_allowed',
              'multiple_results_indirect_matches_by_zip_code_head_allowed',
              'multiple_results_duplicate_skipped',
              'multiple_results_duplicate_allowed',
              'multiple_results_not_on_top',
              'multiple_results_blacklisted_skipped',
              'multiple_results_blacklisted_allowed',
              'multiple_results_twice'
              ]


@fixture(scope='module')
def create_reports_dirs():
    for test_case in test_cases:
        _, report_dir_path = get_io_dir_paths(test_suite, test_case)
        create_dir(report_dir_path)


@fixture(scope='module')
def remove_reports_dirs(request):
    def teardown():
        for test_case in test_cases:
            _, report_dir_path = get_io_dir_paths(test_suite, test_case)
            remove_dir(report_dir_path)
    request.addfinalizer(teardown)


def test_no_result(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '24-200 BABIN' + '\n\n' + \
        'Results found: 0'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='no_result')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_no_result_twice(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '24-200 BABIN' + '\n\n' + \
        '======================================================================' + '\n' + \
        '32-731 BYTOMSKO' + '\n\n' + \
        'Results found: 0'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='no_result_twice')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '21-030 KONOPNICA' + '\n\n' + \
        '#Urząd' + '\n\n' + \
        'Urząd Gminy Konopnica' + '\n' + \
        'Kozubszczyzna 127a' + '\n' + \
        '21-030 Motycz' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_with_two_lines(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '34-603 UJANOWICE' + '\n\n' + \
        '#Klub' + '\n\n' + \
        'AKS UJANOWICE' + '\n' + \
        '34-603 Ujanowice' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_with_two_lines')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_with_four_lines(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '32-862 PORĄBKA IWKOWSKA' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'P.P.H.U. NITUS Piotr Nowak' + '\n' + \
        'Drużków Pusty' + '\n' + \
        'Porąbka Iwkowska 9' + '\n' + \
        '32-862 Porąbka Iwkowska' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_with_four_lines')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_indirect_match_by_city_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '24-300 WOLA RUDZKA' + '\n\n' + \
        'Results found: 0'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_indirect_match_by_city_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_indirect_match_by_zip_code_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '24-400 CUPLE' + '\n\n' + \
        'Results found: 0'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_indirect_match_by_zip_code_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_indirect_match_by_city_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '34-654 PISARZOWA' + '\n\n' + \
        '#Sąd' + '\n\n' + \
        'Sąd Rejonowy w Limanowej' + '\n' + \
        'Marka 19' + '\n' + \
        '34-600 Limanowa' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_indirect_match_by_city_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_indirect_matches=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_indirect_match_by_zip_code_head_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '32-725 RAJBRO' + '\n\n' + \
        '#ZNP' + '\n\n' + \
        'Związek Nauczycielstwa Polskiego. Oddział' + '\n' + \
        'Jana Pawła II 42' + '\n' + \
        '34-600 Limanowa' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_indirect_match_by_zip_code_head_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_indirect_matches=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_indirect_match_by_zip_code_tail_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '24-150 NAŁĘCZÓW' + '\n\n' + \
        '#Wydział' + '\n\n' + \
        'Urząd Miejski w Nałęczowie' + '\n' + \
        'Lipowa 3' + '\n' + \
        '24-140 Nałęczów' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_indirect_match_by_zip_code_tail_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_duplicate_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '34-603 STRZESZYCE' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'Olivea Małopolska Sp. z o. o.' + '\n' + \
        'Strzeszyce 115' + '\n' + \
        '34-603 Ujanowice' + '\n' + \
        '34-603' + '\n\n' + \
        '======================================================================' + '\n' + \
        '34-603 STRZESZYCE' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_duplicate_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_duplicate_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
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
        'Results found: 2'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_duplicate_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_duplicates=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_blacklisted_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '13-340 BIELICE' + '\n\n' + \
        'Results found: 0'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_blacklisted_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_blacklisted_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '13-340 BIELICE' + '\n\n' + \
        '#Szkoła' + '\n\n' + \
        'Zespół Szkół w Bielicach, Gimnazjum im. Narodów Zjednoczonej Europy' + '\n' + \
        'Bielice 120' + '\n' + \
        '13-330 Bielice' + '\n\n' + \
        'Results found: 1'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_blacklisted_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_blacklisted=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_single_result_twice(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '34-600 MORDARKA' + '\n\n' + \
        '#Przedszkole' + '\n\n' + \
        'Niepubliczne Przedszkole Integracyjne Chatka Małego Skrzatka' + '\n' + \
        '34-600 Mordarka' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'FUHP Stalkomplet S.C Walenty Szubryt Stanisław Bubula' + '\n' + \
        'Mordarka dz.1236' + '\n' + \
        '34-600' + '\n\n' + \
        'Results found: 2'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='single_result_twice')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '33-300 NOWY SĄCZ' + '\n\n' + \
        '#muzeum' + '\n\n' + \
        'Muzeum Okręgowe w Nowym Sączu' + '\n' + \
        'Lwowska 3' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Muzeum Okręgowe w Nowym Sączu - Gmach Głowny' + '\n' + \
        'Jagiellońska 56' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Sądecki Park Etnograficzny' + '\n' + \
        'Gen. Wieniawy-Długoszowskiego 83B' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Miasteczko Galicyjskie. Oddział Muzeum Okręgowego w Nowym Sączu' + '\n' + \
        'Lwowska 226' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Galeria Marii Ritter. Oddział Muzeum Okręgowego' + '\n' + \
        'Rynek 2' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Results found: 5'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_indirect_matches_by_city_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '87-207 MAŁE PUŁKOWO' + '\n\n' + \
        '#PZU' + '\n\n' + \
        'Kuźnia Smaków' + '\n' + \
        '20' + '\n' + \
        '20' + '\n' + \
        '87-207 Małe Pułkowo' + '\n\n' + \
        'Markostal Marek Mrowiński' + '\n' + \
        'Małe Pułkowo 67' + '\n' + \
        '87-207 Małe Pułkowo' + '\n\n' + \
        'Results found: 2'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_indirect_matches_by_city_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_indirect_matches_by_zip_code_head_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '33-393 MARCINKOWICE' + '\n\n' + \
        '#Szkoła' + '\n\n' + \
        'Szkoła Podstawowa im. Marszałka Józefa Piłsudskiego' + '\n' + \
        '33-393' + '\n' + \
        'Marcinkowicka 132' + '\n' + \
        '33-395 Marcinkowice' + '\n\n' + \
        'Zespół Szkół im. Władysława Orkana' + '\n' + \
        'Marcinkowice 1' + '\n' + \
        '33-395 Marcinkowice' + '\n\n' + \
        'Results found: 2'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_indirect_matches_by_zip_code_head_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_indirect_matches_by_city_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '87-207 MAŁE PUŁKOWO' + '\n\n' + \
        '#PZU' + '\n\n' + \
        'PZU' + '\n' + \
        'Wolności 44' + '\n' + \
        '87-200 Wąbrzeźno' + '\n\n' + \
        'PZU' + '\n' + \
        'Plac Tysiąclecia 22A' + '\n' + \
        '87-400 Golub-Dobrzyń' + '\n\n' + \
        'PZU Ubezpieczenia Wąbrzeźno - Agent Andrzej Sadłowski' + '\n' + \
        'Poniatowskiego 8' + '\n' + \
        '87-200 Wąbrzeźno' + '\n\n' + \
        'Kuźnia Smaków' + '\n' + \
        '20' + '\n' + \
        '20' + '\n' + \
        '87-207 Małe Pułkowo' + '\n\n' + \
        'PZU Ubezpieczenia Czernikowo - Agent Bożena Zygnerska-Nawrotek' + '\n' + \
        'Juliusza Słowackiego 3' + '\n' + \
        '87-125 Czernikowo' + '\n\n' + \
        'Agencja PZU S.A' + '\n' + \
        'Generała Władysława Sikorskiego 36a' + '\n' + \
        '87-140 Chełmża' + '\n\n' + \
        'Grochocka G. Ubezpieczenia' + '\n' + \
        'Krasińskiego 5' + '\n' + \
        '87-200 Wąbrzeźno' + '\n\n' + \
        'PZU Ubezpieczenia Brodnica - Agent Katarzyna Korzeńska' + '\n' + \
        'Główna 29' + '\n' + \
        '87-300 Jabłonowo Pomorskie' + '\n\n' + \
        'PZU Ubezpieczenia Rypin - Agent Grzegorz Makowski' + '\n' + \
        'Jana Pawła II 6' + '\n' + \
        '87-500 Rypin' + '\n\n' + \
        'Oddział PZU - Rypin, Nowy Rynek,' + '\n' + \
        'Nowy Rynek 6' + '\n' + \
        '87-500 Rypin' + '\n\n' + \
        'Markostal Marek Mrowiński' + '\n' + \
        'Małe Pułkowo 67' + '\n' + \
        '87-207 Małe Pułkowo' + '\n\n' + \
        'Bieganowska Anna. Ubezpieczenia' + '\n' + \
        'Plac Tysiąclecia 2' + '\n' + \
        '87-400 Golub-Dobrzyń' + '\n\n' + \
        'Results found: 12'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_indirect_matches_by_city_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_indirect_matches=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_indirect_matches_by_zip_code_head_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '33-393 MARCINKOWICE' + '\n\n' + \
        '#Szkoła' + '\n\n' + \
        'Szkoła Podstawowa im. Marszałka Józefa Piłsudskiego' + '\n' + \
        '33-393' + '\n' + \
        'Marcinkowicka 132' + '\n' + \
        '33-395 Marcinkowice' + '\n\n' + \
        'Zespół Szkół im. Władysława Orkana' + '\n' + \
        'Marcinkowice 1' + '\n' + \
        '33-395 Marcinkowice' + '\n\n' + \
        'Szkoła Podstawowa im. Stanisława i Jana Potoczków' + '\n' + \
        '33-395 Rdziostów' + '\n\n' + \
        'Szkoła Podstawowa im. Mieszka l' + '\n' + \
        'Marcinkowicka 46' + '\n' + \
        '78-640 Marcinkowice' + '\n\n' + \
        'Szkoła Pływania "TB" Tomasz Baliczek' + '\n' + \
        'Marcinkowicka 9' + '\n' + \
        '33-395 Nowy Sącz' + '\n\n' + \
        'Results found: 5'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_indirect_matches_by_zip_code_head_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_indirect_matches=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_duplicate_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '88-140 GNIEWKOWO' + '\n\n' + \
        '#Przedsiębiorstwo' + '\n\n' + \
        'Gniewkowo Sp. z o.o. Przedsiębiorstwo komunalne' + '\n' + \
        'Jana Kilińskiego 9' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'I.T.I. Poland Sp. z o.o.' + '\n' + \
        'Przemysłowa 2' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Techniki Pompowej IMPELLER' + '\n' + \
        'Zajezierze 8 B' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Pipczyńska Katarzyna. Przedsiębiorstwo wielobranżowe' + '\n' + \
        'Jana Kilińskiego 49' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Tinapol. PH. Lubańska T.' + '\n' + \
        'Wojska Polskiego 23' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Wielobranżowe "e-mir"' + '\n' + \
        'Toruńska 33a' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Results found: 6'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_duplicate_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_duplicate_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '88-140 GNIEWKOWO' + '\n\n' + \
        '#Przedsiębiorstwo' + '\n\n' + \
        'Gniewkowo Sp. z o.o. Przedsiębiorstwo komunalne' + '\n' + \
        'Jana Kilińskiego 9' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'I.T.I. Poland Sp. z o.o.' + '\n' + \
        'Przemysłowa 2' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Techniki Pompowej IMPELLER' + '\n' + \
        'Zajezierze 8 B' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Pipczyńska Katarzyna. Przedsiębiorstwo wielobranżowe' + '\n' + \
        'Jana Kilińskiego 49' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Tinapol. PH. Lubańska T.' + '\n' + \
        'Wojska Polskiego 23' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Wielobranżowe "e-mir"' + '\n' + \
        'Toruńska 33a' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        '#Przedsiębiorstwo' + '\n\n' + \
        'Gniewkowo Sp. z o.o. Przedsiębiorstwo komunalne' + '\n' + \
        'Jana Kilińskiego 9' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'I.T.I. Poland Sp. z o.o.' + '\n' + \
        'Przemysłowa 2' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Techniki Pompowej IMPELLER' + '\n' + \
        'Zajezierze 8 B' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Pipczyńska Katarzyna. Przedsiębiorstwo wielobranżowe' + '\n' + \
        'Jana Kilińskiego 49' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Tinapol. PH. Lubańska T.' + '\n' + \
        'Wojska Polskiego 23' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Wielobranżowe "e-mir"' + '\n' + \
        'Toruńska 33a' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Results found: 12'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_duplicate_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_duplicates=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_not_on_top(create_reports_dirs, remove_reports_dirs):
    expected_report = \
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
        'Fundacja Inicjatyw Społeczno - Akademickich' + '\n' + \
        'Nawojowska 95' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja Rozwoju Ziem Górskich' + '\n' + \
        'Węgierska 33' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Mada. Fundacja Pomocy Osobom z Autyzmem' + '\n' + \
        'Al. Wolności 19' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja Programów Pomocy Dla Rolnictwa' + '\n' + \
        'Tadeusza Kościuszki 7' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja Instytut Państwa i Prawa' + '\n' + \
        'Stefana Czarnieckiego 5' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Nox. Fundacja Pomocy Osobom Fizycznie Niepełnosprawnym' + '\n' + \
        'Jana Kochanowskiego 17' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Stowarzyszenie Sursum Corda ("w górę serca")' + '\n' + \
        'Lwowska 11' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja na rzecz Rozwoju Polskiego Rolnictwa. Biuro terenowe' + '\n' + \
        'Tarnowska 28' + '\n' + \
        '33-395 Nowy Sącz' + '\n\n' + \
        'Nadzieja. Stowarzyszenie Rodziców i Przyjaciół Dzieci Niepełnosprawnych Ruchowo i Umysłowo' + '\n' + \
        'Jana Freislera 10' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Europejski Instytut Rozwoju Obywatelskiego' + '\n' + \
        'Jagiellońska 18' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Humaneo' + '\n' + \
        'biuro' + '\n' + \
        'Nawojowska 12' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Consilium' + '\n' + \
        'ul' + '\n' + \
        'Nadbrzeżna 3' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja Prawa Dzieci oddział Nowy Sącz' + '\n' + \
        'Rynek 30' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Towarzystwo Przyjaciół Dzieci' + '\n' + \
        'Świętej Kunegundy 16' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Fundacja SZOK' + '\n' + \
        'Władysława Broniewskiego 20 E/13' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Wspólnota Emaus - Nowosądeckie Towarzystwa Pomocy im. św. Brata Alberta' + '\n' + \
        'Szwedzka 18' + '\n' + \
        '33-300 Nowy Sącz' + '\n\n' + \
        'Results found: 19'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_not_on_top')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_blacklisted_skipped(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '88-140 GNIEWKOWO' + '\n\n' + \
        '#Przedsiębiorstwo' + '\n\n' + \
        'Gniewkowo Sp. z o.o. Przedsiębiorstwo komunalne' + '\n' + \
        'Jana Kilińskiego 9' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Techniki Pompowej IMPELLER' + '\n' + \
        'Zajezierze 8 B' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Tinapol. PH. Lubańska T.' + '\n' + \
        'Wojska Polskiego 23' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Results found: 3'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_blacklisted_skipped')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_blacklisted_allowed(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '88-140 GNIEWKOWO' + '\n\n' + \
        '#Przedsiębiorstwo' + '\n\n' + \
        'Gniewkowo Sp. z o.o. Przedsiębiorstwo komunalne' + '\n' + \
        'Jana Kilińskiego 9' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'I.T.I. Poland Sp. z o.o.' + '\n' + \
        'Przemysłowa 2' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Techniki Pompowej IMPELLER' + '\n' + \
        'Zajezierze 8 B' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Pipczyńska Katarzyna. Przedsiębiorstwo wielobranżowe' + '\n' + \
        'Jana Kilińskiego 49' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Tinapol. PH. Lubańska T.' + '\n' + \
        'Wojska Polskiego 23' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Przedsiębiorstwo Wielobranżowe "e-mir"' + '\n' + \
        'Toruńska 33a' + '\n' + \
        '88-140 Gniewkowo' + '\n\n' + \
        'Results found: 6'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_blacklisted_allowed')
    searcher = run_google_searcher(data_dir_path, report_dir_path, allow_blacklisted=True)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)


def test_multiple_results_twice(create_reports_dirs, remove_reports_dirs):
    expected_report = \
        '======================================================================' + '\n' + \
        '86-134 DOLNA GRUPA' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'O.M.N. Altomix' + '\n' + \
        'Dolna Grupa 55B' + '\n' + \
        '86-134 Dolna Grupa' + '\n\n' + \
        'BUMAX Okna Drzwi Meble' + '\n' + \
        'Tartaczna 9' + '\n' + \
        '86-134 Dolna Grupa' + '\n\n' + \
        'Altomix sp.j. Odlewnia metali' + '\n' + \
        'Dolna Grupa 55b' + '\n' + \
        '86-134 Dolna Grupa' + '\n\n' + \
        'Klocek Ryszard. Deski, więźby dachowe. Usługi tartaczne' + '\n' + \
        '86-134 Dolna Grupa; Tartaczna' + '\n' + \
        '86-134' + '\n\n' + \
        'Kubiak-Pol. Skup, sprzedaż naprawa palet' + '\n' + \
        'DK91 18' + '\n' + \
        '86-134 Dolna Grupa' + '\n\n' + \
        '======================================================================' + '\n' + \
        '87-123 GŁOGOWO' + '\n\n' + \
        '#Produkcja' + '\n\n' + \
        'ALWA' + '\n' + \
        'Spokojna 8' + '\n' + \
        '87-123 Głogowo' + '\n\n' + \
        'WW Ekochem' + '\n' + \
        'Akacjowa 1' + '\n' + \
        '87-123 Głogowo' + '\n\n' + \
        'MECHATRONIKA' + '\n' + \
        'Ul: Wilcza 36' + '\n' + \
        'Głogowo' + '\n' + \
        '87-123 Dobrzejewice' + '\n\n' + \
        'Results found: 8'

    data_dir_path, report_dir_path = get_io_dir_paths(test_suite, test_case='multiple_results_twice')
    searcher = run_google_searcher(data_dir_path, report_dir_path)
    assert_report_file_content_equals(expected_report, searcher.report_file_path)
