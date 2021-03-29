import requests
import bs4


def get_img_url(bv_num):
    url = 'https://www.bilibili.com/video/{}'.format(bv_num)
    try:
        response = requests.get(url)

        soup = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
        meta = soup.find("meta", {'itemprop': "image"})
        return meta['content']
    except Exception as e:
        print(e)
        return ''


def download_url(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

def get_video_pic(bv_num):
    pic_name = ''
    pic_url = get_img_url(bv_num)
    if pic_url:
        pic_name = pic_url.split('/')[-1]
        download_url(pic_url, pic_name)
    return pic_name

if __name__ == "__main__":
    get_video_pic("BV1hh411f73H")
