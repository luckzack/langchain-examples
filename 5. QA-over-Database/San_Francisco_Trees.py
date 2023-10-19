# 生成 San_Francisco_Trees.db

# 原始数据 https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-28/Street_Tree_Map.csv

# 将 csv 转成 sqlite db

import csv
import sqlite3

# 打开CSV文件和SQLite数据库连接
with open('../data/San_Francisco_Trees.csv', 'r') as csv_file:
    with sqlite3.connect('../data/San_Francisco_Trees.db') as conn:
        cursor = conn.cursor()

        # 创建表格
        cursor.execute('''CREATE TABLE IF NOT EXISTS trees
                          (TreeID INTEGER, qLegalStatus TEXT, qSpecies TEXT, qAddress TEXT,
                          SiteOrder INTEGER, qSiteInfo TEXT, PlantType TEXT, qCaretaker TEXT,
                          qCareAssistant TEXT, PlantDate TEXT, DBH TEXT, PlotSize TEXT,
                          PermitNotes TEXT, XCoord TEXT, YCoord TEXT, Latitude TEXT,
                          Longitude TEXT, Location TEXT)''')

        # 读取CSV文件并将数据插入到数据库
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''INSERT INTO trees
                              (TreeID, qLegalStatus, qSpecies, qAddress, SiteOrder, qSiteInfo,
                              PlantType, qCaretaker, qCareAssistant, PlantDate, DBH, PlotSize,
                              PermitNotes, XCoord, YCoord, Latitude, Longitude, Location)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (row['TreeID'], row['qLegalStatus'], row['qSpecies'], row['qAddress'],
                            row['SiteOrder'], row['qSiteInfo'], row['PlantType'], row['qCaretaker'],
                            row['qCareAssistant'], row['PlantDate'], row['DBH'], row['PlotSize'],
                            row['PermitNotes'], row['XCoord'], row['YCoord'], row['Latitude'],
                            row['Longitude'], row['Location']))

        # 提交更改并关闭数据库连接
        conn.commit()
