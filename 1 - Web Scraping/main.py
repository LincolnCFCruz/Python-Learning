import platform

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core.utils import ChromeType

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Get the default browser on a Windows system
def get_default_browser():
    browser = None
    if platform.system() == 'Windows':
        import winreg
        reg_path = r'SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path) as key:
            value, reg_type = winreg.QueryValueEx(key, 'Progid')
            if reg_type == winreg.REG_SZ:
                browser = value.split('.')[0].lower()
    return browser

# Get the appropriate webdriver for the specified browser
def get_webdriver(browser):
    if browser == 'chrome':
        return webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    elif browser == 'firefox':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'msedgehtm':
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        return None
    
def get_scraping_data(driver):
    if driver:
        driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')

        # Get the table data
        table = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        csv_data = {'Date':[], 'BTC Closing Value':[]} 

        for row in rows[1:11]:
            date = row.find_element(By.XPATH, './td[1]')
            value = row.find_element(By.XPATH, './td[5]')

            csv_data['Date'].append(date.text)
            csv_data['BTC Closing Value'].append(value.text)

        df = pd.DataFrame(csv_data)
        df.to_csv('eur_btc_rates.csv', index=False)

        driver.quit()
    else:
        print('Unable to identify the default browser or no compatible webdriver available.')


if __name__ == "__main__":
    # Identify the default browser
    default_browser = get_default_browser()

    # Get the appropriate webdriver
    driver = get_webdriver(default_browser)

    # Save the scrapped data to a csv
    get_scraping_data(driver)

