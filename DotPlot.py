import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
    字体：坐标：  label大一号
    网格灰色虚线  比原始粗一点  更透明一点  中间多一条线
    圆点  稍微大一点  
    legend边框黑色
    四个边都要刻度  内向
"""


def drawing_compare():
    # Define constants
    METHODS = ["DeepBind", "DeepSEA", "DanQ", "DLBSS", "CRPTS", "CNN_TF", "MTTFSite", "Our"]
    INDICATORS = ['Accuracy', 'ROC-AUC', 'PR-AUC', 'F1-Score']
    COLORS = ["black", "#9de5ff", "#3c6cb5", "#2cabb8", "#70c174", "#f7b64e", "#fcbad3", "#f1695e"]

    # Read data
    data = pd.read_excel("D:\\MRJOHN\\zixuan\\Drawing\\compare.xlsx")

    Accuracy = data.iloc[:, data.columns.str.contains("Accuracy")]
    accuracy_mean = Accuracy.mean(axis=0).values
    # accuracy_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    ROC_AUC = data.iloc[:, data.columns.str.contains("ROC-AUC")]
    roc_auc_mean = ROC_AUC.mean(axis=0).values
    # roc_auc_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    PR_AUC = data.iloc[:, data.columns.str.contains("PR-AUC")]
    pr_auc = PR_AUC.mean(axis=0).values
    # pr_auc = [1, 2, 3, 4, 5, 6, 7, 8]
    F1_Score = data.iloc[:, data.columns.str.contains("F1-Score")]
    f1_score_mean = F1_Score.mean(axis=0).values
    # f1_score_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    # x = [0.45, 0.5, 0.75, 0.85]
    x = np.arange(0, 1, 0.25)
    # y = [accuracy_mean, roc_auc_mean, pr_auc, f1_score_mean]

    # fig, axes = plt.subplots(1, 1)
    # [accuracy_mean[i] * 150, roc_auc_mean[i] * 150, pr_auc[i] * 150, f1_score_mean[i] * 150]
    plt.rc('font', family='Times New Roman', size=14)
    k=1
    scale = 90
    for i in range(len(accuracy_mean)):
        # plt.scatter(x=x, y=[accuracy_mean[i], roc_auc_mean[i], pr_auc[i], f1_score_mean[i]], c=COLORS[i], s=[(accuracy_mean[i] * scale) * k, (roc_auc_mean[i] * scale)  * k, (pr_auc[i] * scale)  * k, (f1_score_mean[i] * scale)  * k], zorder=100, alpha=0.5)
        plt.scatter(x=x, y=[accuracy_mean[i], roc_auc_mean[i], pr_auc[i], f1_score_mean[i]], c=COLORS[i], s=100, zorder=100, alpha=0.5)
        # k=k+0.1


    plt.ylim((0.75, 1))
    fontdict_label = {"size": 15}
    plt.ylabel("Metrics Value", fontdict=fontdict_label)
    # plt.yticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1])
    plt.xticks(x)
    # plt.xticks([0, 0.25, 0.5, 0.75])
    plt.xlabel("Evaluation Metrics", fontdict=fontdict_label)
    plt.axes().set_xticklabels(INDICATORS)
    plt.legend(labels=METHODS, ncol=2, loc=8, edgecolor='black')
    plt.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)

    # 设置边框
    ax = plt.axes()

    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置刻度
    plt.tick_params(top=True, bottom=True, left=True, right=True, direction='in')
    # # plt.minorticks_on()
    # # for i, tick in enumerate()

    # fontdict_label = {"size": 15,  "family": 'Times New Roman'}
    # axes.set_xlabel("Evaluation Metrics", fontdict=fontdict_label)
    # axes.set_ylabel("Metrics Value", fontdict=fontdict_label)
    # axes.tick_params(top=True, bottom=True, left=True, right=True, direction='in', labelsize=14)
    # axes.xaxis.set_ticks(x)
    # axes.set_xticklabels(INDICATORS)
    # axes.yaxis.set_ticks([0.75, 0.8, 0.85, 0.9, 0.95, 1])
    # # axes.yaxis.set_ticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1], ['0.75', '0.775', '0.8', '0.825', '0.85', '0.875', '0.9', '0.925', '0.95', '0.975','1'])
    # # a = ['%.2f'%oi for oi in [0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1]]
    # # axes.yaxis.set_ticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1], [0.75, 0.8, 0.85,0.9, 0.95,1])
    # axes.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)
    # # for i, tick in enumerate(axes.xaxis.get_ticklabels()):
    # #     if i % 2 != 0:
    # #         tick.set_visible(False)
    # # for i, tick in enumerate(axes.yaxis.get_ticklabels()):
    # #     if i % 2 != 0 and i != (len(axes.yaxis.get_ticklabels()) - 1):
    # #         tick.set_visible(False)
    # axes.legend(labels=METHODS, ncol=2, loc=8)
    plt.show()



def drawing_compare1():
    # Define constants
    METHODS = ["DeepBind", "DeepSEA", "DanQ", "DLBSS", "CRPTS", "CNN_TF", "MTTFSite", "Our"]
    INDICATORS = ['Accuracy', 'ROC-AUC', 'PR-AUC', 'F1-Score']
    COLORS = ["black", "#9de5ff", "#3c6cb5", "#2cabb8", "#70c174", "#f7b64e", "#fcbad3", "#f1695e"]

    # Read data
    data = pd.read_excel("D:\\MRJOHN\\zixuan\\Drawing\\compare_1.xlsx")

    Accuracy = data.iloc[:, data.columns.str.contains("Accuracy")]
    accuracy_mean = Accuracy.mean(axis=0).values
    # accuracy_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    ROC_AUC = data.iloc[:, data.columns.str.contains("ROC-AUC")]
    roc_auc_mean = ROC_AUC.mean(axis=0).values
    # roc_auc_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    PR_AUC = data.iloc[:, data.columns.str.contains("PR-AUC")]
    pr_auc = PR_AUC.mean(axis=0).values
    # pr_auc = [1, 2, 3, 4, 5, 6, 7, 8]
    F1_Score = data.iloc[:, data.columns.str.contains("F1-Score")]
    f1_score_mean = F1_Score.mean(axis=0).values
    # f1_score_mean = [1, 2, 3, 4, 5, 6, 7, 8]
    # x = [0.45, 0.5, 0.75, 0.85]
    x = np.arange(0, 1, 0.25)
    # y = [accuracy_mean, roc_auc_mean, pr_auc, f1_score_mean]

    # fig, axes = plt.subplots(1, 1)
    # [accuracy_mean[i] * 150, roc_auc_mean[i] * 150, pr_auc[i] * 150, f1_score_mean[i] * 150]
    plt.rc('font', family='Times New Roman', size=14)
    # k=1
    # scale = 90
    for i in range(len(accuracy_mean)):
        # plt.scatter(x=x, y=[accuracy_mean[i], roc_auc_mean[i], pr_auc[i], f1_score_mean[i]], c=COLORS[i], s=[(accuracy_mean[i] * scale) * k, (roc_auc_mean[i] * scale)  * k, (pr_auc[i] * scale)  * k, (f1_score_mean[i] * scale)  * k], zorder=100, alpha=0.5)
        plt.scatter(x=x, y=[accuracy_mean[i], roc_auc_mean[i], pr_auc[i], f1_score_mean[i]], c=COLORS[i], s=100, zorder=100, alpha=0.5)
        # k=k+0.1

    plt.ylim((0.73, 1))
    fontdict_label = {"size": 15}
    plt.ylabel("Metrics Value", fontdict=fontdict_label)
    # plt.yticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1])
    plt.xticks(x)
    # plt.xticks([0, 0.25, 0.5, 0.75])
    plt.xlabel("Evaluation Metrics", fontdict=fontdict_label)
    plt.axes().set_xticklabels(INDICATORS)
    plt.legend(labels=METHODS, ncol=2, loc=8, edgecolor='black')
    plt.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)

    # 设置边框
    ax = plt.axes()

    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置刻度
    plt.tick_params(top=True, bottom=True, left=True, right=True, direction='in')
    # # plt.minorticks_on()
    # # for i, tick in enumerate()

    # fontdict_label = {"size": 15,  "family": 'Times New Roman'}
    # axes.set_xlabel("Evaluation Metrics", fontdict=fontdict_label)
    # axes.set_ylabel("Metrics Value", fontdict=fontdict_label)
    # axes.tick_params(top=True, bottom=True, left=True, right=True, direction='in', labelsize=14)
    # axes.xaxis.set_ticks(x)
    # axes.set_xticklabels(INDICATORS)
    # axes.yaxis.set_ticks([0.75, 0.8, 0.85, 0.9, 0.95, 1])
    # # axes.yaxis.set_ticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1], ['0.75', '0.775', '0.8', '0.825', '0.85', '0.875', '0.9', '0.925', '0.95', '0.975','1'])
    # # a = ['%.2f'%oi for oi in [0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1]]
    # # axes.yaxis.set_ticks([0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1], [0.75, 0.8, 0.85,0.9, 0.95,1])
    # axes.grid(linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)
    # # for i, tick in enumerate(axes.xaxis.get_ticklabels()):
    # #     if i % 2 != 0:
    # #         tick.set_visible(False)
    # # for i, tick in enumerate(axes.yaxis.get_ticklabels()):
    # #     if i % 2 != 0 and i != (len(axes.yaxis.get_ticklabels()) - 1):
    # #         tick.set_visible(False)
    # axes.legend(labels=METHODS, ncol=2, loc=8)
    plt.show()


drawing_compare1()