
# pip install requests
# pip install beautifulsoup4

import requests
import bs4

def get_bv_img(bv_num):
    url = 'https://www.bilibili.com/video/{}'.format(bv_num)
    try:
        response = requests.get(url)

        soup = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
        meta = soup.find("meta", {'itemprop':"image"})
        return meta['content']
    except Exception as e:
        print(e)
        return ''
    

if __name__ == "__main__":
    img = get_bv_img("BV1hh411f73H")
    print(img)