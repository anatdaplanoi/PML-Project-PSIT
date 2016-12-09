"""This program is shows graph percent of abortion"""
import numpy as np
import matplotlib.pyplot as plt

def graph_abort():
    """The graph shows the provider to terminate the pregnancy."""
    read = open("C:/Users/Planoi/project/project/PML-Project-PSIT/ผู้ให้บริการยุติการตั้งครรภ์.txt", "r")
    ind = np.arange(4)  # the x locations for the groups
    fig = plt.figure()
    ax_size = fig.add_subplot(111)
    da_lis = []
    year_2542 = []
    year_2554 = []
    year_2555 = []
    count = 0
    for i in read:
        if count > 1:
            da_lis.append(i.split())
        count += 1
    for i in range(1, 5):
        year_2542.append(float(da_lis[0][i]))
        year_2554.append(float(da_lis[1][i]))
        year_2555.append(float(da_lis[2][i]))
    rects1 = ax_size.bar(ind, year_2542, 0.24, color='r')
    rects2 = ax_size.bar(ind + 0.24, year_2554, 0.24, color='g')
    rects3 = ax_size.bar(ind + 0.24*2, year_2555, 0.24, color='b')
    ax_size.set_ylabel('abort(%)')
    ax_size.set_xticks(ind + 0.36)
    ax_size.set_xticklabels(('abort by public health', 'abort by not public health',\
        'unknow', 'self abortion'))
    ax_size.legend((rects1[0], rects2[0], rects3[0]), ('2542', '2554', '2555'))
    autolabel(rects1, ax_size)
    autolabel(rects2, ax_size)
    autolabel(rects3, ax_size)
    plt.show()

def autolabel(rects, ax_size):
    """Assign a name to the bar chart in the middle."""
    for i in rects:
        high = i.get_height()
        ax_size.text(i.get_x() + i.get_width()/2, 1.00*high, '%.1f'%float(high), ha='center',\
            va='bottom')

graph_abort()
