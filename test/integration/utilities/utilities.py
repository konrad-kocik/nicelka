import os


def get_io_dir_paths(test_suite, test_case):
    return os.path.join('data', test_suite, test_case), os.path.join('reports', test_suite, test_case)


def run_searcher(searcher_class, data_dir_path, report_file_path, skip_indirect_matches=True, skip_duplicates=True):
    searcher = searcher_class(data_dir_path, report_file_path, skip_indirect_matches=skip_indirect_matches, skip_duplicates=skip_duplicates)
    searcher.search()
    return searcher


def assert_report_file_content_equals(expected_report, report_file_path):
    with open(report_file_path, encoding='utf8') as file:
        assert file.read() == expected_report
