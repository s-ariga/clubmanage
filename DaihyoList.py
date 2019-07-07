#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
各チームの代表者リストを作成する
'''

import os
import glob
import re
import pandas as pd

import clubfunc as cf

DATA_PATH = "../dataclub/"
DATA_GLOB = DATA_PATH + "*.xlsx"
OUTPUT_PATH = "../output/"
OUTPUT_FILE = OUTPUT_PATH + "クラブ代表者リスト.xlsx"

'''
2019年クラブ登録ファイル(Excel) sheet_name(クラブ情報)
pandasで読んだときのフォーマット

  Unnamed: 0                クラブ登録者名簿
0       西暦年度                  string
1        提出日      date
2       クラブ名                string
3      代表者氏名                   string
4   代表者email                   string
5    代表者電話番号           string

sheet_name(メンバー情報)
No.	姓	名	ふりがな	性別	日ラ会員ID	生年月日	郵便番号	都道府県	現住所	電話番号	勤務先（学校）	勤務先(学校)電話番号

'''

def DaihyoList():
    data_list = glob.glob(DATA_GLOB)
    daihyo_list = pd.DataFrame([])
    
    # クラブ登録ファイルから代表リスト作成する
    for n, file in enumerate(data_list):
        print(file)
        team_data = pd.read_excel(file, sheet_name='クラブ情報',dtype='object')
        team_member = pd.read_excel(file, sheet_name='メンバー情報',dtype='object')
        
        team_data.rename(columns={'クラブ登録者名簿':n},
                         inplace=True)
        line = team_data.iloc[[2,3,4,5],[1]].T
        print(line)
        daihyo_name = str(line.iat[0, 1])
        #print(daihyo_name)
        team_member.dropna(subset=['姓'], inplace=True)
        for index, member in team_member.iterrows():
            sei = str(member['姓'])
            mei = str(member['名'])
            #print(str(member['姓']) + str(member['名']))
            pattern = sei + '\s*' + mei
            print(pattern)
            print(daihyo_name)
            repattern = re.compile(pattern)
            result = repattern.match(daihyo_name)
            print(pattern + " " + daihyo_name + " " + str(result))
            if result:
                line['郵便番号'] = str(member['郵便番号'])
                line['現住所'] = str(member['現住所'])
        daihyo_list = pd.concat([daihyo_list, line])

    # 出力の整形
    daihyo_list.rename(columns={2:'クラブ名',
                                3:'代表者名',
                                4:'email',
                                5:'Tel'},
                       
                       inplace=True)
    daihyo_list.to_excel(OUTPUT_FILE)


if __name__=='__main__':
    DaihyoList()
