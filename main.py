from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')

date1 = driver.find_element(By.XPATH, '//td[@class="Py(10px) Ta(start) Pend(10px)"]')
date2 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[1]')
date3 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[1]')
date4 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[1]')
date5 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[1]')
date6 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[1]')
date7 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[1]')
date8 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[1]')
date9 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[1]')
date10 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[1]')

value1 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]')
value2 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[5]')
value3 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[5]')
value4 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[5]')
value5 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[5]')
value6 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[5]')
value7 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[5]')
value8 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[5]')
value9 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[5]')
value10 = driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[5]')

file = open('eur_btc_rates.csv', 'a', newline="")
header = ('Date', 'BTC Closing Value')
data1 = (date1.text, value1.text)
data2 = (date2.text, value2.text)
data3 = (date3.text, value3.text)
data4 = (date4.text, value4.text)
data5 = (date5.text, value5.text)
data6 = (date6.text, value6.text)
data7 = (date7.text, value7.text)
data8 = (date8.text, value8.text)
data9 = (date9.text, value9.text)
data10 = (date10.text, value10.text)

writer = csv.writer(file)
writer.writerow(header)
writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)
writer.writerow(data4)
writer.writerow(data5)
writer.writerow(data6)
writer.writerow(data7)
writer.writerow(data8)
writer.writerow(data9)
writer.writerow(data10)

file.close()
