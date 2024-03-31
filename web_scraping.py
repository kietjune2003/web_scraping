
from itertools import zip_longest
import pandas as pd
import requests
from bs4 import BeautifulSoup
response = requests.get("https://swe.vn/collections/all?sort_by=best-selling")

soup = BeautifulSoup(response.content,'html.parser')
pro_name = []
pro_price = []
pro_items = soup.findAll('div',class_='product-content')
for pro in pro_items:
    pro_name.append(pro.find('a').text.strip())
    pro_price.append(pro.find('span',class_='regular-price').text.strip())
data = list(zip_longest(pro_name,pro_price))
pf = pd.DataFrame(data,columns=["Tên sản phầm","Giá thành"])
pf.to_csv("Product.csv",index=False)




    




