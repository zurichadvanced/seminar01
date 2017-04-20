import requests
from bs4 import BeautifulSoup
import time

proxies = {'http': 'http://10.243.241.44:8080', 'https':'10.243.241.44:8080'}

http = 'http://www.mismarcadores.com/futbol/espana/laliga/'

page = requests.get(http, proxies = proxies)

status = page.status_code

print(status) #200 good request, 400 bad request

##########################################################################################


if status == 200:

    data = page.text
    html = BeautifulSoup(data, 'lxml') #return a BS object that parse HTML
    a_objects = html.find_all('div', {'id':'e-content'}) #return a list of objects 'div'



    for i, a_object in enumerate(a_objects):

        partidos = a_object.find_all('span')
        if len(partidos) > 0:
            string = partidos[0].text
            string = string.split(',')
            [print(i) for i in string]


else:
    print('bad request')

#############################################################################################

while True:
    proxies = {'http': 'http://10.243.241.44:8080', 'https': '10.243.241.44:8080'}

    http = 'https://www.timeanddate.com/weather/spain/barcelona'

    page = requests.get(http, proxies = proxies)

    data = page.text

    html = BeautifulSoup(data, 'lxml')

    temp = html.find_all('div', class_= 'h2')

    print(temp)

    sTerm = html.find_all('div', class_ = 'clear')
    print(sTerm)

    print('La Temperatura de Barcelona es: ' + temp[0].text)
    print('La sensacion termica es: ' + sTerm[1].text)

    time.sleep(15)



##################################################################################################

from datetime import datetime
import re
from datetime import timedelta


proxies = {'http': 'http://10.243.241.44:8080', 'https':'10.243.241.44:8080'}

start_date = '2017-04-01'
end_date = '2017-04-01'

start = datetime.strptime(start_date, '%Y-%m-%d').date()
end = datetime.strptime(end_date, '%Y-%m-%d').date()


def dateiterator(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


with open('file_output.csv', 'w', newline='') as file:
    header = 'ANIO' + ';' + 'MES' + ';' + 'DIA' + ';' + 'HORA' + ';' + 'PESPANIA' + ';' + 'PPORTUGAL' + ';'
    file.write(header)
    for dt in dateiterator(start, end):
        dt = datetime.strftime(dt, '%Y%m%d')
        http = 'http://www.omie.es/datosPub/marginalpdbc/marginalpdbc_' + dt +'.1'
        page = requests.get(http, proxies=proxies)
        print(page.status_code)  # Starting 2 is downloaded ok, Starting 4 not
        page = page.text
        page = re.sub('\*', '', page)
        page = re.sub('MARGINALPDBC;', '', page)
        file.write(page)
        print(page)





