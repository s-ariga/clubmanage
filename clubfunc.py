# Copyright (c) 2019 Seiichi Ariga
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-

"""
Created on Mon Apr 29 13:59:31 2019

@author: seiic

v0.5: 出力ファイル名を日本語に変更した
v0.6: 秋の大会用。10 Proneないので、コメントアウト
v0.7: 2021 5月用 10mPR復活
v0.8: 2022 7月用 10mPRも同じエントリーシート
v0.9: 2023 7月用 種目名変更 FR3X20 -> R3PMなど

"""
import pandas as pd

touroku = '団体登録する'

# TODO: 設定ファイルを別に作って読み込むことにする

shumoku_10m = [
    'ARM',
    'ARW'
    #    'AR60PR' # 秋の大会ではない種目
]

shumoku_50m = [
    'R3PM',
    'RPRM',
    'R3PW',
    'RPRW'
]

# 10mと50m両方の種目名

shumoku_team = shumoku_10m + shumoku_50m # 総合団体に使う種目
shumoku = shumoku_team + ['ARMIX'] # 上+ARMIX or AR60PR

shumoku_10m = [
    'AR60PR団体',
    'AR60PR個人'
]

# 種目名リスト
# ? 'D'ってついてる種目はなんだっけ？
shumoku_dk = [
    'AR60D',
    'AR60',
    'R3PW',
    'R3PM',
    'RPRW',
    'RPRM',
    'AR60WD',
    'AR60W',
    'ARMIX'
]

# 団体登録のある種目
dantai_list = [
    'R3PM団体登録',
    'RPRM団体登録',
    'AR60団体登録',
    'R3PW団体登録',
    'RPRW団体登録',
    'AR60W団体登録'
]

# SB = 7,500 Yen, AR = 3,500 Yen
# 団体登録 = 6,000 Yen
price = {
    'R3PM': 7500,
    'RPRM': 7500,
    'ARM': 3500,
    'R3PW': 7500,
    'RPRW': 7500,
    'ARW': 3500,
    'ARMIX': 3500,
    'AR60PR': 3500, # 秋の大会には無い種目
    '団体登録': 6000
}


def sankahi_calc(shashu: pd.DataFrame, team: pd.DataFrame):
    """
    チームの射手データと団体登録データから、チームの参加費を計算

    Parameters
    -----------------------
    shashu : pandas.DataFrame
        チームの射手リスト
    team : pandas.DataFrame
        チームの団体登録

    Returns
    ----------------------
    ryokin : pandas.Series
        チームの料金
    """
    print(shashu)
    print(team)
    team_name = team['チーム名']

    ryoukin = pd.DataFrame()
    ryoukin['チーム名'] = team_name
    print(team_name)

    # 個人エントリーと団体エントリーそれぞれの人数をカウントして計算
    for s in shumoku:
        kojin = shashu[s] == '個人'
        dantai = shashu[s] == '団体'
        # それぞれの人数に競技ごとの個人エントリーフィーを掛ける
        ryoukin[s + '団体'] = dantai.sum() * price[s]
        if (dantai.sum() > 0):
            tourokuryoukin = price["団体登録"]
            if s.startswith("AR"):
                tourokuryoukin = price["団体登録"]
            ryoukin[s + '団体登録'] = tourokuryoukin
        ryoukin[s] = kojin.sum() * price[s]
    # 団体登録費の計算
    # TODO -> 団体登録費の計算バグ取り 202011
#    for s in dantai_list:
#        ryoukin[s] = price['団体登録'] if team[s].values == '団体登録する' else 0
    ryoukin['合計'] = ryoukin.sum(axis=1, numeric_only=True)
    return ryoukin


