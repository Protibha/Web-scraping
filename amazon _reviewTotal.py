import requests
from bs4 import BeautifulSoup
import pandas as pd

import time

url = 'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

source = requests.get(url)
soup = BeautifulSoup(source.content,'html.parser')
#print(soup)

names = soup.find_all('span',class_='a-profile-name')
#print(names)
cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
#print(cust_name)
cust_name.pop(0)
#print(len(cust_name))
cust_name.pop(0)
#print(len(cust_name))

title = soup.find_all('a',class_='review-title-content')
#print(title)
review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
#print(review_title)
review_title[:] = [titles.lstrip('\n') for titles in review_title]
#print(review_title)
review_title[:] = [titles.rstrip('\n') for titles in review_title]
#print(review_title)

rating = soup.find_all('i',class_='review-rating')
#print(rating)
rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
#print(rate)
rate.pop(0)
#print(rate)
rate.pop(0)
#print(rate)

review = soup.find_all("span",{"data-hook":"review-body"})
#print(review)
review_content = []
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
#print(review_content)
review_content[:] = [reviews.lstrip('\n') for reviews in review_content]
#print(review_content)
review_content[:] = [reviews.rstrip('\n') for reviews in review_content]
#print(review_content)

#print(cust_name)
#print(review_title)
#print(rate)
#print(review_content)

df = pd.DataFrame()
df['Customer Name']=cust_name
#print(df)
df['Review title']=review_title
df['Ratings']=rate
df['Reviews']=review_content
#print(df)

df.to_csv('reviews.csv')
print('Written to CSV file')

time.sleep(5)

import emailattach
