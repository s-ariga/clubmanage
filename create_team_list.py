# Copyright (c) 2019 Seiichi Ariga
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# 射手一覧リストから、団体選手名を抜き出す

import pandas as pd
import clubfunc as cf

DATA_DIR = "../output/"
DATA_FILE = "全射手一覧.xlsx"

class club():


def create_team_list(filename):
    shashu_data = pd.read_excel(filename,
                                dtype='object')
    # print(shashu_data)
    for name in shashu_data["氏名"]:
        print(name)


if __name__ == "__main__":
    create_team_list(DATA_DIR+DATA_FILE)
