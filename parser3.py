from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient

class HHruParser:

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}

    def hh(main_link, search_str, n_str):
        # n_str - кол-во просматриваемых страниц
        response = requests.get(
            main_link + '/search/vacancy?clusters=true&enable_snippets=true&text=' + search_str + '&showClusters=true',
            headers=headers)
        dom = bs(response.text, 'html.parser')

        jobs = []
        for i in range(n_str):
            jobs_block = dom.find('div', {'class': 'vacancy-serp'})
            jobs_list = jobs_block.findChildren(recursive=False)
            for job in jobs_list:
                job_data = {}
                req = job.find('span', {'class': 'g-user-content'})
                if req != None:
                    main_info = req.findChild()
                    job_name = main_info.getText()
                    job_link = main_info['href']
                    salary = job.find('div', {'class': 'vacancy-serp-item__compensation'})
                    if not salary:
                        salary_min = None
                        salary_max = None
                    else:
                        salary = salary.getText().replace(u'\xa0', u'')
                        salaries = salary.split('-')
                        salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
                        salary_min = int(salaries[0])
                        if len(salaries) > 1:
                            salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                            salary_max = int(salaries[1])
                        else:
                            salary_max = None
                    job_data['name'] = job_name
                    job_data['salary_min'] = salary_min
                    job_data['salary_max'] = salary_max
                    job_data['link'] = job_link
                    job_data['site'] = main_link
                    jobs.append(job_data)
            time.sleep(random.randint(1, 10))
            next_btn_block = dom.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})
            next_btn_link = next_btn_block['href']
            response = requests.get(main_link + next_btn_link, headers=headers)
            dom = bs(response.text, 'html.parser')

        pprint(jobs)
        return jobs

    search_str = 'Python'
    n_str = 2

hh('https://kolomna.hh.ru', search_str, n_str)

if __name__ == '__main__':
    client = MongoClient('127.0.0.1', 27017)
    db = client['hh_ru']
    parser = HHruParser()
    for hhru in hh:
        hh = parser.hh(hh)
        db.hh.insert_one(hh)

#------------------------------------------
def bigsalarythat(x):
    client = MongoClient('127.0.0.1', 27017)
    db = client['hh_ru']
    db.hh.find({salary_min,{$gt:x}})
bigsalarythat(int(input("Введите зарплату")))

