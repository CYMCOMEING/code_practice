import requests
from bs4 import BeautifulSoup
import re
import time
import json
# 格式化输出.prettify()

base_url = 'https://wiki.52poke.com/'


def get_dex_data():
    """
    全国图鉴网页
    """
    response = requests.get(
        'https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88')
    html = response.text
    with open('dex_data.html', 'w', encoding='utf-8') as f:
        f.write(html)


def parse_dex_data(html):
    """
    全国图鉴提取数据到txt
    """
    soup = BeautifulSoup(html, features="lxml")
    table = soup.find(
        'table', class_='a-c roundy eplist bgl-神奇宝贝百科 b-神奇宝贝百科 bw-2')
    trs = table.tbody.find_all('tr')
    del trs[0]
    del trs[0]

    dex_list = []
    era = ''
    for tr in trs:
        if 'colspan' in tr.td.attrs:
            era = tr.a.text
        else:
            num = tr.td.text.strip()
            name_zh = tr.find_all('td')[1].text.strip()
            dex_list.append({'era': era, 'num': num, 'name_zh': name_zh})

    return dex_list


def get_detail_data(name):
    """
    获取一个精灵详情页
    """
    url = 'https://wiki.52poke.com/wiki/'+name
    response = requests.get(url)
    html = response.text
    with open(name+'.html', 'w', encoding='utf-8') as f:
        f.write(html)


def parse_detail_data(html):
    """
    提取精灵详情页数据到json
    """
    soup = BeautifulSoup(html, features="lxml")
    table = soup.find('div', class_='mw-parser-output').find_all('table')[3]

    trs = table.tbody.contents
    trs = [i for i in trs if i != trs[1]]

    data = {}

    # 名字
    name = trs[0].find_all('b')
    # print(name[0].text, name[1].text, name[2].text)
    data['name_zh'] = name[0].text
    data['name_jp'] = name[1].text
    data['name_en'] = name[2].text

    # 图片链接
    img_url = base_url + trs[1].a['href']
    # print(img_url)
    data['img_url'] = img_url

    # 属性type
    tag_a = table.find('a', title='属性').parent.parent.find_all('a')
    attr_1 = tag_a[2].text

    if len(tag_a) > 3:
        attr_2 = tag_a[4].text
    else:
        attr_2 = ''
    # print(attr_1, attr_2)
    data['attr_1'] = attr_1
    data['attr_2'] = attr_2

    # 分类Category
    category = table.find('a', title='分类').parent.parent.table.text
    # print(category)
    data['category'] = category.strip()

    # 特性Ability
    ability = table.find('a', title='特性').parent.parent.table.find_all('a')
    # print(ability[0].text,ability[1].text)
    hide_ability = table.find(
        'a', title='特性').parent.parent.table.find_all('small')
    # print(hide_ability)
    if hide_ability:
        data['hide_ability'] = ability[-1].text
        ability.pop()

    data['ability'] = [i.text for i in ability]

    # 身高 high
    high = table.find('a', title='宝可梦列表（按身高排序）').parent.parent.table.text
    # print(high)
    data['high'] = high.strip()

    # 重量weight
    weight = table.find('a', title='宝可梦列表（按体重排序）').parent.parent.table.text
    # print(weight)
    data['weight'] = weight.strip()

    # 捕获率Catch Rate 1~255
    catch_rate = table.find('a', title='捕获率').parent.parent.table.td
    # 普通的精灵球在满体力下的捕获率
    # print(catch_rate.small.text)
    if catch_rate.small:
        catch_rate.small.clear()
    # print(catch_rate.text)
    data['catch_rate'] = catch_rate.text.strip()

    # 性别gender
    gender = table.find('a', title='宝可梦列表（按性别比例分类）').parent.parent.table
    for i in gender.find_all(class_='hide'):
        i.clear()
    # print(gender.text)
    data['gender'] = gender.text.strip()

    # 蛋群Egg group
    egge_group = table.find('a', title='宝可梦培育').parent.parent.table.td
    # for i in egge_group.find_all('a'):
    #     print(i.text)
    data['egge_group'] = [i.text for i in egge_group.find_all('a')]

    # 孵化周期Egg cycle
    egg_cycle = egge_group.next_sibling.next_sibling.text
    # print(egg_cycle)
    data['egg_cycle'] = egg_cycle.strip()

    # 获取努力力值Base points
    base_points = table.find('a', title='基础点数').parent.parent.table.tr.text
    # print(base_points)
    data['base_points'] = base_points.strip()

    # 种族值
    # hp
    hp = soup.find('tr', class_='bgl-HP')
    hp.div.clear()
    # print(hp.th.text)
    data['hp'] = hp.th.text.strip()

    # 攻击 Attack
    attack = soup.find('tr', class_='bgl-攻击')
    attack.div.clear()
    # print(attack.th.text)
    data['attack'] = attack.th.text.strip()

    # 防御 Defense
    defense = soup.find('tr', class_='bgl-防御')
    defense.div.clear()
    # print(defense.th.text)
    data['defense'] = defense.th.text.strip()

    # 特攻 Special Attack
    sattack = soup.find('tr', class_='bgl-特攻')
    sattack.div.clear()
    # print(sattack.th.text)
    data['sattack'] = sattack.th.text.strip()

    # 特防 Special Defense
    sdefense = soup.find('tr', class_='bgl-特防')
    sdefense.div.clear()
    # print(sdefense.th.text)
    data['sdefense'] = sdefense.th.text.strip()

    # 速度 Speed
    speed = soup.find('tr', class_='bgl-速度')
    speed.div.clear()
    # print(speed.th.text)
    data['speed'] = speed.th.text.strip()

    # 种族值总和 Species strength
    species_strength = speed.next_sibling.next_sibling
    species_strength.div.clear()
    # print(species_strength.text)
    data['species_strength'] = species_strength.text.strip()

    return json.dumps(data, ensure_ascii=False)

