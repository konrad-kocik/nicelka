from time import sleep

from exceptbool import except_to_bool
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from nicelka.engine.web_page import WebPage
from nicelka.exceptions.exceptions import GooglePageException
from nicelka.logger.logger import Logger


class GooglePage(WebPage):
    def __init__(self, executable_path):
        super(GooglePage, self).__init__(executable_path=executable_path)
        self._name = 'google_page'
        self._url = 'https://google.pl'

    def start(self):
        super(GooglePage, self).start()
        self._close_cookies_popup()

    def search(self, city, key):
        self._enter_query(city, key)
        return self._get_results()

    def _close_cookies_popup(self):
        Logger.debug(self, 'Trying to close cookies popup...')
        try:
            cookie_frame_xpath = "//iframe[contains(@src, 'consent.google.com')]"
            self._wait_for_element_by_xpath(cookie_frame_xpath, timeout=2)
            cookie_frame = self._find_element_by_xpath(cookie_frame_xpath)
            self._switch_to_frame(cookie_frame)
            accept_button = self._find_element_by_xpath('//*[@id="introAgreeButton"]/span/span')
            accept_button.click()
            Logger.debug(self, 'Cookies popup closed successfully')
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            Logger.error(self, e, self._close_cookies_popup.__name__)

    def _enter_query(self, city, key):
        Logger.info(self, "Searching for city: '{}' key: '{}'".format(city, key))
        sleep(1.2)

        try:
            self._driver.get(url=self._url)
            search_input = self._find_element_by_name('q')
            search_input.send_keys('{} {} adres'.format(city, key))
            search_input.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            Logger.error(self, e, self._enter_query.__name__)
            raise GooglePageException('Failed to enter query')

    def _get_results(self):
        if self._is_single_result():
            return self._get_single_result()
        elif self._are_multiple_results():
            return self._get_multiple_results()
        else:
            Logger.info(self, 'No results')
            return []

    @except_to_bool(exc=NoSuchElementException)
    def _is_single_result(self):
        self._find_element_by_class_name('LrzXr')

    @except_to_bool(exc=NoSuchElementException)
    def _are_multiple_results(self):
        self._find_element_by_class_name('H93uF')

    def _get_single_result(self):
        Logger.info(self, 'Getting single result...')
        result = []

        try:
            name_output_xpath = '//div[@class="SPZz6b"]//span'
            self._wait_for_element_by_xpath(name_output_xpath, timeout=2)
            name_output = self._find_element_by_xpath(name_output_xpath)
            name = name_output.text

            address_output_class = 'LrzXr'
            self._wait_for_element_by_class_name(address_output_class, timeout=2)
            address_output = self._find_element_by_class_name(address_output_class)
            address = address_output.text

            Logger.debug(self, 'Single result: {} {}'.format(name, address))
            result.append(name + '\n' + self._format_address(address) + '\n')
        except (TimeoutException,
                NoSuchElementException,
                ElementClickInterceptedException,
                StaleElementReferenceException) as e:
            Logger.error(self, e, self._get_single_result.__name__)
            raise GooglePageException('Failed to get single result')

        return result

    def _get_multiple_results(self):
        Logger.info(self, 'Getting multiple results...')
        results = []
        result_link_class = 'dbg0pd'

        try:
            self._open_map()
            self._wait_for_element_by_class_name(result_link_class, 2)
            result_links = self._find_elements_by_class_name(result_link_class)
        except (TimeoutException, NoSuchElementException, GooglePageException) as e:
            Logger.error(self, e, self._get_multiple_results.__name__)
            return results

        for result_link in result_links:
            try:
                name, address = self._get_one_of_multiple_results(result_link)
                results.append(name + '\n' + self._format_address(address) + '\n')
            except GooglePageException as e:
                Logger.error(self, e, self._get_multiple_results.__name__)

        return results

    def _open_map(self):
        try:
            map_link = self._find_element_by_class_name('H93uF')
            map_link.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            Logger.error(self, e, self._open_map.__name__)
            raise GooglePageException('Failed to open a map')

    def _get_one_of_multiple_results(self, result_link):
        try:
            result_link.click()
            sleep(2)

            name_output_xpath = '//div[@class="SPZz6b"]//span'
            self._wait_for_element_by_xpath(name_output_xpath, timeout=2)
            name_output = self._find_element_by_xpath(name_output_xpath)
            name = name_output.text

            address_output_class = 'LrzXr'
            self._wait_for_element_by_class_name(address_output_class, timeout=1)
            address_output = self._find_element_by_class_name(address_output_class)
            address = address_output.text
        except (TimeoutException,
                NoSuchElementException,
                ElementClickInterceptedException,
                StaleElementReferenceException) as e:
            Logger.error(self, e, self._get_one_of_multiple_results.__name__)
            raise GooglePageException('Failed to get one of multiple results')

        Logger.debug(self, 'One of multiple results: {} {}'.format(name, address))
        return name, address

    @staticmethod
    def _format_address(address):
        return address.replace(', ', '\n')
