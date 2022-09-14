import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time
import sqlalchemy

def page_amount_definder(soup):
    res_count = soup.find('span', class_='resultsShowingCount-1707762110').text
    res_count_list = list(res_count.split(' '))
    res_amount = res_count_list[5]
    pages_count = int(res_amount) // 45
    return pages_count
   

def database_loader(df):
    engine = sqlalchemy.create_engine('postgresql://postgres:postgres1234@localhost:5432')
    df.to_sql('my_database', engine)


def ads_scraper():

    result = requests.get('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')

    soup = BS(result.content, 'lxml')

    page_amount = page_amount_definder(soup)

    prices = []
    currancy = []
    locations = []
    created_date = []
    descriptions = []
    titles = []
    badrooms = []
    images = []

    for page in range(1,page_amount+1):
        time.sleep(5)
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        r = requests.get(url)
        soup = BS(r.content, 'lxml')

        add_list = soup.find_all('div', class_='clearfix')
    
        for item in add_list:
            prc = item.find('div', class_='price')
            if prc is not None:
                prc1 = prc.text.replace('\n','').replace(',', '').replace(' ', '')
                prices.append(prc1[1:])
                currancy.append(prc1[:1])
            
            loc = item.find('div', class_='location') 
            if loc is not None:
                loc1 = loc.find('span', '').text.replace('\n','').replace(',', '')
                locations.append(loc1.strip())

            dat = item.find('div', class_='location')
            if dat is not None:
                dat1 = dat.find('span', 'date-posted').text.replace('\n','').replace(',', '')
                created_date.append(dat1.strip()[1:])

            desc = item.find('div', class_='description')
            if desc is not None:
                desc1 = desc.text.replace('\n','').replace(',', '')
                descriptions.append(desc1.strip())

            tit = item.a.text
            if tit.strip() != 'Home':
                titles.append(tit.strip())

            bad = item.find('span', class_='bedrooms')
            if bad is not None:
                bad1 = bad.text.replace('\n','').replace(',', '').replace(' ', '')
                badrooms.append(bad1)

            img = item.find('img')
            if img is not None:
                img1 = img['src']
                images.append(img1)


    df = pd.DataFrame({'images': images,'titles': titles,'created_date': created_date,'locations':locations,
                        'badrooms':badrooms,'descriptions':descriptions,'currancy':currancy,'prices':prices})

    database_loader(df)
   


ads_scraper()

