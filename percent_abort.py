import numpy as np
import matplotlib.pyplot as plt
read = open("C:/Users/Planoi/Desktop/project/PML-Project-PSIT-master/ผู้ให้บริการยุติการตั้งครรภ์.txt", "r")
N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
da_lis = []
year_2542 = []
year_2554 = []
year_2555 = []

count = 0
for i in read:
    if count != 0:
        da_lis.append(i.split())
    count = 1
year_2542.append(float(da_lis[1][1]))
year_2542.append(float(da_lis[1][2]))
year_2542.append(float(da_lis[1][3]))
year_2542.append(float(da_lis[1][4]))
year_2554.append(float(da_lis[2][1]))
year_2554.append(float(da_lis[2][2]))
year_2554.append(float(da_lis[2][3]))
year_2554.append(float(da_lis[2][4]))
year_2555.append(float(da_lis[3][1]))
year_2555.append(float(da_lis[3][2]))
year_2555.append(float(da_lis[3][3]))
year_2555.append(float(da_lis[3][4]))
print(year_2542)

yvals = year_2542
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = year_2554
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = year_2555
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('abort(%)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('abort by public health', 'abort by not public health', 'unknow', 'abort by oneself') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('2542', '2554', '2555') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%.1f'%float(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()