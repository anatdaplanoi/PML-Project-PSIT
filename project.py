"""This program is shows graph about A​nalysis of teenage pregnancy"""
from pylab import *
def openfile():
    """This function is open file"""
    read = open("C:/Users/Aal/Desktop/project/data.txt", "r")
    da_lis = []
    da_year = []
    da_amount = []
    for i in read:
        da_lis.append(i.split())
    for i in range(len(da_lis)):
        da_year.append(int(da_lis[i][0]))
        da_amount.append(float(da_lis[i][4]))
    print(da_year)
    print(da_amount)
openfile()
