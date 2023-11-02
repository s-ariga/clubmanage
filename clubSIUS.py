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
    'ARM',
    'ARW',
    'AR60PR',
    'AR60PRW',
    'ARMIX'
]

event_list_50m = [
    'R3PM',
    'RPRM',
    'R3PW',
    'RPRW'
]

event_list = event_list_10m + event_list_50m

SIUS_event_data = pd.DataFrame([SIUS_list])

if __name__ == '__main__':
    print("クラブ専用SIUSデータモジュール")
    print("import clubSIUS")
