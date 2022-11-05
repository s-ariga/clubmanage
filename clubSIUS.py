'''
Seiichi Ariga <seiichi.ariga@gmail.com>
'''

import pandas as pd

# SiusRank入力のためのカラム名 + Eventを追加(groupby用)
# 詳細はSiusRank参照
SIUS_list = [
    'Event',
    'Start Number',
    'Name',
    'Fisrt Name',
    'Nation Groups',
    'Team',
    'Relay',
    'Target Number'
]

event_list_10m = [
    'AR60PR',
    'AR60PRW',
    'AR60W',
    'AR60',
    'AR40PRW'
    'ARMIX'
]

event_list_50m = [
    'R3X20',
    'R60PR',
    'FR3X20',
    'FR60PR'
]

event_list = event_list_10m + event_list_50m

SIUS_event_data = pd.DataFrame([SIUS_list])

if __name__ == '__main__':
    print("クラブ専用SIUSデータモジュール")
    print("import clubSIUS")
