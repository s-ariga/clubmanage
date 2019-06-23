# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

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
    'ARMIX'
]

event_list_50m = [
    'R3X40',
    'R60PR',
    'FR3X40',
    'FR60PR'
]

event_list = event_list_10m + event_list_50m

SIUS_event_data = pd.DataFrame([SIUS_list])

if __name__ == '__main__':
    print("クラブ専用SIUSデータモジュール")
    print("import clubSIUS")