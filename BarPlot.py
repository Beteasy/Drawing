import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def drawing_compare3():
    # Define constants
    METHODS = ["MTTFSite", "Our"]
    INDICATORS = ['Accuracy', 'Kappa', 'F1-Score']
    COLORS = ["#5a7ca9", "#ca7791"]

    HATCHES = ['/', '.']

    # Read data
    data = pd.read_excel("D:\\MRJOHN\\zixuan\\Drawing\\compare_3.xlsx")

    Accuracy = data.iloc[:, data.columns.str.contains("Accuracy")]
    accuracy_mean = Accuracy.mean(axis=0).values
    Kappa = data.iloc[:, data.columns.str.contains("Kappa")]
    kappa_mean = Kappa.mean(axis=0).values
    F1_Score = data.iloc[:, data.columns.str.contains("F1-Score")]
    f1_score_mean = F1_Score.mean(axis=0).values
    # x = np.linspace(0, 1, 3)
    x = np.arange(len(INDICATORS))

    n = len(accuracy_mean)
    TOTAL_WIDTH = len(INDICATORS)

    width = TOTAL_WIDTH / (len(INDICATORS)) / 6
    # width = 0.1
    x = x - (TOTAL_WIDTH - width) / 2
    plt.rc('font', family='Times New Roman', size=14)
    # x + i * width, height = [[accuracy_mean[i], kappa_mean[i], f1_score_mean[i]], width = width
    for i in range(len(accuracy_mean)):
        # plt.bar(x=x, height=[accuracy_mean[i], kappa_mean[i], f1_score_mean[i]], width=width,
        #         color=COLORS[i], hatch=HATCHES[i])
        plt.bar(x=(x + ((i-n/2) * width)), height=[accuracy_mean[i], kappa_mean[i], f1_score_mean[i]], width=width, color=COLORS[i], hatch=HATCHES[i], edgecolor='black', linewidth=1.5)
        # break


    # Drawing

    # Set the figure
    plt.ylim((0.1, 0.9))
    fontdict_label = {"size": 15}
    plt.ylabel("Metrics Value", fontdict=fontdict_label)
    plt.xticks(x)
    plt.xlabel("Evaluation Metrics", fontdict=fontdict_label)
    plt.axes().set_xticklabels(INDICATORS)
    plt.legend(labels=METHODS, ncol=1, loc=9, edgecolor='black')
    plt.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)

    # 设置边框
    ax = plt.axes()
    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置刻度
    plt.tick_params(top=True, bottom=True, left=True, right=True, direction='in')

    plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\compare_3_bar.png")
    plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\compare_3_bar.pdf")
    plt.show()


drawing_compare3()