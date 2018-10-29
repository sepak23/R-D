
# coding: utf-8

# In[1]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import pandas as pd


# In[2]:


myurl="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tid=6662"


# In[3]:


uClient=uReq(myurl)


# In[4]:


page_html=uClient.read()


# In[6]:


uClient.close()


# In[7]:


page_soup=soup(page_html,"html.parser")


# In[8]:


page_soup.h1


# In[9]:


containers=page_soup.findAll("div",{"class":"item-container"})


# In[11]:


len(containers)


# In[106]:


filename='/Users/sepehrpiri/Documents/python_games/my_first_web_scraping.csv'


# In[120]:


brands=[]
titles=[]
prices=[]
shippings=[]


# In[121]:


for container in containers:
    brand=container.div.div.a.img['title']
    title=container.findAll("a",{"class":"item-title"})[0].text
    pricelist=re.findall(r'\d+',container.div.findAll("li",{"class":"price-current"})[0].text.strip())
    price=pricelist[0]+'.'+pricelist[1]
    shipping=container.findAll("li",{"class":"price-ship"})[0].text.strip()
    brands.append(brand)
    titles.append(title)
    prices.append(price)
    shippings.append(shipping)

    


# In[123]:


d = {'brand': brands,
         'title': titles,
         'price': prices,
         'shipping': shippings}
df = pd.DataFrame.from_dict(d)


# In[127]:


df.to_csv('/Users/sepehrpiri/Documents/python_games/my_first_web_scraping.csv')

