# -*- coding: utf-8 -*- 

import requests
import pandas as pd
import re
import csv
import os

client_id = "7xT5apJ1MOfu4xp4LyfV"
client_secret = "xXSwW40yhU"

def csv2list(filename):
    file = open(filename, 'r')
    csvfile = csv.reader(file)
    result = []
    for i, item in enumerate(csvfile):
        if i == 0:
            continue
        if len(item) > 0 and len(item[0]) > 0:
            result.append((item[0].strip(), item[1]))
    return result

def call(search_word, keyword, encode_type, max_display, sort, start):
    url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word} {keyword}&display={str(max_display)}&start={str(start)}&sort={sort}"
    headers = {'X-Naver-Client-Id' : client_id,
           'X-Naver-Client-Secret':client_secret
           }
    result = requests.get(url, headers=headers)
    return result

def clean_html(x):
    x = re.sub("\&\w*\;","",x)
    x = re.sub("<.*?>","",x)
    return x

def data2csv(company, keyword, data, filename):
    df = pd.DataFrame(data.json()['items'])
    if not df.empty:
        df = df.reindex(columns=['id', 'companyname', 'keyword', 'title', 'description', 'originallink','link','pubDate'])
        df['companyname'] = company
        df['keyword'] = keyword
        df['title'] = df['title'].apply(lambda x: clean_html(x))
        df['description'] = df['description'].apply(lambda x: clean_html(x))
        if os.path.exists(filename):
            df.to_csv(filename, index=False, mode='a', encoding='utf-8-sig', header=False)
        else:
            df.to_csv(filename, index=False, mode='w', encoding='utf-8-sig')

def run():
    #init
    inputfilename = "preprocessed_companyList.csv"
    companyList = csv2list(inputfilename)
    datadir="./output/"
    outputfilename = datadir + "single_preprocessed_news_result.csv"
    # keywordList = ["", " 기부", " 검찰", " 공정위", " 나눔", " 불매", " 윤리"]
    # keywordList = [""]

    encode_type = "json"
    max_display = 1
    sort = "sim"
    start = 1
    
    #api call
    for row in companyList:
        company = row[0]
        group = row[1]
        keyword = ""
        # for keyword in keywordList:
        data = call(company, keyword, encode_type, max_display, sort, start)
        data2csv(company, keyword, data, outputfilename) 

run()
