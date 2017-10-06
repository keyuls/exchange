import airtable
import json
from flask import make_response
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2




def ratesList():
    at = airtable.Airtable('apprqrzvw676i9OFy', 'keyrlOeTeyJFkz8D2')
    table= at.get('rate%20details')
    records= table["records"]
    result = createRateList(records)
    result = json.dumps(result, indent=4)
    r = make_response(result)
    r.headers['Content-Type'] = 'application/json'
    return r


def createRateList(records):
    element = []
    specialOffer = True
    for field in records:
        if "special_offer" in field["fields"]:
            specialOffer = False
        output={
            "send_from" : field["fields"]["send_from"],
            "send_to": field["fields"]["send_to"],
            "rate": field["fields"]["rate"],
            "service": [
              {
                "name" : field["fields"]["name"],
                "image_url":field["fields"]["image_url"],
                "ref_url":field["fields"]["ref_url"],
                "special_offer": specialOffer
              }
            ]
        }
        element.append(output)

    return element

def scrapSite():
    data = []
    quote_page = ['https://www.compareremit.com/compare-money-transfer-services-from-usd-to-india/?amt=1000&sc=USD&rc=INR']
    for pg in quote_page:
        # page = urllib2.urlopen(pg)
        driver = webdriver.Firefox(executable_path=r'C:\Users\pax\Downloads\geckodriver-v0.19.0-win64\geckodriver.exe')
        driver = webdriver.Chrome()
        #driver.get(pg)
        page = driver.page_source

        soup = BeautifulSoup(page, 'html.parser')
        company = soup.find_all('div', attrs={'class': 'inner-padding-40'})
        for cpy in company:
            service = cpy.find('img', attrs={'class': 'partner-logo'})
            service_name = service['alt']
            service_name = service_name.replace(' Logo', '')
            print (service_name)
            name_box = cpy.find_all('span', attrs={'class': 'rate', 'title': 'Guaranteed rate'})
            data = [span.get_text() for span in name_box]
            for d in data:
                print d
            print ("----")
    return []