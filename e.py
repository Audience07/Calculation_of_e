#高精度库
import decimal
#延时
import time
#系统操作
import os
#数学库
import math
def calc_e():
    #设置n
    n:int = 0
    #e是求和后的结果,因此初始值为0
    e=decimal.Decimal(0)
    #设置精度
    decimal.getcontext().prec=190
    #死循环
    while True:
        #1/n!
        Temp=decimal.Decimal(1)/math.factorial(n)
        e+=Temp
        n+=1
        print(f"第{n+1}次展开:{e}")
        time.sleep(0.1)
        #os.system("cls")
    return e


if __name__=="__main__":
    calc_e()