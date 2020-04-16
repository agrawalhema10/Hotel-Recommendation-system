from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.request import urlopen as uReq
class scrap:
    def __init__(self,city,checkin,checkout):
        self.city=city
        self.checkin=checkin
        self.checkout=checkout
    def func(self,city,checkin,checkout):
        try:
            self.city=self.city.capitalize()
            myurl=f"https://www.hotels-scanner.com/Hotels/Search?destination=place%3A{self.city}&checkin={self.checkin}&checkout={self.checkout}&Rooms=1&adults_1=2&languageCode=EN&currencyCode=INR"
            browser = webdriver.Chrome("C:\\Users\\Hp\\chromedriver.exe")
            browser.get(myurl)
            html_source = browser.page_source
            page_soup = soup(html_source, 'html.parser')
            f = page_soup.find('div',{"hc_sr_summary"})
            container=f.find_all('div',{"hc-searchresultitem"})
            with open('data_scanner.csv','w') as f:
                f.write('Image_of_site,price,Book Now,Rating,Hotel,Hotel_image'+'\n')
            for x in container:

                a = x.find('div',{"hc-searchresultitem__hotelsummary"})
                img=x.find('a',{"hc-searchresultitem__gallery"})
                ul=img.find('ul',{"hc-searchresultitem__gallerylist"})
                li=ul.find('li',{'hc-searchresultitem__galleryitem'})
                s=li['style']
                s = s.replace('background-image: url(', '')
                s = s.replace(');', '')
                hotel_image=s

                c = a.find('h3',{"hc-searchresultitem__hotelname"})
                name = c.find('a', {"hc-searchresultitem__hotelnamelink"})
                name = name.text
                name = str(name)

                try:
                    g = x.find('div', {"hc-searchresultitemdeal hc-searchresultitemdeal--bestrate"})
                    b = x.find('p', {"hc-hotelrating hc-hotelrating--star"})
                    rating = b['title']
                except:
                    rating=[0,0]
                    rating[1]=0

                try:
                    im = g.find('img', {})
                    image = im['src']
                    p = g.find('span', {'data-track': "SearchResultItem-Deal 1-Price"})
                    d = str(p.text)
                except:

                    pass
                price = d.replace(",","")
                link = g.find('a', {})

                Book_now = "https://www.hotels-scanner.com" + link['href']


                with open('data_scanner.csv', 'a', encoding="utf-8") as f:
                    f.write(image + "," + price + "," + Book_now + "," + rating[1] + "," + name +","+hotel_image+"\n")
        except:
            return "Error"




