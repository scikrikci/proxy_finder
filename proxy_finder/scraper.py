from bs4 import BeautifulSoup as bs4
from time import sleep
import requests
import json
import os

proxy_sites_url = "https://socks-proxy.net/"
total_proxys = []

class Scrap:
    def start(self):
        # banned_site_url = "https://www.gsmarena.com/"
        
        r= requests.get(proxy_sites_url)
        soup = bs4(r.content,"html.parser")

        data = soup.find_all("table",{"class":"table table-striped table-bordered"})
        # print(data)

        tablo = (data[0].contents)[len(data[0].contents)-1]
        # print(tablo)

        tablo = tablo.find_all("tr")
        # print(tablo)

        for tr in tablo:
            # httpss = tr.find_all("td")[6].text
            port = tr.find_all("td")[0].text
            ip = tr.find_all("td")[1].text

            proxy = f"{port}:{ip}"

            total_proxys.append(proxy)

        # print(json.dumps(total_proxys,indent=4))
        write_json()

def write_json():
    json_string = json.dumps(total_proxys,indent=4)
    _path = os.getcwd()+f'/data/{_name()}_total.json'
    with open(_path, 'w') as outfile:
        json.dump(json_string, outfile)

def _name():
    total_files = os.listdir(os.getcwd()+'/data')
    return str(len(total_files))