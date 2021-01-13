from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time

# for page 2+, search term is <search term>/2
search_term = "kanahei"
url = "https://stickers.cloud/search/" + search_term

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = Request(url, headers=hdr)
url_html = urlopen(req).read()
soup = BeautifulSoup(url_html)
pack_divs = soup.findAll("div", {"class": "md-title"})
print(pack_divs)