def data_to_sql():
    """
    创建表头
    create 
    num name_zh name_jp name_en img_url attr_1 attr_2 category 
    ability_1 ability_2 hide_ability high weight catch_rate gender
    egge_group egg_cycle base_points hp attack defense sattack sdefense
    speed species_strength
    """
    csql = """
    create table if not exists PokeData (
        num integer primary key,
        name_zh text,
        name_jp text,
        name_en text,
        img_url text,
        attr_1 text,
        attr_2 text,
        category text,
        ability_1 text,
        ability_2 text,
        hide_ability text,
        high int,
        weight int,
        catch_rate text,
        gender text,
        egge_group text,
        egg_cycle text,
        base_points text,
        hp int,
        attack int,
        defense int,
        sattack int,
        sdefense int,4
        speed int,
        species_strength int,
        );"
    """
    pass


if __name__ == "__main__":
    # 获取图鉴
    # get_dex_data()
    # 提取图鉴网页中的数据
    # html = ''
    # with open('dex_data.html', 'r', encoding='utf-8') as f:
    #     html = f.read()
    # if html:
    #     data = parse_dex_data(html)
    #     with open('dex_data.txt', 'w', encoding='utf-8') as f:
    #         for i in data:
    #             f.write(i['name_zh'] + '\n')

    # 每个宝可梦详情网页
    # with open('dex_data.txt', 'r', encoding='utf-8') as f:
    #     while True:
    #         name = f.readline()
    #         if not name:
    #             break
    #         try:
    #             name = name.strip()
    #             print(name)
    #             get_detail_data(name)
    #             time.sleep(1)
    #         except Exception as e:
    #             print(name, e)

    with open('poke_data.txt', 'a+', encoding='utf-8') as f1:
        with open('dex_data.txt', 'r', encoding='utf-8') as f2:
            while True:
                name = f2.readline()
                if not name:
                    break
                html = ''
                name = name.strip()
                print(name)
                with open(name + '.html', 'r', encoding='utf-8') as f3:
                    html = f3.read()
                if html:
                    data = parse_detail_data(html)
                    f1.write(data+'\n')
    