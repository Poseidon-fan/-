# 以下几个库需要pip下载
# 所爬取的文件保存在和本py文件相同的目录下，文件名为用户选择的歌曲名
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import requests

NAME = ''


def scrape_target_url(browser, url):
    global NAME
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    datas = soup.find_all(name='li', attrs={'class': 'clearfix'})
    tar_locations = browser.find_elements(By.CLASS_NAME, 'song_name')
    num = 0
    for tar_location in tar_locations:
        data = datas[num]
        name = data.find(name='a', attrs={'class': 'song_name'}).attrs['title']
        print(num+1, name)
        num = num + 1

    which = int(input('输入选择下载的歌曲的编号\n'))
    NAME = datas[which-1].find(name='a', attrs={'class': 'song_name'}).attrs['title']
    tar_locations[which-1].click()
    sleep(1)
    browser.switch_to.window(browser.window_handles[-1])
    return browser.page_source


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    url = soup.find(name='audio', attrs={'class': 'music'}).attrs['src']
    res = requests.get(url).content
    with open(NAME+'.mp3', 'wb') as f:
        f.write(res)


def main():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    BASE_URL = 'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord='
    target = input('输入要下载的歌曲的名称\n')
    BASE_URL = BASE_URL + target
    html = scrape_target_url(browser, BASE_URL)

    parse_html(html)
    print('下载成功')


if __name__ == '__main__':
    main()


