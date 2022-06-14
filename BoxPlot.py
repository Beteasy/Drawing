import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def drawing_box():
    # Define constants
    COLORS = ["#de8a9b", "#d58964", "#3fad94", "#5eb164", "#5da2d4", "#9995c8", "#d186b9"]
    # COLORS = ["#de8a9b", "#d58964", "#3fad94", "#5eb164", "#5da2d4", "#9995c8"]

    # Read data
    data = pd.read_excel("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\xiaorong.xlsx")
    data = data.reindex(data.mean().sort_values().index, axis=1)

    # Drawing
    plt.rc('font', family='Times New Roman', size=14)
    bp = plt.boxplot(x=data, widths=0.3, zorder=2, labels=data.columns.values.tolist(), patch_artist=True)

    for patch, color in zip(bp['boxes'], COLORS):
        patch.set_facecolor(color)

    # for whisker in bp['whiskers']:
    #     # 这个是中间竖直线
    #     whisker.set(color='b', linewidth=2)

    # 设置四分位线样式
    for median in bp['medians']:
        median.set(color='black')

    # 设置异常点样式
    for index, flier in enumerate(bp['fliers']):
        flier.set(marker='D', markerfacecolor=COLORS[index], markeredgecolor=COLORS[index], markersize=5.0)



    # Set the figure
    plt.ylim((0.4, 1.0))
    fontdict_label = {"size": 15}
    plt.ylabel("ACC", fontdict=fontdict_label)
    # plt.xticks()
    plt.gcf().subplots_adjust(bottom=0.3)
    x = np.arange(len(data.columns))
    # print(plt.xlim()[0])
    plt.xticks(rotation=90)
    # plt.xlabel("Evaluation Metrics", fontdict=fontdict_label)
    # plt.axes().set_xticklabels(INDICATORS)
    # plt.legend(labels=METHODS, ncol=2, loc=9, edgecolor='black')
    plt.grid(axis='both', linestyle='--', alpha=0.4, zorder=0, linewidth=1.1)
    plt.plot([plt.xlim()[0], plt.xlim()[1]], [data.median()[-1], data.median()[-1]], c=COLORS[-1], linestyle="--", linewidth=1.25)

    # 设置边框
    ax = plt.axes()
    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置刻度
    plt.tick_params(top=True, bottom=True, left=True, right=True, direction='in')

    plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\xiaorong.png")
    plt.savefig("D:\\MRJOHN\\zixuan\\Drawing\\xiaorong\\xiaorong.pdf")
    plt.show()


drawing_box()