"""This program is shows graph about percentage teenage pregnancy of the second period."""
import pylab
def main():
    """The graph shows the sex rate"""
    read = open("/Users/porpiraya/Desktop/alldata.txt", "r")
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
        da_per_a.append(float(da_lis[i][1]))
        da_per_b.append(float(da_lis[i][2]))
    pylab.plot(da_year, da_per_a,'-bo',linewidth=2)
    pylab.plot(da_year, da_per_b,'-ro',linewidth=2)
    labelProperty = dict(fontweight='bold',fontsize='12')
    pylab.xlabel('Years', labelProperty)
    pylab.ylabel('Percentage', labelProperty)
    legends = ('Sex rate of second years senior high school',
        'Sex rate of second years vocational',)
    pylab.legend(legends,
     loc='upper left', shadow=True, fancybox=True)
    pylab.xlim(2546,2556)
    pylab.xticks(da_year)
    pylab.grid(True)
    pylab.show()
main()
