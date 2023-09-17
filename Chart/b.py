import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_radar(labels, values, colors):
    
    #描画領域の作成
    fig, ax = plt.subplots(1, 1, figsize=(5, 5), subplot_kw={'projection': 'polar'})

    #チャートを順に描画
    for i, data in enumerate(zip(values, colors)):        
        d = data[0]
        color = data[1]
        
        #要素数の連番作成
        angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
        #閉じた多角形に変換
        value = np.concatenate((d, [d[0]]))  
        
        #線の描画
        ax.plot(angles, value, 'o-', color=color)
        #塗りつぶし
        ax.fill(angles, value, alpha=0.25, facecolor=color)  

    #軸ラベルの設定
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  
    #描画開始位置の指定（N: North）
    ax.set_theta_zero_location('N')
    
    plt.show()
    plt.close(fig)
    
#ここから
if __name__ == '__main__':

    labels = ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3']
    data = [
        [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
        [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
        [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
        [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
        [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]
    ]
    colors = ['b', 'r', 'g', 'm', 'y']

    plot_radar(labels, data, colors)