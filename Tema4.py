import requests
from bs4 import BeautifulSoup
import pandas as pd
total = []
r = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-22-aprilie-2020-ora-13-00/')
s1 = BeautifulSoup(r.text, 'lxml')
header = '<tr><th>Nr.crt</th><th>Judet</th>'
for i in range(3,25):
    header += f'<th>Aprilie {i}</th>'
header += '</tr>'

rows = ['<tr>' for i in range(43)]

index = 0
for rand in s1.table.findAll('tr')[1:]:
    for camp in rand.findAll('td')[0:1]:  # nr crt
        # print(camp.text)
        if index != 42:
            rows[index] += f'<td>{camp.text}</td>'
        else:
            rows[index] += f'<td></td>'

    for camp1 in rand.findAll('td')[1:2]:  # judet
        if index != 42:
            rows[index] += f'<td>{camp1.text}</td>'
        else:
            rows[index] += f'<td>Total</td>'
    index += 1

for zi in range(3, 25):
    index = 0
    url = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-'
    if zi == 7 or zi == 17:
        for i in range(42):
            rows[i] += '<td>TOATE</td>'
        total.append(f'<td>TOATE</td>')
    else:
        url += f'{zi}-aprilie-2020-ora-13-00/'
        r = requests.get(url)
        s1 = BeautifulSoup(r.text, 'lxml')
        for rand in s1.table.findAll('tr')[1:]:
            for camp in rand.findAll('td')[2:]:
                if index != 42:
                    rows[index] += f'<td>{camp.text}</td>'
                index += 1
        if index == 42 or index == 43:
            for rand in s1.table.findAll('tr')[1:]:
                for camp in rand.findAll('td')[1:2]:
                    if '.' in camp.text and 'Mun' not in camp.text or camp.text.isdigit():

                        total.append(f'<td>{camp.text}</td>')


rows[42] += ''.join(total)

for row in rows:
    row += '</tr>'
body = ''.join(rows)
text = f'<table>{header}{body}</table>'
file = open('C:/Users/andre/Desktop/SituatieCovid.html', 'w', encoding='utf-8')
file.writelines(text)
file.close()

table = pd.read_html('C:/Users/andre/Desktop/SituatieCovid.html')[0]
table.to_excel('C:/Users/andre/Desktop/SituatieCovid.xls')
