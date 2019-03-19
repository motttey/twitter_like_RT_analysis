# -*- coding:utf-8 -*-
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import glob

def main():
    file_list = glob.glob('result/*.json')
    ave_list = []
    for fname in file_list:
        if 'mt_tg' not in fname:
            df_u = pd.read_json(fname.replace('\\', '/'))
            if not df_u.empty: ave_list.append(df_u["ratio"].mean())

    df_f = pd.read_json('result/mt_tg.json')
    df_f["ratio"].plot()

    df = pd.DataFrame({"ratio":ave_list})
    df["ratio"].plot.bar()
    plt.xlim(0, len(df_f) - 1)
    plt.show()
    return

if __name__ == '__main__':
    main()
