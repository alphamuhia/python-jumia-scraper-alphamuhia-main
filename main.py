import requests
import csv

from bs4 import BeautifulSoup

url = 'https://www.jumia.co.ke/womens-jewelry/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

jewelry = soup.find_all('article', class_='prd _fb col c-prd')

data =[]

for product in jewelry:
    product_name = product.find('h3', class_='name').text
    brand_name = 'Fashion'
    product_price = product.find('div', 'prc').text
    product_discount = product.find('div', class_='bdg _dsct _sm').text
    product_revews = product.find('h2', class_='-fs14 -m -upp -ptm')
    product_rating = product.find('div', class_='stars _s').text.strip()
    data.append([product_name, brand_name, product_price, product_discount, product_revews, product_rating])

with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['product_name', 'brand_name', 'product_price', 'product_discount', 'product_reviews', 'product_rating'])
    writer.writerows(data)


print("data saved to 'products.csv'")