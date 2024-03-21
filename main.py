import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
from matplotlib.font_manager import FontProperties # *日本語対応

# ここにCSVデータを入力します
csv_data = """
日付,終値,始値,高値,安値,出来高,変化率%
2024-03-01,100,95,105,90,10000,5.26
2024-03-02,95,100,110,90,15000,-5.00
2024-03-03,96,95,105,94,12000,1.05
2024-03-04,97,96,98,95,11000,1.04
2024-03-05,94,97,100,93,13000,-3.09
"""

# CSVデータをPandas DataFrameに変換
# df = pd.read_csv(StringIO(csv_data))

# 日本語対応
fp = FontProperties(fname=r'C:\WINDOWS\Fonts\msgothic.ttc', size=16)

## df = pd.read_csv("data/VOO_test.csv")
## df = pd.read_csv("data/VOO_2020-01-01_2024-03-22.csv")
## df = pd.read_csv("data/VOO_2010-09-10_2024-03-22_weekly.csv")
## df = pd.read_csv("data/VOO_2010-09-10_2024-03-22_monthly.csv")
df = pd.read_csv("data/SP500_1970-01-01_2024-03-22_monthly.csv")

# 変化率のデータを取得
change_rates = df['変化率 %'].str.rstrip('%').astype(float)

# 変化率%のデータから最大値と最小値を取得
max_change_rate = change_rates.max()
min_change_rate = change_rates.min()

# 最大値と最小値に基づいてビンの範囲を決定
## bins = np.arange(np.floor(min_change_rate * 2) / 2, np.ceil(max_change_rate * 2) / 2 + 0.5, 0.5)
## bins = np.arange(-100, 100, 0.5) # -100%から+100%まで0.5%刻みでビンを作成
start = -50
end = 50

bins = np.arange(start, end, 0.5) # -100%から+100%まで0.5%刻みでビンを作成

# ヒストグラムの設定
plt.figure(figsize=(10, 6))

# ヒストグラムの描画
# plt.hist(change_rates, bins=bins, edgecolor='black')
plt.hist(change_rates, bins=bins, edgecolor='black')

# グラフのタイトルと軸ラベルの設定
plt.title('変化率のヒストグラム', fontproperties=fp)
plt.xlabel('変化率%', fontproperties=fp)
plt.ylabel('頻度', fontproperties=fp)

plt.grid(True)

# x軸の範囲設定
plt.xlim(start, end)

# ヒストグラムの表示
plt.show()

mean     = np.mean(change_rates)
variance = np.var(change_rates)
std      = np.std(change_rates)

print(f"平均: {mean}")
print(f"分散: {variance}")
print(f"標準偏差: {std}")

#%%
