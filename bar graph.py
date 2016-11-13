"""This program is bar graph about percentage teenage pregnancy of the second period."""
from matplotlib import pyplot as plt
from matplotlib import style
def bar():
    """This function is open file bar graph"""
    style.use('ggplot')
    read = open("C:/Users/Planoi/Desktop/project/project/data.txt", "r")
    da_lis = []
    da_year = []
    da_per_a = []
    da_per_b = []
    count = 0
    for i in read:
        if count != 0:
            da_lis.append(i.split())
        count = 1
    for i in range(len(da_lis)):
        da_year.append(int(da_lis[i][0]))
        #da_per_a.append(float(da_lis[i][4]))
        da_per_b.append(float(da_lis[i][5]))
    plt.bar(da_year, da_per_b, color='g', align='center')
    plt.title(' bar graph')
    plt.ylabel('percentage teenage pregnancy of the second period')
    plt.xlabel('Years')
    plt.show()
bar()
