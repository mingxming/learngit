from bs4 import BeautifulSoup
from lxml import html
import xml
import requests, json,time,certifi,os
cur_path=os.path.abspath(os.curdir)
def get_paper(url):
    kv={'user-agent':'Mozilla/5.0'}
    f = requests.get(url,headers=kv,verify=True)
    bf=BeautifulSoup(f.text,'lxml')
    bf.encoding=bf.apparent_encoding
    a1=bf.find_all('div',class_='zm-invite-pager')
    a_bf=BeautifulSoup(str(a1),'lxml')
    a2=a_bf.find_all('span')
    return int(a2[-2].text)
    
def get_title(url):
    kv={'user-agent':'Mozilla/5.0'}
    f = requests.get(url,headers=kv,verify=True)
    bf=BeautifulSoup(f.text,'lxml')
    bf.encoding=bf.apparent_encoding
    h2=bf.find_all('h2',class_='zm-item-title')
    a_bf=BeautifulSoup(str(h2),'lxml')
    a=a_bf.find_all('a')
    for i in a:
                print(i.text)
                with open(cur_path+'\\spider_data.txt','a+') as f:
                    f.write(i.text+'\n')
def get_all_title(url,paper_num):
    a=1
    for i in range(1,paper_num+1):
                url2=url+'?page={}'.format(i)
                print(url2)
                get_title(url2)
                print('\n\n')
                
if __name__ == '__main__':
    url=input("请输入url:")
    paper_num=get_paper(url)
    get_all_title(url,paper_num)
    input("按回车结束")
