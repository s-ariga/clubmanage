"""
Seiichi Ariga <seiichi.ariga@gmail.com>
"""


class shashu:
    def setEntry(self, row):
        self.name = row['氏名']
        self.name = row['ふりがな']
        self.name = row['日ラID']
        self.name = row['役員資格']
        self.name = row['出役可能日']
        self.name = row['チーム名']
        self.name = row['FR3x20']
        self.name = row['FR3x20希望日']
        self.name = row['FR60PR']
        self.name = row['FR60PR希望日']
        self.name = row['AR60']
        self.name = row['AR60希望日']
        self.name = row['R3x20']
        self.name = row['R3x20希望日']
        self.name = row['R60PR']
        self.name = row['R60PR希望日']
        self.name = row['AR60W']
        self.name = row['AR60W希望日']
        self.name = row['ARMIX']
        self.name = row['ARMIXチーム名']
        self.name = row['特記事項']

    def output(self, row):
        pass


if __name__ == "__main__":
    pass
