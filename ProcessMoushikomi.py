# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd
import numpy as np

# 使う場合、DBはSQlite3で
import sqlite3
#from sqlite3 import Error

import clubfunc as cf

DBPATH = "../sqlite/2019club.db"
DATAPATH = "../data/"
DATAGLOB = DATAPATH + "*.xlsx"
OUTPUTPATH = "../output/"

if __name__=='__main__':
    # Excelファイルを探す
    datalist = glob.glob(DATAGLOB)
    #conn= sqlite3.connect(DBPATH)
    #cur = conn.cursor()

    team_list = pd.DataFrame([])
    shashu_list = pd.DataFrame([])
    shashu_10m_list = pd.DataFrame([])
    sankahi_list = pd.DataFrame([])

    # PandasでExcelを読み込み。射手データ読み込み
    for file in datalist:
        print(file)
        shashu_data = pd.read_excel(file, 
                                    sheet_name = '申込フォーム', 
                                    skiprows=2, 
                                    dtype='object')
    
        # 氏名空白の行は削除
        # Tip: dropメソッドは元データを改変しないので、inplace = Trueか以下が必要
        # "入力例"を削除
        shashu_data = shashu_data.dropna(subset = ['氏名']).drop(0)
        # "番号"も必要ないので削除
        del shashu_data['番号']
        # 日ラIDに'-', '_'を含めている場合があるので、replace
        #shashu_data['日ラID'] = shashu_data['日ラID'].str.replace('_', '')
        #shashu_data['日ラID'] = shashu_data['日ラID'].str.replace('-', '')
        #shashu_data['日ラID'] = shashu_data['日ラID'].str.replace(' ', '')
        
        # チーム名を最初の射手のチーム名[0, 5]から取得
        team_name = shashu_data.iloc[0, 5]
        # チームのデータを登録リストに追加
        shashu_list = pd.concat([shashu_list, shashu_data], 
                                sort = False, 
                                ignore_index = True)
    
        team_data = pd.read_excel(file, sheet_name = '申込フォーム',
                                  nrows = 1, usecols = [8,10,12,14,16,18])
        team_data['チーム名'] = team_name
        team_data = team_data.iloc[:,[6,0,1,2,3,4,5]]
        team_list = pd.concat([team_list, team_data], sort = False,
                              ignore_index = True)
        # チームの参加費を計算して参加費リストに追加
    sankahi_list = pd.concat([cf.sankahi_calc(shashu = shashu_data, team = team_data), sankahi_list], sort = False, ignore_index = True)
                   
    # 10m競技のリスト読み込み
    shashu_10m_list = cf.shashu_10m(path = '../data10mp60/')
    # 10m伏射のリストを保存
    shashu_10m_list.to_excel(OUTPUTPATH + '10m伏射射手.xlsx')

    # 10mデータ側の要らないカラムを削除

     
    shashu_list = pd.merge(shashu_list, shashu_10m_list, how='outer', on=['氏名', 'ふりがな', '日ラID', 'チーム名'])
    #shashu_list = shashu_list.rename(columns={'ふりがな_x': 'ふりがな', '日ラID_x': '日ラID', 'チーム名_x': 'チーム名'})
    # 種目ごとの射手リスト作成
    cf.shumoku_shashu_list(shashu_list)

    # 射手リスト、チームリスト、参加費一覧をExcelに出力
    shashu_list.to_excel(OUTPUTPATH + '全射手一覧.xlsx')
    team_list.to_excel(OUTPUTPATH + '全チーム一覧.xlsx')
    sankahi_list.to_excel(OUTPUTPATH + '全チーム参加費集計.xlsx')
