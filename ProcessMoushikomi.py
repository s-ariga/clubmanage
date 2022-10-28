# Copyright (c) 2019 Seiichi Ariga
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-

"""
各チームのクラブ戦エントリーを集計するスクリプト

@s_ariga 2019

"""
import glob
import pandas as pd

import clubfunc as cf

DBPATH = "../sqlite/2019club.db"
DATAPATH = "../data/"
DATAGLOB = DATAPATH + "*.xlsx"
OUTPUTPATH = "../output/"
print("before moushikoni")

if __name__ == '__main__':
    # Excelファイルを探す
    datalist = glob.glob(DATAGLOB)
    team_list = pd.DataFrame([])
    shashu_list = pd.DataFrame([])
    shashu_10m_list = pd.DataFrame([])
    sankahi_list = pd.DataFrame([])

    # PandasでExcelを読み込み。射手データ読み込み
    print(datalist)
    for file in datalist:
        print(file)
        shashu_data = pd.read_excel(file,
                                    sheet_name='申込フォーム',
                                    skiprows=2,
                                    dtype='object')
        # 氏名空白の行は削除
        # Tip: dropメソッドは元データを改変しないので、inplace = Trueか以下が必要
        # "入力例"を削除
        shashu_data = shashu_data.dropna(subset=['姓']).drop(0)
        # "番号"も必要ないので削除
        del shashu_data['番号']
        # shashu_data = shashu_data['日ラID'].replace('-', '')
        # shashu_data = shashu_data['日ラID'].replace(' ', '')
        # shashu_data = shashu_data['日ラID'].replace('_', '')
        # チーム名を最初の射手のチーム名[0, 7]から取得
        team_name = shashu_data.iloc[0, 7]
        # チーム名を入力していない場合、エラーを出して終了
        if team_name == "":
            print("team_name が空です")
            print(file)
            exit()
        print(file)
        print(shashu_data["チーム名"])
        # チームのデータを登録リストに追加
        shashu_list = pd.concat([shashu_list, shashu_data], sort=False,
                                ignore_index=True)
        # INFO: 種目のセルは、年度によって違う
        team_data = pd.read_excel(file,
                                  sheet_name='申込フォーム',
                                  nrows=1,
                                  usecols=[9, 11, 13, 15, 17, 19])
        team_data['チーム名'] = team_name
        team_data = team_data.iloc[:, [6, 0, 1, 2, 3, 4, 5]]
        team_list = pd.concat([team_list, team_data], sort=False,
                              ignore_index=True)
        # チームの参加費を計算して参加費リストに追加
        sankahi_list = pd.concat([cf.sankahi_calc(shashu=shashu_data,
                                                  team=team_data),
                                  sankahi_list],
                                 sort=False,
                                 ignore_index=True)
    # 10m競技のリスト読み込み
#    shashu_10m_list = cf.shashu_10m(path='../data10mp60/')
    # 10m伏射の参加費を計算
#    sankahi_list = cf.sankahi_10m_calc(sankahi_list, shashu_10m_list)
#    sankahi_list = sankahi_list.fillna(0)
    # 他の競技の参加費合計にAR60PRの参加費を加算
#    sankahi_list['総合計'] = sankahi_list['合計'] + sankahi_list['AR60PR']
#    sankahi_list['振込日'] = ''
    # 10m伏射のリストを保存
#    shashu_10m_list.to_excel(OUTPUTPATH + '10m伏射射手.xlsx')
    # 10m伏射とその他競技のデータをマージ
    # その前に、'日ラID'の列をstrにキャスト。何故かint型が混じるので
    ##shashu_list['日ラID'] = shashu_list['日ラID'].astype(str)
#    shashu_10m_list['日ラID'] = shashu_10m_list['日ラID'].astype(str)
#    shashu_list = pd.merge(shashu_list, shashu_10m_list,
#                           how='outer',
#                           on=['氏名', 'ふりがな', '日ラID', 'チーム名'])
    # 種目ごとの射手リスト作成
    cf.shumoku_shashu_list(shashu_list)

    # 射手リスト、チームリスト、参加費一覧をExcelに出力
    shashu_list.to_excel(OUTPUTPATH + '全射手一覧.xlsx')
    # 請求書の作成に必要なCSVも出力 2022
    shashu_list.to_csv(OUTPUTPATH + '全射手一覧.csv')
    team_list.to_excel(OUTPUTPATH + '全チーム一覧.xlsx')
    sankahi_list.to_excel(OUTPUTPATH + '全チーム参加費集計.xlsx')
