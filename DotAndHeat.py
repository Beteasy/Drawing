import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def drawing_dot_head():
    # Define constants
    # METHODS = ["DeepBind", "DeepSEA", "DanQ", "DLBSS", "CRPTS", "CNN_TF", "MTTFSite", "Our"]
    # INDICATORS = ['Accuracy', 'ROC-AUC', 'PR-AUC', 'F1-Score']
    # COLORS = ["black", "#9de5ff", "#3c6cb5", "#2cabb8", "#70c174", "#f7b64e", "#fcbad3", "#f1695e"]
    COLORS = ["#9de5ff", "#3c6cb5", "#2cabb8", "#70c174", "#f7b64e"]
    MARKERS = ['o', '^', '*']

    # Read data
    data = pd.read_excel("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\shape_xiaorong.xlsx", index_col=0)

    # Accuracy = data.iloc[:, data.columns.str.contains("Accuracy")]
    # accuracy_mean = Accuracy.mean(axis=0).values
    # ROC_AUC = data.iloc[:, data.columns.str.contains("ROC-AUC")]
    # roc_auc_mean = ROC_AUC.mean(axis=0).values
    # PR_AUC = data.iloc[:, data.columns.str.contains("PR-AUC")]
    # pr_auc = PR_AUC.mean(axis=0).values
    # F1_Score = data.iloc[:, data.columns.str.contains("F1-Score")]
    # f1_score_mean = F1_Score.mean(axis=0).values
    columns = data.columns.values
    for column in columns[1:]:
        data[column] = data[columns[0]] - data[column]
    x = np.arange(len(data.index))
    # 设置画布大小，默认640x480
    plt.figure(figsize=(640, 480))
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.rc('font', family='Times New Roman', size=14)
    for i in np.arange(1, len(columns)):
        plt.scatter(x=x, y=data.iloc[:, i], c=COLORS[i], s=100, zorder=100, alpha=0.5, marker=MARKERS[i-1])


    # plt.ylim((0.75, 1))

    fontdict_label = {"size": 15}
    plt.ylabel("Accuracy", fontdict=fontdict_label)
    plt.xticks(x, rotation=90)
    plt.xlabel("TFs", fontdict=fontdict_label)
    plt.axes().set_xticklabels(data.index.values)
    plt.legend(labels=columns[1:], ncol=3, loc=9, edgecolor='black')
    plt.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)

    # 设置边框
    ax = plt.axes()

    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置刻度
    plt.tick_params(top=True, bottom=True, left=True, right=True, direction='in')
    # plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\shape_xiaorong.png")
    # plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\shape_xiaorong.pdf")
    plt.show()
drawing_dot_head()