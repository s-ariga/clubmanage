# Copyright (c) 2019 Seiichi Ariga
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-



"""
Created on Sun Apr 28 14:47:53 2019

@author: seiic
"""
import pandas as pd


class shashu:
    def setEntry(self, row):
        self.name = row['氏名']
        self.name = row['ふりがな']
        self.name = row['日ラID']
        self.name = row['役員資格']
        self.name = row['出役可能日']
        self.name = row['チーム名']
        self.name = row['FR3x40']
        self.name = row['FR3x40希望日']
        self.name = row['FR60PR']
        self.name = row['FR60PR']
        self.name = row['AR60']
        self.name = row['AR60']
        self.name = row['R3x40']
        self.name = row['R3x40']
        self.name = row['R60PR']
        self.name = row['R60PR']
        self.name = row['AR60W']
        self.name = row['AR60W']
        self.name = row['ARMIX']
        self.name = row['ARMIXチーム名']
        self.name = row['特記事項']

    def output(self, row):
        pass

if __name__ == "__main__":
    pass