# -*- coding: utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

# 爬取内容：
#   NBA && CBA & 国足 & 国际足球 & 综合

import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from utils import download_page

urlcol = ['http://sports.163.com/special/000587PK/newsdata_nba_index.js?callback=data_callback',
'http://sports.163.com/special/000587PN/newsdata_world_index.js?callback=data_callback',
'http://sports.163.com/special/000587PM/newsdata_china_index.js?callback=data_callback',
'http://sports.163.com/special/000587PQ/newsdata_allsports_index.js?callback=data_callback']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}


# 收集标题的list
def sportsdict():
    for url in urlcol:
        result = download_page.download_html_waitting(url,headers,1)
        result = str(result, encoding = "gbk").replace("data_callback(", '{"data_callback":', 1)[:-1] + "}"
        result = json.loads(result,strict=False)
        items = result['data_callback']
        for item in items:
            title = item['title']
            docurl = item['docurl']
            print(title, docurl)
            soup = download_page.download_soup_waitting(docurl, headers, 1)
            try:
                post = soup.find('div', id="endText")
                if post is None:
                    print ("格式不相符")
                else:
                    text = post.get_text().strip()
                    result = text.replace('\n', '')
                    print(result)
            except:
                print ("Except -- ，跳往下一链接")

if __name__ == '__main__':
    sportsdict()