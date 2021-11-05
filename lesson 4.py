from pprint import pprint
from lxml import  html
import requests
from datetime import datetime
from pymongo import MongoClient

def get_news_mail_ru():
    news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    keys = ('title', 'date', 'link')
    date_format = '%Y-%m-%dT%H:%M:%S%z'

    mail_ru = 'https://mail.ru/'

    request = requests.get(mail_ru, headers=headers)
    root = html.fromstring(request.text)

    news_links = root.xpath('''(//div[@class =  "news-item o-media news-item_media news-item_main"]  |  
                                //div[@class =  "news-item__inner"])
                                /a[contains(@href, "news.mail.ru")]/@href''')

    news_text = root.xpath('''(//div[@class =  "news-item o-media news-item_media news-item_main"]//h3  |  
                               //div[@class =  "news-item__inner"]/a[contains(@href, "news.mail.ru")])
                               /text()''')

    for i in range(len(news_text)):
        news_text[i] = news_text[i].replace(u'\xa0', u' ')

    news_links_temp = []
    for item in news_links:
        item = item.split('/')
        news_links_temp.append('/'.join(item[0:5]))

    news_links = news_links_temp
    del (news_links_temp)

    news_date = []

    for item in news_links:
        request = requests.get(item, headers=headers)
        root = html.fromstring(request.text)
        date = root.xpath('//span[@class="note__text breadcrumbs__text js-ago"]/@datetime')
        news_date.extend(date)

    for i in range(len(news_date)):
        news_date[i] = datetime.strptime(news_date[i], date_format)

    for item in list(zip(news_text, news_date, news_links)):
        news_dict = {}
        for key, value in zip(keys, item):
            news_dict[key] = value

        news_dict['source'] = 'mail.ru'
        news.append(news_dict)

    return news

get_news_mail_ru()

'''if __name__ == '__main__':
    client = MongoClient('127.0.0.1', 27017)
    db = client['mail_ru']
    parser = mailruParser()
    for mailru in mail:
        mail = parser.mail(mail)
        db.mail.insert_one(mail)'''
