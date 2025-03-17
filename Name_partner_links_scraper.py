import requests as req
import re
import math
from bs4 import BeautifulSoup
import pandas as pd

# Set options to display text (conditions for table cells in pd)
pd.set_option('max_colwidth', 500)
pd.set_option('display.width', 700)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 700)

headers = {
'Accept' : 'Accept',
'Accept-Encoding' : 'Accept-Encoding',
'Accept-Language' : 'Accept-Language',
'Cache-Control' : 'Cache-Control',
'Cookie' : 'Cookie',
'Priority' : 'Priority',
'Sec-Ch-Ua' : 'Sec-Ch-Ua',
'Sec-Ch-Ua-Mobile' : 'Sec-Ch-Ua-Mobile',
'Sec-Ch-Ua-Platform' : 'Sec-Ch-Ua-Platform',
'Sec-Fetch-Dest' : 'Sec-Fetch-Dest',
'Sec-Fetch-Mode' : 'Sec-Fetch-Mode',
'Sec-Fetch-Site' : 'Sec-Fetch-Site',
'Sec-Fetch-User' : 'Sec-Fetch-User',
'Upgrade-Insecure-Requests' : 'Upgrade-Insecure-Requests',
'User-Agent' : 'User-Agent'
}

url = f'https://www.astromeridian.ru/imya/'
r = req.get(url, headers=headers, verify=False)
text = r.text

# Parse HTML text using BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')

# Find all h2 and h4 elements
h2_elements = soup.find_all('h2')
h4_elements = soup.find_all('h4')

# Find all a elements
a_elements = soup.find_all('a')

# Create empty lists to store data
h2_data = []
h4_data = []
a_text_data = []
a_href_data = []

# Loop through h2 elements
for h2 in h2_elements:
    h2_data.append(h2.text.strip())

# Loop through h4 elements
for h4 in h4_elements:
    h4_data.append(h4.text.strip())

# Loop through a elements
for a in a_elements:
    a_text_data.append(a.text.strip())
    if a.has_attr('href'):  # Check if a has href attribute
        a_href_data.append(a['href'])
    else:
        a_href_data.append('')  # or some default value

# Create Pandas table
df = pd.DataFrame({
    # 'h2': h2_data,
    # 'h4': h4_data,
    'Value': a_text_data,
    'Link': a_href_data
})


df = df.iloc[13:294]
df = df.reset_index(drop=True)

df.insert(loc=0, column='Параметр', value=[None]*len(df))
df.insert(loc=1, column='Пол', value=[None]*len(df))

df.loc[:30, 'Пол'] = 'Женские и Мужские'
df.loc[:30, 'Параметр'] = 'Имена по буквам'

df.loc[31:83, 'Пол'] = 'Женские'
df.loc[84:134, 'Пол'] = 'Мужские'
df.loc[31:134, 'Параметр'] = 'Имена по стране'

df.loc[135:158, 'Пол'] = 'Женские'
df.loc[159:182, 'Пол'] = 'Мужские'
df.loc[135:182, 'Параметр'] = 'Имена по региону'

df.loc[183:203, 'Пол'] = 'Женские'
df.loc[204:224, 'Пол'] = 'Мужские'
df.loc[183:224, 'Параметр'] = 'Имена по группам'

df.loc[225:249, 'Пол'] = 'Женские'
df.loc[250:280, 'Пол'] = 'Мужские'
df.loc[225:280, 'Параметр'] = 'Имена по значению'

df

df.to_csv(r'C:\Users\aleksandra.babkina\Desktop\Список_ссылок_с_именами_с_сайта.csv', index=False)

df.to_csv(r'Список_ссылок_с_именами_с_сайта.csv', index=False)



