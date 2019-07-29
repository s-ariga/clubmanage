#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
日ラIDを抽出する

@s_ariga 2019
'''

import os
import glob
import pandas as pd
import numpy as np

import clubfunc as cf


DATAPATH = '../data/'
DATAPATH10M = '../data10mp60/'
DATAGLOB = DATAPATH + '*.xlsx'
DATAGLOB10M = DATAPATH10M + '*.xlsx'
OUTPUTPATH = '../output/'

if __name__ == '__main__':
    datalist = glob.glob(DATAGLOB)
    # 全射手のIDを読み込み
    shashu_id = pd.read_excel('../data/全射手ID.xlsx', dtype='object')
    for file in datalist:
        print(file)
        shashu_data = pd.read_excel(file,
                                    sheet_name='申込みフォーム',
                                    skiprows=2,
                                    dtype='object')
        shashu_data = shashu_data.dropna(subset=['氏名']).drop(0)
        del shashu_data['番号']
        team_list = pd.concat([shashu_list, shashu_data],
                              sort=False,
                              ignore_index=True)

        
