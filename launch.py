# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:24 
# @Software: PyCharm
"""
import os

from cawler_pages import page_douban, page_movie, page_esports, page_news, page_sinablog, page_sports, page_toutiao
from globalVariable import fpath

print("--------------#### 任务正在启动 ####-----------------")


path_list=['douban','esports','movie','news','sinablog','sports','toutiao']

#
# # 清除上次运行结果
# for path in path_list:
#     final_path = fpath + '\\cawler_result\\' + path +".txt"
#     if os.path.exists(final_path):
#         os.remove(final_path)
#
# # 爬取豆瓣信息
# print("——————开始爬取豆瓣内容———————")
# page_douban.doubanCrawler(fpath+'\\cawler_result\\'+'douban.txt')
# # 爬取电竞信息
# print("——————开始爬取电竞内容———————")
# page_esports.esportsCrawler(fpath+'\\cawler_result\\'+'esports.txt')
# # 爬取电影信息
# print("——————开始爬取电影内容———————")
# page_movie.hotmovieCrawler(fpath+'\\cawler_result\\'+'movie.txt')
# # 爬取新闻信息
# print("——————开始爬取新闻内容———————")
# page_news.newsCrawler(fpath+'\\cawler_result\\'+'news.txt')
# # # 爬取微博信息
# print("——————开始爬取新浪内容———————")
# page_sinablog.sinaCrawler(fpath+'\\cawler_result\\'+'sinablog.txt')
# # # 爬取体育信息
# print("——————开始爬取体育内容———————")
# page_sports.sportCrawler(fpath+'\\cawler_result\\'+'sports.txt')
# # 爬取头条信息
# print("——————开始爬取头条内容———————")
# page_toutiao.toutiaoCrawler(fpath+'\\cawler_result\\'+'toutiao.txt')


# 调分词脚本
fenci = ['\\jieba_md\\jieba_fenci.py','\\new_word_md\\demo_run.py','\\word_seg_md\\newWordsFind.py']


for f in fenci:
    print('开始执行分词--'+fpath + f)
    for line in os.popen(fpath + f):
        print(line)


print('------------任务结束--------------')