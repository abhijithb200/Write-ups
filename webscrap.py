import requests
from bs4 import BeautifulSoup
from mdutils.mdutils import MdUtils
from mdutils import Html

url = "https://pentester.land/list-of-bug-bounty-writeups.html#bug-bounty-writeups-published-in-2021"

mdFile = MdUtils(file_name='Subdomain takeover', title='Subdomain takeover')


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
flag=0

catlist=[]
# i=3
# while i<=len(soup.find_all('td')):
#     test = soup.find_all('td')[i].text
#     catlist.append(test)
#     i+=6
    
# print(catlist,"\n")
# unique_numbers = list(set(catlist))
# print(unique_numbers)


# print(len(catlist))
# print(len(unique_numbers)) 
i=1

while i<len(soup.find_all('tr')):
    category = soup.find_all('tr')[i].text.split('\n')[4]
    
    items = []
    if "Subdomain takeover" in category:
        link = soup.find_all('tr')[i].a['href']
        all_list = soup.find_all('tr')[i].text.split('\n')
        heading = soup.find_all('tr')[i].text.split('\n')[1]
        
        print(f"{i} of {len(soup.find_all('tr'))} ")
        
        items.append(f"{ mdFile.new_inline_link(link=link, text=heading)}\t{category}")
        mdFile.new_list(items=items)
    
        
    
    i+=1


# print(catlist,"\n")
# unique_numbers = list(set(catlist))
# print(unique_numbers)

# print(len(catlist))
# print(len(unique_numbers)) 
mdFile.create_md_file()