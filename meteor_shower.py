import requests
from bs4 import BeautifulSoup
from main import *

url = 'https://www.imo.net/members/imo_showers/working_shower_list'
r = requests.get(url)
sp = BeautifulSoup(r.text,'html.parser')
list_meteor_shower=[['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level'] for i in range(6)]
meteor_shower_list=['QUA', 'PER', 'GEM', 'LYR', 'ORI', 'LEO']
meteor_shower_name_c_list=['象限儀座流星雨', '英仙座流星雨', '雙子座流星雨', '天琴座流星雨','獵戶座流星雨', '獅子座流星雨']
meteor_shower_name_e_list=['Quadrantids', 'Perseids', 'Geminids', 'Lyrids', 'Orionids', 'Leonids']


for i in range(6):
    for para in sp.find_all("tbody"):
        for rrlist in para.find_all('tr'):
            if rrlist.find_all('td')[0].getText() == meteor_shower_list[i]:
                ZHR=rrlist.find_all('td')[9].getText()
                Peak=rrlist.find_all('td')[3].getText()
                list_meteor_shower[i][0]=meteor_shower_name_c_list[i]
                list_meteor_shower[i][1]=meteor_shower_name_e_list[i]
                Date_name=list(Peak.replace(" ", ""))
                Date_name[0:2], Date_name[2:5] = Date_name[3:5], Date_name[0:3]                
                list_meteor_shower[i][2]=''.join(Date_name)+str(year)
                list_meteor_shower[i][3]=''
                list_meteor_shower[i][4]='ZHR=' + ZHR + ' Please update ZHR, Date and Time.'
                if i <3:
                    list_meteor_shower[i][5]=1
                else:
                    list_meteor_shower[i][5]=2
                print(list_meteor_shower[i])
                
