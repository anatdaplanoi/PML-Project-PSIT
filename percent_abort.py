"""This program is shows graph about A​nalysis of teenage pregnancy"""
import numpy as np
import matplotlib.pyplot as plt
def main():
    """..."""
    read = open("E:/แอล/KMITL/PSIT/Project/PML-Project-PSIT/ผู้ให้บริการยุติการตั้งครรภ์.txt", "r")
    ind = np.arange(4)  # the x locations for the groups
    fig = plt.figure()
    ax = fig.add_subplot(111)
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
    rects1 = ax.bar(ind, year_2542, 0.24, color='r')
    rects2 = ax.bar(ind + 0.24, year_2554, 0.24, color='g')
    rects3 = ax.bar(ind + 0.24*2, year_2555, 0.24, color='b')
    ax.set_ylabel('abort(%)')
    ax.set_xticks(ind + 0.36)
    ax.set_xticklabels(('abort by public health', 'abort by not public health', 'unknow', 'abort by oneself'))
    ax.legend((rects1[0], rects2[0], rects3[0]), ('2542', '2554', '2555'))
    autolabel(rects1, ax)
    autolabel(rects2, ax)
    autolabel(rects3, ax)
    plt.show()

def autolabel(rects, ax):
    """..."""
    for i in rects:
        high = i.get_height()
        ax.text(i.get_x() + i.get_width()/2., 1.05*high, '%.1f'%float(high), ha='center', va='bottom')
main()