def shashu_10m(path: str) -> pd.DataFrame:
    """
    10m伏射の集計をする

    Parameters
    -----------------------
    path : str
        データ置き場のパス

    Returns
    -----------------------
    shashu_list_10m : pandas.DataFrame
        10m射手のリスト in DataFarme
    """
    
    import glob

    # 10m射手のファイルは別フォルダに置く
    DATAPATH = path
    DATAGLOB = DATAPATH + "*.xlsx"
    datalist = glob.glob(DATAGLOB)
    shashu_list_10m = pd.DataFrame([])
    for file in datalist:
        print(file)
        shashu_data_10m = pd.read_excel(file,
                                        sheet_name='申込フォーム',
                                        dtype='object')
        # リストから空欄と入力例を削除
        shashu_data_10m = shashu_data_10m.dropna(subset=['氏名']).drop(0)
        # 番号も必要ないので削除
        del shashu_data_10m['番号']
        shashu_list_10m = pd.concat([shashu_data_10m, shashu_list_10m],
                                    sort=False,
                                    ignore_index=True)
    return shashu_list_10m


def sankahi_10m_calc(sankahi: pd.DataFrame, shashu_list: pd.DataFrame) -> pd.DataFrame:
    """
    10m伏射の参加費を計算し、参加費リストに追加

    Parameters
    ----------------------
    sankahi : pandas.DataFrame
        参加費リスト
    shashu_list : pandas.DataFrame
        10m伏射射手リスト

    Returns
    -----------------------
    sankahi : pandas.DataFrame
        参加費リスト（引数で受けたものを返す）
    """
    sankahi_10m = pd.DataFrame(columns=['チーム名', 'AR60PR'])
    # チーム名でGroupbyした射手リストを作成
    groupby_10m = shashu_list.groupby('チーム名')
    for team, team_list in groupby_10m:
        # リストのカウントがエントリー射手の人数。10m登録者数リストに追加していく
        entry_count = team_list.count()['氏名']
        print('AR伏射 チーム {0} エントリー {1}人'.format(team, entry_count))
        sankahi_10m = sankahi_10m.append({
            'チーム名': team,
            'AR60PR':
            entry_count*price['AR60PR']
        }, ignore_index=True)
    # 参加費リストに上で作った10mのリストをチーム名でマージ
    print(sankahi_10m)
    sankahi = sankahi.merge(sankahi_10m, how='outer', on=['チーム名'])
    return sankahi


def shumoku_shashu_list(shashu_list: pd.DataFrame, output="../output/"):
    """
    種目別射手リストを作成し、ファイルに保存する

    Parameters
    ---------------------
    shashu_list : pandas.DataFrame
        射手のリスト in DataFrame
    output : string
        データ出力フォルダのパス
    """

    # Pandas のwriterを使って、種目別にシートを作成する
    with pd.ExcelWriter(output + '種目別射手リスト.xlsx') as writer:
        for s in shumoku:
            cols = ['姓', '名', 'ふりがな', 'チーム名']
            # SBPR以外の実施日は１つなので、希望日はなし
            # ! 2022ほぼすべての種目で希望日あり
            # ! 2022秋。そうでもない
            if s == 'ARMIX':
                cols += ['ARMIX', '特記事項']
            elif s == 'FR60PR' or s == 'R60PR':
                cols += [s, s + '\n希望日', '特記事項']
            else:
                cols += [s, '特記事項']
            s_list = shashu_list[cols].dropna(subset=[s])
            s_name = s_list['姓'].map(str) + " " + s_list['名'].map(str)
            s_list['氏名'] = s_name
            s_list.reset_index(inplace=True)
            s_list.to_excel(writer, sheet_name=s)

#        for s in shumoku_10m:
#            cols = ['氏名', 'ふりがな', 'チーム名', s, s + '希望日', '特記事項']
#            s_list = shashu_list[cols].dropna(subset=[s])
#            s_list.reset_index(inplace=True)
#            s_list.to_excel(writer, sheet_name=s)


# このファイルはモジュールなので直接実行はしません
if __name__ == '__main__':
    print("クラブ戦エントリーシート　モジュール")
    print("import clubfunc")
