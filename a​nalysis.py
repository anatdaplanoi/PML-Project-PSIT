"""This program is shows graph about A​nalysis of teenage pregnancy"""
import pylab
def main():
    """This function is open file"""
    read = open("C:/Users/Planoi/Desktop/project/project/data.txt", "r")
    da_lis = []
    da_year = []
    da_amount = []
    count = 0
    for i in read:
        if count != 0:
            da_lis.append(i.split())
        count = 1
    for i in range(len(da_lis)):
        da_year.append(int(da_lis[i][0]))
        da_amount.append(float(da_lis[i][6]))
    pylab.plot(da_year, da_amount,'-bo',linewidth=2)
    labelProperty = dict(fontweight='bold',fontsize='12')
    pylab.xlabel('Years', labelProperty)
    pylab.ylabel('Pregnancy', labelProperty)
    legends = ('Total of Teenage Pregnancy',)
    pylab.legend(legends,
     loc='upper left', shadow=True, fancybox=True)
    pylab.xlim(2533,2555)
    pylab.xticks(da_year)
    pylab.grid(True)
    pylab.show()
main()
