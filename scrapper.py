from bs4 import BeautifulSoup
from selenium import webdriver

data = []
quote_page = ['https://www.compareremit.com/compare-money-transfer-services-from-usd-to-india/?amt=1000&sc=USD&rc=INR']

def scrapSites():
    for pg in quote_page:
        #page = urllib2.urlopen(pg)
        driver = webdriver.Firefox(executable_path=r'C:\Users\keyul\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
        driver.get(pg)
        page = driver.page_source

        soup = BeautifulSoup(page, 'html.parser')
        company = soup.find_all('div', attrs ={'class': 'inner-padding-40'})
        for cpy in company:
            service= cpy.find('img', attrs ={'class': 'partner-logo'})
            service_name= service['alt']
            service_name = service_name.replace(' Logo','')
            print (service_name)
            name_box = cpy.find_all('span', attrs={'class': 'rate', 'title': 'Guaranteed rate'})
            data = [span.get_text() for span in name_box]
            for d in data:
                print (d)
            print ("----")


#scrapSites()
quote_page = ['https://www.producthunt.com/upcoming/darian']
def scrapEmbedly():
    for pg in quote_page:
        #page = urllib2.urlopen(pg)
        url = 'http://embed.ly/code?url='+pg
        driver = webdriver.Firefox(executable_path=r'C:\Users\keyul\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
        driver.get(url)
        page = driver.page_source

        soup = BeautifulSoup(page, 'html.parser')
        company = soup.find('div', attrs ={'id': 'snippetDiv'})
        print(company.get_text())
        print ("----")


scrapEmbedly()