"""This program is shows graph about percentage teenage pregnancy of the second period."""
import pylab
def main():
    """This function is open file"""
    read = open("E:/แอล/KMITL/PSIT/Project/alldata.txt", "r")
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
        da_per_a.append(float(da_lis[i][4]))
        da_per_b.append(float(da_lis[i][5]))
    pylab.plot(da_year, da_per_a,'-bo',linewidth=2)
    pylab.plot(da_year, da_per_b,'-ro',linewidth=2)
    labelProperty = dict(fontweight='bold',fontsize='12')
    pylab.xlabel('Years', labelProperty)
    pylab.ylabel('Percentage', labelProperty)
    legends = ('Percent of the 10-14 age',
        'Percent of the 15-19 age',)
    pylab.legend(legends,
     loc='upper left', shadow=True, fancybox=True)
    pylab.xlim(2533,2555)
    pylab.xticks(da_year)
    pylab.grid(True)
    pylab.show()
main()
