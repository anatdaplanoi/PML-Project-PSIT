import pylab
read = open("C:/Users/Planoi/Desktop/project/project/data.txt", "r")
da_lis = []
da_year = []
da_amount = []
for i in read:
    da_lis.append(i.split())
for i in range(len(da_lis)):
    da_year.append(int(da_lis[i][0]))
    da_amount.append(float(da_lis[i][4]))
pylab.plot(da_year, da_amount,'-bo',linewidth=1)
labelProperty = dict(fontweight='bold',fontsize='12')
pylab.xlabel('Years', labelProperty)
pylab.ylabel('Pregnancy', labelProperty)
legends = ('Average total time')
pylab.legend(legends,
 loc='upper left', shadow=True, fancybox=True)
pylab.xlim(2500,2560)
pylab.xticks(da_year)
pylab.grid(True)
pylab.show()
