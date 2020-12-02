# -*- coding: utf-8 -*- 

import requests
import pandas as pd
import re
import csv
import os
import preprocessing

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
    try:
        df = pd.DataFrame(data.json()['items'])
        if not df.empty:
            df = df.reindex(columns=['id', 'companyname', 'keyword', 'title', 'description', 'originallink','link','pubDate'])
            df['companyname'] = company
            df['keyword'] = keyword
            df['title'] = df['title'].apply(lambda x: clean_html(x))
            df['description'] = df['description'].apply(lambda x: clean_html(x))
            if (df.shape[0] > 1):
                titles = df.loc[:, 'title']
                check = preprocessing.cos_similarity(titles)
                if (len(check) == 1 and check[0] > 20):
                    df = df.drop(df.index[1])
                elif (len(check) > 1):
                    threshold = [check.index(x) for x in check if x > 20]
                    if len(threshold) > 1:
                        df = df.drop(df.index[1, 2])
                    elif len(threshold) == 1:
                        df = df.drop(df.index[min(threshold[0] + 1, 2)])
            if os.path.exists(filename):
                df.to_csv(filename, index=False, mode='a', encoding='utf-8-sig', header=False)
            else:
                df.to_csv(filename, index=False, mode='w', encoding='utf-8-sig')
    except:
        print ("error")

def run():
    #init
    inputfilename = "preprocessed_companyList.csv"
    companyList = csv2list(inputfilename)
    datadir="./triple_output/"
    keywordList = ["", "윤리경영", "친환경 생산", "검찰", "공정위", "기부 나눔활동", "공익캠페인", "봉사활동", "불매", "갑질", "위생검사"]

    encode_type = "json"
    max_display = 3
    sort = "sim"
    start = 1
    for keyword in keywordList:
        outputfilename = "preprocessed_news_result_" + keyword + ".csv"
        #api call
        for row in companyList:
            company = row[0]
            group = row[1]
            # for keyword in keywordList:
            data = call(company, keyword, encode_type, max_display, sort, start)
            data2csv(company, keyword, data, outputfilename) 

run()
